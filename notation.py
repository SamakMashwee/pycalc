def multiply(x, y):
    return x * y

def divide(x, y):
    return x/y

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

operations = {'*':multiply, '/':divide, '+':add, '-':subtract, '^':pow}

class data:
    def __init__(self, input):
        self.input = input
    
    def mkstring(self):
        self.input = self.input.join(self.input.split())
        