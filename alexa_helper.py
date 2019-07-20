
from ask_sdk.standard import StandardSkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

class StateVariables:
    STATE_HISTORY_ENABLED = True # useful for debugging
    STATE_HISTORY = "STATE_HISTORY"

    @staticmethod
    def set_state(handler_input, key, value):
        # retireve Alexa state variables
        state_variables = handler_input.attributes_manager.persistent_attributes

        # make sure that the key is a string
        key = str(key)

        # store the value in the state variables
        state_variables[key] = value # note this overrides any previous value if it existed
        
        if (StateVariables.STATE_HISTORY_ENABLED):
            # get the state history
            state_histroy = state_variables[StateVariables.STATE_HISTORY]

            # create the history if it doesn't exist yet
            if (state_histroy is None):
                state_histroy = list()

            # add the state we just set
            state_histroy.append({ key, value, })

            # write history back to state variables list
            state_variables[StateVariables.STATE_HISTORY] = state_histroy

        # save the state variables
        handler_input.attributes_manager.session_attributes = state_variables

    @staticmethod
    def retrieve_non_null_state(handler_input, key):
        #read out our key, if it's None raise an error.
        value = StateVariables.retrieve_state(handler_input, key)
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