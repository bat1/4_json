import json
import os 

def load_data(file):
    
    with open(file, 'r') as handle:
        parsed = json.load(handle)
        return parsed
        
def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii = False, indent=4, sort_keys=True))
    
if __name__ == '__main__':

    file_path = os.path.abspath(input("Введите путь к файлу с JSON: ").strip()) # например /projects/4_json/jsonfile.txt
    file = os.path.basename(file_path)
    data = load_data(file_path)
    pretty_print_json(data)
