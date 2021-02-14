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
   
   
    @classmethod
    def display_user(cls):
        return cls.user_list