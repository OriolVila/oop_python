from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import requests
import wikipedia

# python -m pip install kivy

# As an introduction to the Kivy library
Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    def get_image_link(self):
        # Get user query from test input
        query = self.manager.current_screen.ids.user_query.text
        #Get wikipedia page and the first image link
        page = wikipedia.page(query)
        image_link = page.images[0]
        print('1')
        return image_link

    def download_image(self):  
        # Download the image
        req = requests.get(self.get_image_link())
        imagepath = 'files/image.jpg'
        print('2')
        with open(imagepath, 'wb') as file:
            file.write(req.content)
        # Set the image in the Image widget
        return imagepath
        print('3')
    def set_image(self):
        # Set the image in the Image widget
            self.manager.current_screen.ids.img.source = self.download_image()

class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()

#req.content error. Servers are under maintenance