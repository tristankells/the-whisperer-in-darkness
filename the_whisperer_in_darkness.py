from response import Response
from test_translator import Translator

class TheWhispererInDarkness :
    whisper_repsonse = Response("Test","Test")

    def handle_launch(self) :
        self.whisper_repsonse = Translator.Launch
    
    
    def enter_door(door_number):
        return "You asked to go through door number " + door_number

    enter_door = staticmethod(enter_door)

        