import operator
import re
import enum

class token_type(enum.Enum):
    T_NUM = 0
    T_ADD = 1
    T_SUB = 2
    T_MUL = 3
    T_DIV = 4
    T_POW = 5
    T_LPAR = 6
    T_RPAR = 7
    T_END = 8

operations = { '*' : operator.mul, '/' : operator.truediv, '+' : operator.add, '-' : operator.sub, '^' : pow }
token_map = { '*' : token_type.T_MUL, '/' : token_type.T_DIV, '+' : token_type.T_ADD, '-' : token_type.T_SUB, '^' : token_type.T_POW }

class node:
    def __init__(self, type, data=None):
        self.type = type
        self.data = data
        self.children = []

class data:
    def __init__(self, input):
        self.input = input
    
    def tokenize(self):
        self.strtkns = []
        for counter in range(len(self.input)):
            if self.input[counter].isdigit():
                tmpstr = ""
                while self.input[counter].isdigit():
                    tmpstr += self.input[counter]
                    counter+=1
                self.strtkns.append(tmpstr)
            
            else:
                self.strtkns.append(self.input[counter])

    def construct_ast(self):
        self.tokens = []
        for c in self.input:
            if c in token_map:
                token = node(token_map[c], data=c)
            elif re.match(r'\d', c):
                token = node(token_type.T_NUM, data=int(c))
            else:
                raise Exception(f"Error Invalid Token: {token}")
            self.tokens.append(token)
        self.tokens.append(node(token_type.T_END))
        
        