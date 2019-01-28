import unittest  # Importing the unittest module
from user import User  # Importing the user class


class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours
    """

    def setUp(self):
        '''
        set up method to run before each test cases.
        '''
        self.new_user = User("lorna", "milkshake")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username, "lorna")
        self.assertEqual(self.new_user.password, "milkshake")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user oblect is saved into the users' list
        '''
        self.new_user.save_user()  # saving the new user
        self.assertEqual(len(User.user_list), 1)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean is we cannot find the user.
        '''
        self.new_user.save_user()
        test_user = User("User", "12345")
        test_user.save_user()
        user_exists = User.user_exists("12345")
        self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main()
