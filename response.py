from audio import Audio

class Response() :
    def __init__ (self, speech_text, state_variables=None, reprompt=None, should_save_speech_text=None):
        # state_variables is fine to be None
        if (reprompt is None):
            reprompt = Audio.FORMAT_STRING.format("19_Error.mp3")
        if (should_save_speech_text is None):
            should_save_speech_text = True
        
        self.speech_text = speech_text
        self.state_variables = state_variables
        self.reprompt = reprompt
        self.should_save_speech_text = should_save_speech_text
