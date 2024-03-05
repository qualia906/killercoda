import subprocess
import json
import sys

def get_containers_info():
    result = subprocess.run(['docker', 'ps', '--format', '{{.Names}}'], capture_output=True, text=True, check=True)
    container_names = result.stdout.strip().split('\n')
    
    containers_info = []
    for name in container_names:
        inspect_result = subprocess.run(['docker', 'inspect', name], capture_output=True, text=True, check=True)
        containers_info.append(json.loads(inspect_result.stdout)[0])
    
    return containers_info

def check_containers(containers_info):
    redis_found, clickcounter_found = False, False
    for container in containers_info:
        image = container['Config']['Image']
        names = container['Name']
        ports = container.get('NetworkSettings', {}).get('Ports', {})
        if 'redis:alpine' in image:
            redis_found = True
        if 'qualia906/click-counter' in image and '5000/tcp' in ports and any(p['HostPort'] == '8085' for p in ports['5000/tcp']):
            clickcounter_found = True
    
    return redis_found and clickcounter_found

def main():
    containers_info = get_containers_info()
    if check_containers(containers_info):
        print("Docker Compose services are up and running correctly.")
        sys.exit(0)
    else:
        print("Docker Compose services are not running as expected.")
        sys.exit(1)

if __name__ == '__main__':
    main()
