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
    def save_credentials(self):
        '''
        function that saves a credential
        it appends a new credential to the credential_list
        '''
        Credentials.credential_list.append(self)
    def delete_credential(self):
        '''
        funtion that deletes a credential
        '''
        Credentials.credential_list.remove(self)
