users = []

def add_user(user_id, name):
    if user_id == "" or name == "":
        print("Error: Empty input not allowed")
        return

    users.append({"id": user_id, "name": name})
    print("User added successfully")

def view_users():
    if len(users) == 0:
        print("No users found")
        return

    for u in users:
        print(u)

def update_user(user_id, new_name):
    for u in users:
        if u["id"] == user_id:
            u["name"] = new_name
            print("User updated")
            return
    print("User not found")

def delete_user(user_id):
    for u in users:
        if u["id"] == user_id:
            users.remove(u)
            print("User deleted")
            return
    print("User not found")
