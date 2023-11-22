from flask import Flask, request


app = Flask(__name__)

users = [
    {"id": 1, "name": "Juan", "age": "22"},
    {"id": 2, "name": "Luis", "age": "24"},
]

## CRUD

@app.route("/users", methods=["GET"])
def userList():
    return users, 200


@app.route("/users/<int:id>", methods=["GET"])
def userById(id):
    for user in users:
        if user["id"] == id:
            return user, 200
    return {"message": f"User ID -> {id} not found"}, 404


@app.route("/users", methods=["POST"])
def userCreate():
    data = request.get_json()
    users.append(data)
    return {"message": "User created sucessfully", "data": users}, 201


@app.route("/users/<int:id>", methods=["PUT"])
def userUpdateById(id):
    data = request.get_json()
    for user in users:
        if user["id"] == id:
            user["name"] = data["name"]
            user["age"] = data["age"]
            return {"message": "User updated sucessfully", "data": users}
    return {"message": f"User ID -> {id} not found"}, 404


@app.route("/users/<int:id>", methods=["DELETE"])
def userDeleteById(id):
    for index, user in enumerate(users):
        if user["id"] == id:
            users.pop(index)
            return {"message": "User deleted sucessfully", "data": users}, 200
    return {"message": f"User ID -> {id} not found"}, 404
