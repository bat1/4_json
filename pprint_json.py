import json
import os 

def load_data(filepath):
    if not os.path.exists(filepath):
        return print("Вы ввели несуществующий путь к файлу. Введите правильный путь.")
    with open(jsonfile, 'r') as file_handler:
        return json.load(file_handler)
    
def pretty_print_json(raw_json):
    print(json.dumps(raw_json, ensure_ascii = False, indent=4, sort_keys=True))
    
if __name__ == '__main__':

    filepath = os.path.abspath(input("Введите путь к файлу с JSON: ").strip()) # например /projects/4_json/jsonfile.txt
    jsonfile = os.path.basename(filepath)
    raw_json = load_data(filepath)
    pretty_print_json(raw_json)
