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
    @classmethod
    def find_by_app_name(cls,app_name):
        '''
        function that takes an application name and return credential that matches it
        helps user to search for a specific credential
        '''
        for credential in cls.credential_list:
            '''
            a for loop to loop through the list and return the credential that matches the app name
            '''
            if credential.app_name == app_name:
                return credential
        # for user in User.user_list:
        #     '''
        #     a for loop to loop through the list and check if the credential exists
        #     '''
        #     if user.app_name == app_name:
        #         present_user = user.app_name
        #         return present_user
        # return "credential does not exist"
