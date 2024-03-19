import sys
import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def compare_yaml(file1, file2):
    yaml1 = load_yaml(file1)
    yaml2 = load_yaml(file2)
    
    return yaml1 == yaml2

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python compare_yaml.py file1.yaml file2.yaml")
        sys.exit(1)
    
    is_equal = compare_yaml(sys.argv[1], sys.argv[2])
    if is_equal:
        print("YAML files are equivalent.")
        sys.exit(0)
    else:
        print("YAML files are not equivalent.")
        sys.exit(1)
