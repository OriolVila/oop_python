from PIL import Image
import numpy as np

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
