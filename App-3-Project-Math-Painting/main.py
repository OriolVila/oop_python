from PIL import Image
import numpy as np


#python -m pip install numpy

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
        canvas.data[self.x: (self.x + self.width), self.y: (self.y + self.height)]= self.color


class Canvas:
    """
    Create a black or white canvas to draw. 
    It has a method that saves the final canvas as image
    """
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        #Create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        #Change [0, 0, 0] with user given values for color 
        self.data[:] = self.color

    def make(self, imagepath):
        """Converts the current array into an image file"""
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)

canvas = Canvas(height=20, width=30, color=(255,255, 255))

r1 = Rectangle(x=1, y=6, height=7, width=10, color=(100,200,125))
r1.draw(canvas)

s1 = Square(x=1, y=3, side=3, color=(0,100,222))
s1.draw(canvas)

canvas.make('canvas.png')