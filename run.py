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
