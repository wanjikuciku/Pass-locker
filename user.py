class User:
    """
    Class that generates new instances of users
    """
    user_list = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)

    @classmethod
    def user_exists(cls, characters):
        '''
        Method that checks if a user exists from the user list.
        Args:
            character:username to search if it exists
        Returns:
            Boolean:true or false depending on the condition
        '''
        for user in cls.user_list:
            if user.password == characters:
                return True

        return False
