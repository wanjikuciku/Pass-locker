import unittest
from credentials import Credential


class TestCredential(unittest.TestCase):
    """
    Test class that defines test cases for the credential class behaviours
    """

    def setUp(self):
        """
        set up method to run before each test cases
        """
        self.new_credential = Credential(
            "123456", "instagram", "milkshake", "12345")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        '''
        Credential.credential_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.view_password, "12345")
        self.assertEqual(self.new_credential.account, "instagram")
        self.assertEqual(self.new_credential.login, "milkshake")
        self.assertEqual(self.new_credential.password, "12345")

    def test_save_credential(self):
        """
        test_save_credential test case to test if the credential object is saves into
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if one can save multiple credentials
        '''
        self.new_credential.save_credential()
        test_credential = Credential("12345","test","login","67890")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    
    if __name__ == '__main__':
        unittest.main()
