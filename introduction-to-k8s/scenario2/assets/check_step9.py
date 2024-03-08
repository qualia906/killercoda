import sys
import subprocess
import json

def check_container_config(container_id):
    # Get container info
    result = subprocess.run(['docker', 'inspect', container_id], capture_output=True, text=True)
    details = json.loads(result.stdout)

    # Check port conf
    ports = details[0]['NetworkSettings']['Ports']
    if '8080/tcp' not in ports or ports['8080/tcp'][0]['HostPort'] != '38285':
        return False

    # Check env var
    env_vars = details[0]['Config']['Env']
    if 'APP_COLOR=green' not in env_vars:
        return False

    # Check image name
    image = details[0]['Config']['Image']
    if 'qualia906/simple-webapp' not in image:
        return False

    # Check detached mode
    config = details[0]['Config']
    if config['AttachStdin'] or config['AttachStdout'] or config['AttachStderr']:
        return False

    return True

if __name__ == '__main__':
    container_id = sys.argv[1]
    if check_container_config(container_id):
        sys.exit(0)
    else:
        sys.exit(1)
