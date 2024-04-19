#  Abstraction -> Hidden
from abc import ABC,abstractmethod

class BankApp(ABC):

    def database(self):
        print('connected to database')

    @abstractmethod
    def security(self):
        pass


class MobileApp(BankApp):

    def mobile_login(self):
        print('login into mobile')

    def security(self):
        print("mobile security")

# TypeError: Can't instantiate abstract class MobileApp with abstract method security
obj=MobileApp()
obj.security()