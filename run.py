import getpass
from credentials import Credentials
from user import User
import pyperclip
import string
import random
from pyfiglet import Figlet

def create_user(f_name,l_name,u_name,psswd):
    '''
    A funtcion to create a new user.
    '''
    new_user = User(f_name, l_name,u_name, psswd)
    return new_user
def save_user(User):
    '''
    function to save user
    '''
    User.save_user()
def del_user(User):
    '''
    function to delete a specific user
    '''
    User.delete_user()
def create_credential(app_name,username, password):
    '''
    function to create a new credential
    '''
    new_credential = Credentials(app_name,username,password)
    return new_credential
def save_credentials(Credentials):
    '''
    function to save credentials
    '''
    Credentials.save_credentials()
def delete_credential(Credentials):
    '''
    a function to delete credential
    '''
    Credentials.delete_credential()
def check_existing_credentials(app_name):
    '''
    functions that checks if a credential exist
    '''
    return Credentials.find_by_app_name(app_name)
def find_credential(app_name):
    '''
    Function that finds a contact by username and return the credential
    '''
    return Credentials.find_by_app_name(app_name)
def display_credentials():
    '''
    function that displays all the credentials
    '''
    return Credentials.display_credentials()

def passGen(size = 8, char=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    gen = ''.join(random.choice(char) for _ in range(size))
    return gen

def check_if_userExist(u_name, psswd):
    return User.check_if_userExist(u_name, psswd)

def main():
    print("Hello, welcome to Password Locker. Please tell us your name")
    user_name = input()
    print('\n')
    print(f"Hello {user_name},Please create your Password-Locker account:")
    print("Your full information:")
    print("-"*20)
    print("Enter your first name .....")
    f_name = input()
    print("Enter your last name .....")
    l_name = input()
    print("Enter your prefered username .....")
    u_name = input()
    print("Enter Password .....")
    psswd = getpass.getpass()
    print("Confirm password .....")
    c_psswd = getpass.getpass()
    if c_psswd == psswd :
        print("ACCOUNT SUCCESSFULLY CREATED!")
        save_user(create_user(f_name,l_name,u_name,psswd))
    else:
     #    A loop to test until confirm password is same as password inputed
        while c_psswd != psswd:
            print('\n')
            print("please confirm your password!")
            print("Confirm password .....")
            c_psswd = getpass.getpass()
        print("ACCOUNT SUCCESSFULLY CREATED!")
        save_user(create_user(f_name,l_name,u_name,psswd))
    print('\n')
    print("Please Log in using your username")
    print("Username .....")
    u_name = input()
    print("Password .....")
    psswd = input()
    account_exist = check_if_userExist(u_name, psswd)
    while account_exist != u_name:
        print('\n')
        print("invalid username or password")
        print("Please Log in using your username")
        print("Username .....")
        u_name = input()
        print("Password .....")
        psswd = input()
        account_exist = check_if_userExist(u_name, psswd)
    if account_exist == u_name:
        print(f"Dear {u_name}, You're successfully Logged in!")
