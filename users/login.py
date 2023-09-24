import json

def create_useracc(name, id,uid):
    with open("login.json", "a") as file:
        data = {
            "username":name,
            "password":id,
            "uid":uid
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

def search_login(uid):
    users = retrive_useracc()
    if id == users[0]["id"]:
        data = [{
          "username":users[0]["username"],
          "password":users[0]["password"],
          "uid":users[0]["uid"]  
        }]
        return data
    
def get_uid(username):
    users = retrive_useracc()
    uid = users[0]["uid"] 
    return uid
    