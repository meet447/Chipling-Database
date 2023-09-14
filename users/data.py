import json
import uuid
import random

def create_user(name, id, key):
    with open("users_data.json", "a") as file:
        data = {
            "name":name,
            "id":id,
            "key":key
            }
        json.dump(data, file)
        file.write('\n')
        print("operation succesfull")

def retrieve_users():
    posts = []
    with open('users_data.json', 'r') as file:
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