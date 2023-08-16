import os
import configparser

cwd = os.getcwd()

production_config = configparser.ConfigParser()
production_config.read(os.path.join(cwd, 'production', 'production_config.ini'))
uwsgi_config = open(os.path.join(cwd, 'production', 'uwsgi.ini')).read()
nginx_config = open(os.path.join(cwd, 'production', 'web.ini')).read()

def replace_config(config_string:str, config_key:str, config_value:str=None):
    return config_string.replace('{{%s}}'%(config_key), config_value if not (config_value is None) else production_config.get(config_key))


project_name = production_config.get('PROJECT_NAME')
uwsgi_socket = os.path.join(production_config.get('PROJECT_PATH'), f'{project_name}_uwsgi.sock')
uwsgi_path = os.path.join(production_config.get('PROJECT_PATH'), f'{project_name}_uwsgi.ini')

#generate uwsgi configuration based on production config
uwsgi_config = replace_config(uwsgi_config, 'HOST_WITH_PROTOCOL', f'{production_config.get("PROTOCOL")}://{production_config.get("HOST")}')
uwsgi_config = replace_config(uwsgi_config, 'VIRTUALENV_PATH')
uwsgi_config = replace_config(uwsgi_config, 'PROJECT_PATH')
uwsgi_config = replace_config(uwsgi_config, 'PY_WSGI_FILE', os.path.join(production_config.get("PROJECT_PATH"), production_config.get("PROJECT_MAIN_APP"), 'wsgi.py'))
uwsgi_config = replace_config(uwsgi_config, 'PROJECT_SETTINGS', os.path.join(production_config.get("PROJECT_PATH"), production_config.get("PROJECT_MAIN_APP"), 'settings.py'))

#generate nginx configuration based on production config
nginx_config = replace_config(nginx_config, 'HOST')
nginx_config = replace_config(nginx_config, f'www.{production_config.get("HOST")}')
nginx_config = replace_config(nginx_config, 'UWSGI_SOCKET', uwsgi_socket)

with open(os.path.join('/etc/nginx/sites-available', f'{project_name}.conf'), 'w+') as nginx_config_file:
    nginx_config_file.write(nginx_config)

os.system(f'ln -s /etc/nginx/sites-available/{project_name}.conf /etc/nginx/sites-enabled/')

with open(uwsgi_path, 'w+') as uwsgi_config_file:
    uwsgi_config_file.write(uwsgi_config)
