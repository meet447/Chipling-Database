from api.data.push import push_data

key = "123456"
id = "b740a79b2c7c"
name = "chippling-test"

data = {
    "name":"meet",
    "age":"44"
}

push_data(id=id, name=name, key=key, data=data)