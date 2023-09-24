import json
from users.projects import get_project

def push_data(id, name, key, data):
    file_path = f"projects/{id}/{name}.json"
    print(file_path)
    sys_key = get_project(id=id)
    
    if key == sys_key[0]["key"]:
        print(key)
        with open(file_path, 'w') as file:
            json.dump(data, file)
            file.write('\n')
        print("Operation successful")
    else:
        print("Operation unsuccessful")