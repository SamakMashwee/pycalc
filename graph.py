import json
from math import sin

def function(x):
    return sin(x)

def derive(x):
    return 

def close_to(x, y, deviation):
    return abs(x-y)<deviation

def snap_val(y, pos, range):
    steps = range/8
    goal = y-(pos-(range/2))
    counter = 0
    step = 0
    while step < goal:
        step += steps
        counter+=1
    return counter-1

class pixel():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    display = ''
    def shade(self):
        self.display = '#'
    
class ascii_display():
    def __init__(self, params):
        self.height = params["height"]
        self.width = params["width"]
        self.xmin = params["xmin"]
        self.xmax = params["xmax"]
        self.ymin = params["ymin"]
        self.ymax = params["ymax"]
        self.xsteps = (abs(self.xmax - self.xmin))/self.width
        self.ysteps = (abs(self.ymax - self.ymin))/self.height
    
    screen = []
    def construct_display(self):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(pixel(self.xmin + (self.xsteps * j), self.ymax - (self.ysteps * i)))
            self.screen.append(row)
    
    def draw_graph(self):
        for i in range(self.height):
            for j in range(self.width):
                if close_to(self.screen[i][j].x, 0, self.xsteps/2) and close_to(self.screen[i][j].y, 0, self.ysteps/2):
                    self.screen[i][j].display = '+'
                elif close_to(self.screen[i][j].x, 0, self.xsteps/2):
                    self.screen[i][j].display = '|'
                elif close_to(self.screen[i][j].y, 0, self.ysteps/2):
                    self.screen[i][j].display = '-'
                else:
                    self.screen[i][j].display = ' '
                
                if close_to(self.screen[i][j].y, function(self.screen[i][j].x), self.ysteps/2):
                    table = "_,.-~*'`"
                    self.screen[i][j].display = table[int(snap_val(function(self.screen[i][j].x), self.screen[i][j].y, self.ysteps))]

    def show_display(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.screen[i][j].display, end='')
            print()

display_properties = json.load(open("properties.json"))

disp = ascii_display(display_properties)
disp.construct_display()
disp.draw_graph()
disp.show_display()