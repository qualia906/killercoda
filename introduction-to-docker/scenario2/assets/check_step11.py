import sys
import subprocess
import json

def check_mysql_config(container_id):
    # Get container info
    result = subprocess.run(['docker', 'inspect', container_id], capture_output=True, text=True)
    details = json.loads(result.stdout)

    # Check env var
    env_vars = details[0]['Config']['Env']
    mysql_root_password_var = 'MYSQL_ROOT_PASSWORD=db_pass123'
    if mysql_root_password_var not in env_vars:
        return False

    return True

if __name__ == '__main__':
    container_id = sys.argv[1]
    if check_mysql_config(container_id):
        sys.exit(0)
    else:
        sys.exit(1)
