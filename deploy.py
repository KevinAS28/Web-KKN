import os
from datetime import datetime as dt,date

def log(msg, end='\n'):
    with open('deploypy_log.txt', 'a+') as fd:
        fd.write(f'{dt.now()}\n{msg}{end}\n{"*"*15}')
    print(msg+end)

os_commands = [
    'python3 env_preparations.py',
    'python3  -m pip install -r requirements.txt',
    'python3 manage.py makemigrations',
    'python3 manage.py migrate',
    
]

def unzip_static():
    backup_db_name = f'db.sqlite3.{str(date.today())}'
    os.system(f'cp db.sqlite3 {backup_db_name}')
    log('backing up db to ')
    if os.path.isfile('static.zip'):
        os.system('unzip -q -o static.zip')


if __name__=='__main__':
    
    for command in os_commands:
        try:
            log(f'running command: {command}')
            os.system(command)
        except Exception as e:
            log(f'ERROR command: {command}: {str(e)}')
            exit(1)

    log('unzipping static...')
    unzip_static()

exit(0)