import sys
import subprocess
import json

def check_port_mapping(container_id):
    result = subprocess.run(['docker', 'inspect', container_id], capture_output=True, text=True)
    details = json.loads(result.stdout)

    ports = details[0]['NetworkSettings']['Ports']
    if '8080/tcp' not in ports or ports['8080/tcp'][0]['HostPort'] != '8282':
        return False

    return True

if __name__ == '__main__':
    container_id = sys.argv[1]
    if check_port_mapping(container_id):
        sys.exit(0)
    else:
        sys.exit(1)
