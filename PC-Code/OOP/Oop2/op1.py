# Encapsulation

# # Instance var -> name , country
class Person:

    def __init__(self,name,country):
        self.name = name
        self.country = country

p1=Person('Ranjeet','India')
p2=Person('Abdul','Pakistan')
print(p1.name)
print(p2.name)

class Atm:

    # constructor(special function)->superpower -> 
    def __init__(self):
        print(id(self))
        self.pin = ''
        self.__balance = 0
        #self.menu()

    def get_balance(self):
        return self.__balance

    def set_balance(self,new_value):
        if type(new_value) == int:
            self.__balance = new_value
        else:
            print('beta bahot maarenge')

    def __menu(self):
        user_input = input("""
        Hi how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit
        """)

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input('enter your pin')
        self.pin = user_pin

        user_balance = int(input('enter balance'))
        self.__balance = user_balance

        print('pin created successfully')

    def change_pin(self):
        old_pin = input('enter old pin')

        if old_pin == self.pin:
        # let him change the pin
            new_pin = input('enter new pin')
            self.pin = new_pin
            print('pin change successful')
        else:
            print('nai karne de sakta re baba')

    def check_balance(self):
        user_pin = input('enter your pin')
        if user_pin == self.pin:
            print('your balance is ',self.__balance)
        else:
            print('chal nikal yahan se')

    def withdraw(self):
        user_pin = input('enter the pin')
        if user_pin == self.pin:
            # allow to withdraw
            amount = int(input('enter the amount'))
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print('withdrawl successful.balance is',self.__balance)
            else:
                print('abe garib')
        else:
            print('sale chor')