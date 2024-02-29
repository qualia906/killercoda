import sys
import subprocess
import json

def is_detached_mode(container_name):
    result = subprocess.run(['docker', 'inspect', container_name], capture_output=True, text=True)
    if result.returncode != 0:
        return False

    details = json.loads(result.stdout)
    if not details:
        return False

    try:
        config = details[0]['Config']
        if not config['AttachStdin'] and not config['AttachStdout'] and not config['AttachStderr']:
            return True
    except KeyError:
        return False

    return False

if __name__ == '__main__':
    container_name = sys.argv[1]
    if is_detached_mode(container_name):
        sys.exit(0)
    else:
        sys.exit(1)