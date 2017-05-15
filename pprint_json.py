import json
import os 

def load_data(input_filepath):
    if not os.path.exists(input_filepath):
        print("Вы ввели несуществующий путь к файлу. Введите правильный путь.")
    else:
        jsonfile = os.path.basename(input_filepath)
        with open(jsonfile, 'r') as file_handler:
            return json.load(file_handler)

def pretty_print_json(raw_json):
    return print(json.dumps(raw_json, ensure_ascii = False, indent=4, sort_keys=True))
    
if __name__ == '__main__':

    input_filepath = os.path.abspath(input("Введите путь к файлу с JSON: ").strip())
    raw_json = load_data(input_filepath)
    pretty_print_json(raw_json)