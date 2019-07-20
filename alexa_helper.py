
from ask_sdk.standard import StandardSkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response
from collections import defaultdict

class StateVariables:
    STATE_HISTORY_ENABLED = True # useful for debugging
    STATE_HISTORY = "STATE_HISTORY"

    @staticmethod
    def set_state(handler_input, key, value):
        # retireve Alexa state variables
        state_variables = handler_input.attributes_manager.persistent_attributes

        print(type(state_variables))

        # make sure that the key is a string
        key = str(key)

        # store the value in the state variables
        state_variables[key] = value # note this overrides any previous value if it existed
        
        if (StateVariables.STATE_HISTORY_ENABLED):
            # get the state history
            try:
                state_histroy = state_variables[StateVariables.STATE_HISTORY]
            except KeyError:
                state_histroy = list()

            # add the state we just set
            state_histroy.append({ key, value, })

            # write history back to state variables list
            state_variables[StateVariables.STATE_HISTORY] = state_histroy

        # save the state variables
        handler_input.attributes_manager.session_attributes = state_variables

    @staticmethod
    def get_state(handler_input, keys):
        """
        get_state(key) -> str
        get_state(keys) -> defaultdict
        """
        # retireve Alexa state variables
        state_variables = handler_input.attributes_manager.persistent_attributes       

        # if keys is just a single key (doesn't implement __iter__) use it as the key
        # else loop over each element in the list of keys
        if not hasattr(keys, "__iter__"):
            keys = str(keys)
           return state_variables
        else:            
            # create a dictionary to return
            values = defaultdict()
            for key in map(str, keys):
                try:
                    values[key] = state_variables[key]
                except KeyError:
                    values[key] = None
            return values
        