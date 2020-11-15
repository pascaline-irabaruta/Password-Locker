import getpass
import random, string
class Credentials:
    '''
    Class that generates added credentials
    '''
    credential_list = []
    def __init__(self,app_name , username, password):

        '''
        function that generate properties for our objects
        '''
        self.app_name = app_name
        self.username = username
        self.password = password
