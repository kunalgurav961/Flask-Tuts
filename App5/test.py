import json

# data = json.load('data.json')
# print(data)

# f = open("data.json", 'r')
# data = json.load(f)

# for d in data:
#     print(f"Name: {d.get('name')}")

data = []
with open('data.json', 'r') as f:
    data = json.load(f)
    
user = {
    "name": "Vaishnavi",
    "email":"vaishnavi1234@gmail.com",
    "nickname": "Mau"
}
# print(data)
is_present = False
for doc in data:
    if doc.get("email") == user.get('email'):
        is_present = True
if not is_present:
    data.append(user)
    with open('data.json', 'w') as f:
        json.dump(data, f)
    print("user created!")
else:
    print("User already exists!")