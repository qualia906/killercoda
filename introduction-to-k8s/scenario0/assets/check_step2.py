import subprocess
import json
import sys

def check_container(container_name, expected_image):
    try:
        result = subprocess.run(['docker', 'inspect', container_name], capture_output=True, text=True, check=True)
        details = json.loads(result.stdout)[0]

        image = details['Config']['Image']
        attach_stdout = details['Config']['AttachStdout']
        attach_stderr = details['Config']['AttachStderr']

        if image != expected_image:
            print(f"{container_name} is not running from the expected image. Found {image}, expected {expected_image}.")
            return False
        
        if attach_stdout or attach_stderr:
            print(f"{container_name} is not running in detached mode.")
            return False

        print(f"{container_name} is running from the expected image {expected_image} in detached mode.")
        return True
    except subprocess.CalledProcessError:
        print(f"Failed to get container details for {container_name}.")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 check_container_running.py <container_name> <expected_image>")
        sys.exit(1)

    container_name = sys.argv[1]
    expected_image = sys.argv[2]

    if check_container(container_name, expected_image):
        sys.exit(0)
    else:
        sys.exit(1)
