import pyperclip
class User:
    '''
    class that generates new instances for users
    '''
    
    user_credentials = []

    

    def __init__(self,login_details,login_username,login_password):

        '''
        Args:
            login_details: User login details.
            login_username: User login username.
            login_password: User login password.

        '''

        self.login_details = login_details
        self.login_username = login_username
        self.login_password = login_password
   
   
    def test_copy_email(self):
        '''
        copy password from a found username
        '''
        self.new_user.save_user()
        User.copy_password("1234567")

        self.assertEqual(self.new_user.password,pyperclip.paste())


   