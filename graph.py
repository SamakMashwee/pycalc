import json

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
                if self.screen[i][j].x == 0 and self.screen[i][j].y == 0:
                    self.screen[i][j].display = '+'
                elif self.screen[i][j].x == 0:
                    self.screen[i][j].display = '|'
                elif self.screen[i][j].y == 0:
                    self.screen[i][j].display = '-'
                else:
                    self.screen[i][j].display = ' '

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