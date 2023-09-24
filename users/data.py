import json
import uuid
import random

def create_user(username, uid, key, id):
    with open("json_files/users_data.json", "a") as file:
        data = {
            "username":username,
            "id":id,
            "key":key,
            "uid":uid
            }
        json.dump(data, file)
        file.write('\n')
        print("operation succesfull")

def retrieve_users():
    posts = []
    with open('json_files/users_data.json', 'r') as file:
        for line in file:
            post = json.loads(line)
            posts.append(post)
    return posts

def search_users(id):
    users = retrieve_users()
    if id == users[0]["id"]:
        data = [{
          "name":users[0]["name"],
          "id":users[0]["id"]  
        }]
        return data