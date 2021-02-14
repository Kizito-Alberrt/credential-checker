import unittest
from user import User

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''
    def setUp(self):
        '''
        set up method thatruns before each test cases.
        '''
        self.new_user = User("kizito","kizito-albert","1234567")

    def test_init(self):
        '''
        test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.login_details,"kizito")
        self.assertEqual(self.new_user.login_username,"kizito-albert")
        self.assertEqual(self.new_user.login_password,"1234567") 
    
    def test_save_user(self):
        '''
        tests if the user object is saved to the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
 

    @classmethod
    def user_exist(cls,number):
        for user in cls.user_list:
            if user.login_username == username:
                return True

    
    def test_display_all_user(self):
        self.assertEqual(User.display_user(),User.user_list)
        
        return False
    if __name__ == '__main__':
        unittest.main()       