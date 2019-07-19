class Response () :
    """
    Contains the all info for the game response including speech text and
    reprompt text
    """
    def __init__ (self, speech_text, reprompt ) :
        self.SpeechText = speech_text
        self.Reprompt = reprompt