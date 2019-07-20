from response import Response
from audio import Audio

class Translator() :
    """
    Test translator for the whisperer in darkness. Contains shorter, more
    debug focussed test phrases
    """
    Launch = Response(
        Audio.Splat + " Welcome to the whisperer in darkness"
        ,"Launch Reprompt"
        )

        