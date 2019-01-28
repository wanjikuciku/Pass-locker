from user import User


def create_user(username, password):
    '''
    Function to create a new user
    '''
    new_user = User(username, password)
    return new_user


def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()
