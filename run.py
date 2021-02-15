from user import User


def create_user(details,username,password):
        '''
        function to create new user
        '''
        new_user = User(details,username,password)
        return new_user

def save_user(user):
    '''
    function to save user
    '''
    user.save_user()


def del_user(user):
    '''
    function to delete a user
    '''
    user.delete_user()


def find_user(username):
    '''
    function that find a user by username and returns the details
    '''
    return User.find_by_username(username)


def check_existing_user(username):
    '''
    function that check if a user exists with that username and return a boolean
    '''
    return User.user_exists(username)


def display_user(password):
    '''
    function that returns all the saves passwords
    '''
    return User.display_user(password)

def main():
    print("welcome. Write your username")
    user_name = input()

    print("{user_name}. welcome")
    print('\n')

    while True:
        print("Use these short codes  cd - create new details, dd - display detail, fd - find details, ex - exit the detail list ")

        short_code = input().lower()

        if short_code == 'cd':
            print("New details")
            print("-"*10)

            print ("login details..")
            l_details = input()

            print ("login username..")
            l_username = input()

            print ("login password..")
            l_password = input()


            save_user(create_user(l_details,l_username,l_password))

            print ('\n')
            print("New User {l_details} {l_username} {l_password} created")
            print ('\n')


        elif short_code == 'dd':
            if display_user():
                print("Your details are as follows")
                print ('\n')

                for user in display_user():
                    print("{user.login_details} {user.login_username}...{user.login_password}")
                    print('\n')

            else: 

                print('\n')
                print("You dont have a valid user")
                print('\n')

        
        elif short_code == 'fd':
            print("Enter a username")

            search_username = input()
            if check_existing_user(search_username):
                search_user = find_user(search_username)

                print("{search_user.login_details}")

                print('-' * 20)

                print("login username...{search_user.login_username}")

                print("login password...{search_user.login_password}")


            else:
                print("Details does not exist")


        elif short_code == "ex":
            print("Thank you....")
            break
        else:

            print("Kindly use the short codes")


if __name__ == '__main__':

    main()