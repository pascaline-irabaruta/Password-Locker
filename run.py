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
