import sys
import json
import xml.etree.ElementTree as ET
import yaml

def parse_args():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]

def load_data(filepath):
    if filepath.endswith('.json'):
        with open(filepath, 'r') as file:
            return json.load(file)
    elif filepath.endswith('.xml'):
        tree = ET.parse(filepath)
        return tree.getroot()
    elif filepath.endswith('.yml') or filepath.endswith('.yaml'):
        with open(filepath, 'r') as file:
            return yaml.safe_load(file)

def save_data(data, filepath):
    if filepath.endswith('.json'):
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
    elif filepath.endswith('.xml'):
        tree = ET.ElementTree(data)
        tree.write(filepath)
    elif filepath.endswith('.yml') or filepath.endswith('.yaml'):
        with open(filepath, 'w') as file:
            yaml.safe_dump(data, file)

if __name__ == "__main__":
    file1, file2 = parse_args()
    data = load_data(file1)
    save_data(data, file2)