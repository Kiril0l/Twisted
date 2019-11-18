actions=["+","-","*","/"]

class CalcException(Exception):
    pass


def check(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        arg1, arg2, action = result
        try:
            if "." in arg1:
                arg1 = float(arg1)
            else:
                arg1 = int(arg1)
        except ValueError:
            raise CalcException("error arg1")

        try:
            if "." in arg2:
                arg2 = float(arg2)
            else:
                arg2 = int(arg2)
        except ValueError:
            raise CalcException("error arg2")
        try:
            if action not in actions:
                print("action error")
        except ValueError:
            raise CalcException("error arg2")
        return arg1, arg2, action
    return wrapper


class Calc():

    def inpData(self, *args, **kwargs):
        self.arg1=input("print first nr >> ")
        self.arg2=input("print second nr >> ")
        self.action=input("specify action >> ")

    def check(self):
        try:
            if "." in self.arg1:
                self.arg1 = float(self.arg1)
            else:
                self.arg1 = int(self.arg1)
        except ValueError:
            raise CalcException("error arg1")

        try:
            if "." in self.arg2:
                self.arg2 = float(self.arg2)
            else:
                self.arg2 = int(self.arg2)
        except ValueError:
            raise CalcException("error arg2")
        try:
            if self.action not in actions:
                print("action error")
        except ValueError:
            raise CalcException("error arg2")
        except ZeroDivisionError:
            pass

    def outputData(self):
        if self.action == "+":
            print(self.arg1+self.arg2)
        if self.action == "-":
            print(self.arg1-self.arg2)
        if self.action == "*":
            print(self.arg1*self.arg2)
        if self.action == "/":
            print(self.arg1/self.arg2)


if __name__ == '__main__':
    calc = Calc()
    while True:
        calc.inpData()
        try:
            calc.check()
        except CalcException as e:
            print(e)
        else:
            calc.outputData()
        ansver = input("Для выхода введите 'Н' >>> ")
        if ansver == "Н":
            break
