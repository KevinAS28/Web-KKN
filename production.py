import os
import configparser

cwd = os.getcwd()

production_config = configparser.ConfigParser()
production_config.read(os.path.join(cwd, 'production', 'production_config.ini'))
uwsgi_config = open(os.path.join(cwd, 'production', 'uwsgi.ini')).read()
nginx_config = open(os.path.join(cwd, 'production', 'web.ini')).read()

def replace_config(config_string:str, config_key:str, config_value:str=None):
    return config_string.replace('{{%s}}'%(config_key), config_value if not (config_value is None) else config(config_key))

def config(key):
    return production_config.get('PRODUCTION', key)


project_name = config('PROJECT_NAME')
uwsgi_socket = os.path.join(config('PROJECT_PATH'), f'{project_name}_uwsgi.sock')
uwsgi_path = os.path.join(config('PROJECT_PATH'), f'{project_name}_uwsgi.ini')
print(f'uwsgi --ini {uwsgi_path} -s {uwsgi_socket} --chmod-socket=777')

#generate uwsgi configuration based on production config
uwsgi_config = replace_config(uwsgi_config, 'HOST_WITH_PROTOCOL', f'{config("PROTOCOL")}://{config("HOST")}')
uwsgi_config = replace_config(uwsgi_config, 'VIRTUALENV_PATH')
uwsgi_config = replace_config(uwsgi_config, 'PROJECT_PATH')
uwsgi_config = replace_config(uwsgi_config, 'PY_WSGI_FILE', os.path.join(config("PROJECT_PATH"), config("PROJECT_MAIN_APP"), 'wsgi.py'))
uwsgi_config = replace_config(uwsgi_config, 'PROJECT_SETTINGS', os.path.join(config("PROJECT_PATH"), config("PROJECT_MAIN_APP"), 'settings.py'))

#generate nginx configuration based on production config
nginx_config = replace_config(nginx_config, 'HOST')
nginx_config = replace_config(nginx_config, 'WWW_HOST', f'www.{config("HOST")}')
nginx_config = replace_config(nginx_config, 'UWSGI_SOCKET', uwsgi_socket)

with open(os.path.join('/etc/nginx/sites-available', f'{project_name}.conf'), 'w+') as nginx_config_file:
    nginx_config_file.write(nginx_config)

os.system(f'ln -s /etc/nginx/sites-available/{project_name}.conf /etc/nginx/sites-enabled/')

with open(uwsgi_path, 'w+') as uwsgi_config_file:
    uwsgi_config_file.write(uwsgi_config)

run_instructions = f'''
uwsgi --ini {uwsgi_path} -s {uwsgi_socket} --chmod-socket=777
service nginx restart
'''