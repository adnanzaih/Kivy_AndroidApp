import time

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
kivy.require('1.9.0')

class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot,self).__init__()

    def generate_number(self):
        self.random_label.text = "Adnan"

class NeuralRandom(App):

    def build(self):
        """
        Going to return App UI
        Return: Label
        """
        return MyRoot()


neuralRandom = NeuralRandom()
neuralRandom.run()