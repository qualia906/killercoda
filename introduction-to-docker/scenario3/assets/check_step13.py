import sys
import subprocess
import json

def check_image_details(image_name):
    # Get image info
    result = subprocess.run(['docker', 'inspect', image_name], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Could not get image details for {image_name}.")
        return False

    details = json.loads(result.stdout)[0]

    # Check ports
    if "8080/tcp" not in details['Config']['ExposedPorts']:
        print("Port 8080 is not published correctly.")
        return False

    # Check working directory
    if details['Config']['WorkingDir'] != '/opt':
        print("Working directory is not /opt.")
        return False

    # Check ENTRYPOINT
    if details['Config']['Entrypoint'] != ["python", "app.py"]:
        print("ENTRYPOINT is not ['python', 'app.py']")
        return False

    return True

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)

    image_name = sys.argv[1]
    if check_image_details(image_name):
        print(f"Image {image_name} is correct.")
        sys.exit(0)
    else:
        sys.exit(1)
