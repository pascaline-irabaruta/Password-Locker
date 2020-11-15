class User():
    '''
    A class that prompts user to signup and login to generate passwords
    '''
    user_list = []
    def __init__(self,f_name,l_name,u_name,psswd):
        '''
        a function to define user proprties
        '''
        self.f_name = f_name
        self.l_name = l_name
        self.u_name = u_name
        self.psswd = psswd
