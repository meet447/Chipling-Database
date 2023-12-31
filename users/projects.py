import json
import os

def create_project(id, key, name, uid):
    project_folder = os.path.join("projects", id)

    if not os.path.exists(project_folder):
        os.makedirs(project_folder)

    project_file = os.path.join(project_folder, name + ".json")

    with open(project_file, "w") as file:
        print("created a new file")

    with open("json_files/projects.json", "a") as file:
        data = {
            "name": name,
            "key": key,
            "id": id,
            "uid":uid
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
            
def get_user_projects():
    with open("json_files/projects.json") as file:
        posts = []
        with open('projects.json', 'r') as file:
            for line in file:
                post = json.loads(line)
                posts.append(post)
        return posts
    
def search_projects(uid):
    with open("json_files/projects.json", "r") as file:
        posts = []
        for line in file:
            project = json.loads(line)
            if project.get("uid") == uid:
                posts.append(project)
    return posts

def get_project(id):
    with open("json_files/projects.json", "r") as file:
        posts = []
        for line in file:
            project = json.loads(line)
            if project.get("id") == id:
                posts.append(project)
    return posts