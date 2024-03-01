import sys
import subprocess
import json

def check_container_command(container_id):
    # Get container info
    result = subprocess.run(['docker', 'inspect', container_id], capture_output=True, text=True)
    if result.returncode != 0:
        print("Failed to get container info.")
        return False

    details = json.loads(result.stdout)

    # Check command
    if details[0]['Config']['Cmd'] != ['sleep', '1000']:
        print("Container command is not 'sleep 1000'.")
        return False

    return True

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)

    container_id = sys.argv[1]
    if check_container_command(container_id):
        print("OK")
        sys.exit(0)
    else:
        sys.exit(1)
