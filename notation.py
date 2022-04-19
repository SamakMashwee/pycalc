import operator
import re

operations = { '*' : operator.mul, '/' : operator.truediv, '+' : operator.add, '-' : operator.sub, '^' : pow }
class data:
    def __init__(self, input):
        self.input = input
    
    def tokenize(self):
        self.tokens = []
        for counter in range(len(self.input)):
            if self.input[counter].isdigit():
                tmpstr = ""
                while self.input[counter].isdigit():
                    tmpstr += self.input[counter]
                    counter+=1
                self.tokens.append(tmpstr)
            
            else:
                self.tokens.append(self.input[counter])

    def mkstring(self):
        self.input = self.input.join(self.input.split())

        self.tokenize()
        for token in self.tokens:
            