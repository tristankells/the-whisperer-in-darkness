
from ask_sdk.standard import StandardSkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response
from collections import defaultdict

class AlexaHelper:
    @staticmethod
    def createAdder(handler_input):
        return lambda y: handler_input.something.you

    #obsolete
    @staticmethod
    def save_state_callback(handler_input, state):
        handler_input.attributes_manager.session_attributes = state
        return True

    #obsolete
    @staticmethod
    def get_save_state_callback(handler_input):
        return lambda state: AlexaHelper.save_state_callback(handler_input, state)

    @staticmethod
    def build_response(handler_input, response, should_save_speech_text = True):
        state_variables = response.state_variables
        speech_text = response.speech_text
        reprompt = response.reprompt

        # save speech_text for next time
        if (should_save_speech_text):
            state_variables["PreviousSpeechText"] = speech_text
            state_variables["PreviousReprompt"] = reprompt

        # save state variables
        handler_input.attributes_manager.session_attributes = state_variables

        # build alexa response
        handler_input.response_builder.speak(speech_text).ask(reprompt)

        # return the handler method with the new attributes and response builder
        return handler_input

    #obsolete
    @staticmethod
    def get_state(handler_input, key):
        key = str(key)
        try:
            return handler_input.attributes_manager.persistent_attributes[key]               
        except KeyError:
            return None

    @staticmethod
    def get_state_helper(session_variables_delegate):
        return StateHelper(session_variables_delegate)

class StateHelper:
    def __init__(self, session_variables_delegate):
        self.session_variables_delegate = session_variables_delegate

    def get_state(self, key):
        session_variables = self.session_variables_delegate()
        key = str(key)
        try:
            return session_variables[key]               
        except KeyError:
            return None

#obsolete
class StateVariables:
    # STATE_HISTORY_ENABLED = True # useful for debugging
    # STATE_HISTORY = "STATE_HISTORY"

    #obsolete
    @staticmethod
    def set_state(handler_input, key, value):
        # retireve Alexa state variables
        state_variables = handler_input.attributes_manager.persistent_attributes

        print(type(state_variables))

        # make sure that the key is a string
        key = str(key)

        # store the value in the state variables
        state_variables[key] = value # note this overrides any previous value if it existed
        
        # if (StateVariables.STATE_HISTORY_ENABLED):
        #     # get the state history
        #     try:
        #         state_histroy = state_variables[StateVariables.STATE_HISTORY]
        #     except KeyError:
        #         state_histroy = list()

        #     # add the state we just set
        #     state_histroy.append({ key, value, })

        #     # write history back to state variables list
        #     state_variables[StateVariables.STATE_HISTORY] = state_histroy

        # save the state variables
        handler_input.attributes_manager.session_attributes = state_variables
    
    #obsolete
    @staticmethod
    def set_state_v2(state_variables, save_state_callback, key, value):

        # make sure that the key is a string
        key = str(key)

        # store the value in the state variables
        state_variables[key] = value # note this overrides any previous value if it existed
        
        # save the state variables
        save_state_callback(state_variables)

    #obsolete
    @staticmethod
    def get_state(handler_input, key):
        """
        get_state(handler_input, key) -> str
        get_state(handler_input, key) -> defaultdict #if key defines __iter__
        """
        state_variables = handler_input.attributes_manager.persistent_attributes

        # if keys is just a single key (doesn't implement __iter__) use it as the key
        # else loop over each element in the list of keys
        if not hasattr(key, "__iter__"):
            key = str(key)
            try:
                return state_variables[key]               
            except KeyError:
                return None
        else:            
            # create a dictionary to return
            values = defaultdict()
            for key in map(str, key):
                try:
                    values[key] = state_variables[key]
                except KeyError:
                    values[key] = None
            return values
        

class Slots:
    @staticmethod
    def get_slot(handler_input, key):
        """
        get_slot(handler_input, key) -> str
        """
        # TODO make this use slots not persistent_attributes

        state_variables = handler_input.attributes_manager.persistent_attributes
        
        key = str(key)
        try:
            return state_variables[key]               
        except KeyError:
            return None