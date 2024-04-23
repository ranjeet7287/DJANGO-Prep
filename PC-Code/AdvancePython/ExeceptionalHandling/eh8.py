
class SecurityError(Exception):

    def __init__(self,message):
        print(message)

    def logout(self):
        print('logout')

class Google:
    
    def __init__(self,name,email,password,device):
        self.name=name
        self.email=email
        self.password=password
        self.device=device
    
    def login(self,email,password,device):
        if device!=self.device:
            raise SecurityError('bhai teri to lag gyi')
        if email==self.email and password==self.password:
            print('welcome')
        else:
            print('login error')

obj=Google('Ranjeet','sranjepjoij@hmail.vom','1234','poco')

try:
    obj.login('sranjepjoij@hmail.vom','1234','poco')
except SecurityError as e:
    e.logout()
else:
    print(obj.name)
finally:
    print('database connection closed')

