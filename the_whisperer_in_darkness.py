from response import Response
from test_translator import Translator

class TheWhispererInDarkness :
    whisper_repsonse = Response("Test","Test")

    def handle_launch(self) :
        self.whisper_repsonse = Translator.Launch