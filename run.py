from user import User


def create_user_account(username, password):
    '''
    Function to create a new user account
    '''
    new_user = User(username, password)
    return new_user


def save_user_account(user):
    '''
    Function to save user account
    '''
    user.save_user()


def check_existing_users(characters):
    '''
    Function that checks if a User exists with those characters and return Boolean
    '''
    return User.user_exist(characters)


def main():
    print("Hello Welcome to your Pass-locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}.")
    print('\n')
    while true:
            print("\nUse these short codes below:")
            print
