class Atm:
    # Constructor (special function) -> Superpower -> we don't need to call exiplity 
    def __init__(self):
        self.pin="7287"
        self.balance=0
        # print("mai tho execute ho gaya")
        self.menu()
    
    def menu(self):
        user_input = input("""
                Hello How can I help you ?
                    1.Press 1 to create pin
                    2.Press 2 to change pin
                    3.Press 3 to check balance 
                    4.Press 4 to withdraw money
                    5.Anything else to exit
            """)

        if user_input=='1':
            # create pin
            self.create_pin()
        elif user_input == '2':
            # change pin
            self.change_pin()
        elif user_input == '3':
            # check balance
            self.check_balance()
        elif user_input == '4':
            # withdraw money
            self.withdraw()
        else :
            # anything else
            exit()

    def create_pin(self):
        new_pin = input("Enter new Pin")
        self.pin = new_pin

        user_balance = int(input('enter balance'))
        self.balance = user_balance

        print("Pin Created Successfully 😉")
        self.menu()
        
    def change_pin(self):
        current_pin = input("Enter current pin :")
        if (self.pin == current_pin):
            new_pin = input("Enter new pin : ")
            self.pin = new_pin
            print("New pin created successfully 👍")
            self.menu()

        else:
            print("Enter correct pin")
            self.menu()

    def check_balance(self):
        pin=input("Enter Pin :")
        if(pin==self.pin):
            print("your balance is ",self.balance)
            self.menu()
        else:
            print("Please Enter Correct Pin")
            self.menu()
    
    def withdraw(self):
        pin=input("Enter Pin :")
        if(pin==self.pin):
            amount= int(input("Enter Amount : "))
            if(amount <= self.balance):
                self.balance=self.balance-amount
                print("Yeh Lo apne pisa", amount)
            else:
                print("abey garib")
        else:
            print("Slaeey chor")
        self.menu()

obj1 = Atm()
# print(obj1) 