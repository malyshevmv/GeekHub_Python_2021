"""
1. Створити клас Calc, який буде мати атребут last_result та 4 методи.
Методи повинні виконувати математичні операції з 2-ма числами, а саме додавання, віднімання, множення, ділення.
   - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
   - Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.
   - Додати документування в клас (можете почитати цю статтю: https://realpython.com/documenting-python-code/ )

"""


class Calc(object):
    """
    A class in which methods perform mathematical operations

    Attributes
    ----------
    last_result : None
        returns the result of the class method

    Methods
    -------
    adding : Calc class object
        Performs the addition of two objects of the class
    subtraction : Calc class object
        Performs subtraction of two objects of a class
    multiplication : Calc class object
        Multiplies two class objects
    division : Calc class object
        Divides two class objects
    """

    last_result = None

    def __init__(self, value):
        """
        Parameters
        ----------
        value : int
            parameter value takes ONLY integer
        """
        self.value = value

    def __str__(self):
        return str(self.value)

    def adding(self, other):
        """
        Performs the addition of two objects of the class

        Parameters
        ----------
        self : the first object of the Calc class
        other : the second object of class Calc
        """
        Calc.last_result = self.value + other.value
        return Calc.last_result

    def subtraction(self, other):
        """
        Performs subtraction of two objects of a class

        Parameters
        ----------
        self : the first object of the Calc class
        other : the second object of class Calc
        """
        Calc.last_result = self.value - other.value
        return Calc.last_result

    def multiplication(self, other):
        """
        Multiplies two class objects

        Parameters
        ----------
        self : the first object of the Calc class
        other : the second object of class Calc
        """
        Calc.last_result = self.value * other.value
        return Calc.last_result

    def division(self, other):
        """
        Divides two class objects

        If the second object of class is 0, it returns a message stating that the division cannot be performed

        Parameters
        ----------
        self : the first object of the Calc class
        other : the second object of class Calc
        """
        try:
            Calc.last_result = self.value / other.value
            return Calc.last_result
        except ZeroDivisionError as err:
            Calc.last_result = err
            return Calc.last_result


a = Calc(4)
b = Calc(6)
c = Calc(8)
d = Calc(4)
print(a)
print(b)
print(c)
print(d)
print('last_result', Calc.last_result)
print('adding', Calc.adding(a, b))
print('last_result', Calc.last_result)
print('subtraction', Calc.subtraction(a, b))
print('last_result', Calc.last_result)
print('multiplication', Calc.multiplication(b, c))
print('last_result', Calc.last_result)
print('division', Calc.division(c, d))
print('last_result', Calc.last_result)
