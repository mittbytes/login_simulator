users = {
    "alice": "huh@3434",
    "john": "johnhume"
}

username = input("enter username : ")
password = input("enter password : ")

if username in users and users[username] == password:
    print("login successful!!")
else:
    print("login not successfull!!")
