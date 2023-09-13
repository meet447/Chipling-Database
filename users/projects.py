import json
import os

def create_project(id, key, name):
    project_folder = os.path.join("projects", id)

    if not os.path.exists(project_folder):
        os.makedirs(project_folder)

    project_file = os.path.join(project_folder, name + ".json")

    with open(project_file, "w") as file:
        print("created a new file")

    with open("projects.json", "a") as file:
        data = {
            "name": name,
            "key": key,
            "id": id
        }
        json.dump(data, file)
        file.write('\n')

    print("Created a new project")
    
def retrive_project(id, name, key):
    file = f"projects/{id}/{name}.json"
    with open(file) as file:
        data = []
        for line in file:
            post = json.loads(line)
            data.append(post)
    return data
            