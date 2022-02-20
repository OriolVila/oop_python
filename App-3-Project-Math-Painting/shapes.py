class Square:
    """
    Define a square based on the starting point (x,y), side length and color. 
    It has a method to draw it in the canvas.
    """
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color
    
    def draw(self, canvas):
        #changes a slice of the array with new values
        canvas.data[self.x: (self.x + self.side), self.y: (self.y + self.side)]= self.color

class Rectangle:
    """
    Define a rectangle based on the starting point (x,y), side height, side width and color. 
    It has a method to draw it in the canvas.
    """
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
    
    def draw(self, canvas):
        #changes a slice of the array with new values
        canvas.data[self.x: (self.x + self.height), self.y: (self.y + self.width)]= self.color