import subprocess
import sys
import json

def check_image_in_registry(image_name):
    registry_url = "http://localhost:5000/v2"
    endpoint = f"{registry_url}/{image_name}/tags/list"
    
    try:
        result = subprocess.run(['curl', '-s', endpoint], capture_output=True, text=True)
        if result.returncode != 0 or 'errors' in result.stdout:
            print(f"ERROR: Failed to get {image_name} from registry.")
            return False
        
        data = json.loads(result.stdout)
        if 'tags' in data and data['tags']:
            return True
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return False
    
    return False

if __name__ == "__main__":
    images = sys.argv[1:]
    all_exist = True
    
    for image in images:
        if not check_image_in_registry(image):
            all_exist = False
            print(f"{image} is not found in registry.")
    
    if all_exist:
        print("All images are found in registry.")
        sys.exit(0)
    else:
        sys.exit(1)