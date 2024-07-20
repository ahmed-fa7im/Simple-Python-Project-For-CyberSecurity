import hashlib
import getpass

password_manager = {}

def create_account():
    username = input("Enter you username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account created successfully!")


def login():
    username = input("Enter you username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login successfull")
    else:
        print("Invalid username or password.")


def main():
    while True:
        choise = input("Enter 1 to 'Create An Account', 2 to 'Login', 0 to 'Exit' ")
        match choise:
            case '0':
                break
            case '1':
                create_account()
            case '2':
                login()
            

if __name__ == "__main__":
    main()            