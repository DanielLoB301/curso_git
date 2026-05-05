def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "password":
        print("Login successful")
        return True
    else:
        print("Login failed")
        return False

if __name__ == "__main__":
    login()