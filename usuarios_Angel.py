def create_user(name, email):
    print(f"Creating user: {name} with email: {email}")

def delete_user(user_id):
    print(f"Deleting user with ID: {user_id}")

def update_user(user_id, name=None, email=None):
    print(f"Updating user with ID: {user_id}")
    if name:
        print(f" - New name: {name}")
    if email:
        print(f" - New email: {email}")

def get_user(user_id):
    print(f"Retrieving user with ID: {user_id}")

def list_users():
    print("Listing all users") 
