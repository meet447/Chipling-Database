from users.projects import retrive_project 
import json

def pull_project(key, name, id):
    project = retrive_project(key=key, name=name, id=id)
    return project

def push_proroject(key, id, data):
    if key  == get_key():
        with open(f"projects/{id}/json") as file:
            json.dump(data, file)
            file.write('\n')
            print("operation succesfull")
    
def get_key(key, id):
    return 0