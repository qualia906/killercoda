import sys
import subprocess
import json

def check_container_details(container_id):
    # Get container info
    result = subprocess.run(['docker', 'inspect', container_id], capture_output=True, text=True)
    details = json.loads(result.stdout)

    # Check port binding
    ports = details[0]['NetworkSettings']['Ports']
    if '5000/tcp' not in ports or ports['5000/tcp'][0]['HostPort'] != '5000':
        print("Port binding is not correct.")
        return False

    # Check detached mode
    if details[0]['Config']['AttachStdout'] or details[0]['Config']['AttachStderr']:
        print("Container is not in detached mode.")
        return False

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python check_step4.py <container_id>")
        sys.exit(1)

    container_id = sys.argv[1]
    if check_container_details(container_id):
        print("Container is in correct state.")
        sys.exit(0)
    else:
        sys.exit(1)
