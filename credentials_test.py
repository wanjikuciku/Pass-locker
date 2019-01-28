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
