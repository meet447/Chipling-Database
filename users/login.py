import json

def create_useracc(name, id):
    with open("login.json", "a") as file:
        data = {
            "username":name,
            "password":id
            }
        json.dump(data, file)
        file.write('\n')
        print("operation succesfull")
        
def retrive_useracc():
    posts = []
    with open('login.json', 'r') as file:
        for line in file:
            post = json.loads(line)
            posts.append(post)
    return posts
