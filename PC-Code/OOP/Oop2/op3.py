#  Static Variables (Vs Instance Variables)
# Points to remember about static
    # Static attributes are created at class level.
    # Static attributes are accessed using ClassName.
    # Static attributes are object independent. We can access them without creating instance (object) of the class in which they are defined.
    # The value stored in static attribute is shared between all instances(objects) of the class in which the static attribute is defined.
class Atm:
    __user_id = 1

    def __init__(self):
        self.__pin = ''
        self.__balance = 0
        self.id = Atm.__user_id
        Atm.__user_id += 1

    # utility method
    @staticmethod
    def getId():
        return Atm.__user_id

    # utility method
    @staticmethod
    def setId(id):
        if isinstance(id, int):
            Atm.__user_id = id
        else:
            return "Id should be an integer"


c1=Atm()
c2=Atm()
c3=Atm()
c4=Atm()


