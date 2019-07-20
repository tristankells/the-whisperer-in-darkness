from response import Response
from test_translator import Translator

class TheWhispererInDarkness :
    whisper_repsonse = Response("Test","Test")

    def handle_launch(self) :
        self.whisper_repsonse = Translator.Launch
    
    @staticmethod
    def enter_door(door_number):
        """ returns a string to be said by Alexa after entering a door."""
        return "You asked to go through door number " + door_number

    @staticmethod
    def exposition(parameter_list):
        pass




        