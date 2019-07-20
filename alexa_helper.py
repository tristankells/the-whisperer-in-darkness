
from ask_sdk.standard import StandardSkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

class StateVariables:
    @staticmethod
    def set_state(handler_input, key, value):
        # retireve Alexa state variables
        state_variables = handler_input.attributes_manager.persistent_attributes

        # store the value in the state variables and save to Alexa session
        state_variables[str(key)] = value
        handler_input.attributes_manager.session_attributes = state_variables

    @staticmethod
    def retrieve_non_null_state(handler_input, key):
        #read out our key, if it's None raise an error.
        value = StateVariables.retrieve_key(handler_input, key)
        if (value is None):
            raise Exception("reading out variable '" + str(key) + "' returned None.") #TODO proper exception type
        else:
            return value

    @staticmethod
    def retrieve_state(handler_input, key):
        # retireve Alexa state variables
        state_variables = handler_input.attributes_manager.persistent_attributes       
        #return the value at our key (or None if it doesn't exist)
        return state_variables[str(key)]