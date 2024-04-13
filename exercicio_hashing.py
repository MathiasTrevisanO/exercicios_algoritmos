import hashlib

data_base = {}

def create_hash_password(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()

def storage_in_data_base(username, password):
    hash_password = create_hash_password(password)
    data_base[username] = hash_password
    return hash_password

def create_user():   
    username = input("User Name: ")
    password = input("Password: ")
    hash_password = storage_in_data_base(username, password)
    print(f"User {username} created with hash password: {hash_password}")

def login_user():
    username = input("User Name: ")
    password = input("Password: ")

    if username in data_base:
        hash_password_stored = data_base[username]
        hash_password_input = create_hash_password(password)

        if hash_password_stored == hash_password_input:
            print(f"Welcome {username}")
        else:
            print("Wrong password. Please try again")
    else:
        print("User not found. Please try again")

def main():
    while True:
        print("\n### Welcome ###")
        print("1. Sign up")
        print("2. Sign in")
        print("3. Exit")

        option = input("Choose an option: ")

        if option == "1":
            create_user()
        elif option == "2":
            login_user()
        elif option == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please try again")

if __name__ == "__main__":
    main()
