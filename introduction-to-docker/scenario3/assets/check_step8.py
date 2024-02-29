import sys
import subprocess
import json

def check_image_config(image_name):
    # Get image info
    result = subprocess.run(['docker', 'inspect', image_name], capture_output=True, text=True)
    details = json.loads(result.stdout)

    # Check image name and version
    if 'python:3.6' not in details[0]['Config']['Image']:
        return False

    # Check working directory
    if details[0]['Config']['WorkingDir'] != '/opt':
        return False

    # Check ENTRYPOINT
    if details[0]['Config']['Entrypoint'] != ["python", "app.py"]:
        return False

    return True

if __name__ == '__main__':
    image_name = sys.argv[1]
    if check_image_config(image_name):
        sys.exit(0)
    else:
        sys.exit(1)
