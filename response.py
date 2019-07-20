
class Response() :
    def __init__ (self, speech_text, state_variables = {}, reprompt = "Repeat yourself"):
        self.speech_text = speech_text
        self.state_variables = state_variables
        self.reprompt = reprompt
