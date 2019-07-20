# -*- coding: utf-8 -*-

# This is a 
# The skill serves as a simple sample on how to use the
# persistence attributes and persistence adapter features in the SDK.
import random
import logging

from ask_sdk.standard import StandardSkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response
from the_whisperer_in_darkness import TheWhispererInDarkness
from the_whisperer_in_darkness import OctopusRoom
from slot_types import Door
from alexa_helper import StateVariables
from alexa_helper import AlexaHelper
from audio import Audio

SKILL_NAME = 'The Whisperer in Darkness'
sb = StandardSkillBuilder(table_name="The-Whisperer-In-Darkness", auto_create_table=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    """
    Handler for Skill Launch.
    """
    # type: (HandlerInput) -> Response
    state_variables = handler_input.attributes_manager.persistent_attributes
    if not state_variables:
        state_variables['playing'] = True

    handler_input.attributes_manager.session_attributes = state_variables

    speech_text = TheWhispererInDarkness.handle_launch()

    reprompt = "Repeat yourself"

    handler_input.response_builder.speak(speech_text).ask(reprompt)

    return handler_input.response_builder.response

# Custom Intents Begin 

# region

@sb.request_handler(can_handle_func = lambda input:
                    is_intent_name("EnterDoorIntent")(input))
def enter_door_handler(handler_input):
    """
    Handler for processing the enter door command
    """
    # type: (HandlerInput) -> Response

    # the value of DoorNumber slot passed alongside the intent

   
    try :
        door = str(handler_input.request_envelope.request.intent.slots["DoorNumber"].value)
    except:
        door = None     

    if(door == None) :
        door = Door[str(handler_input.request_envelope.request.intent.slots["DoorOrder"].value)]


    StateVariables.set_state(handler_input, "door", door)

    speech_text = TheWhispererInDarkness.enter_door(door)   

    reprompt = "Repeat yourself"

    handler_input.response_builder.speak(speech_text).ask(reprompt)

    return handler_input.response_builder.response

@sb.request_handler(can_handle_func = is_intent_name("AffirmativeLeftDoorIntent"))
def affirmative_left_door_handler(handler_input):
    pass
    #TODO do things

@sb.request_handler(can_handle_func = is_intent_name("AffirmativeIntent"))
def affirmative_handler(handler_input):
    """
    Handler for processing AffirmativeIntent, calls other intents based on context
    """
    state_variables = handler_input.attributes_manager.persistent_attributes 

    if (state_variables["Affirmative_LeftDoor"]):
        return affirmative_left_door_handler(handler_input)
    
    #TODO error message

@sb.request_handler(can_handle_func = lambda input:
                    is_intent_name("OctopusIntent")(input))
def octopus_handler(handler_input):
    """
    Handler for processing OctopusIntent
    """
    save_state_callback = AlexaHelper.get_save_state_callback(handler_input)
    
    state_variables = handler_input.attributes_manager.persistent_attributes 

    OctopusRoom.octopus(state_variables, save_state_callback)
    StateVariables.set_state(handler_input, "InOctopusRoom", True)

@sb.request_handler(can_handle_func = is_intent_name("WardrobeIntent"))
def wardrobe_handler(handler_input):
    """
    Handler for processing WardrobeIntent
    """
    state_variables = handler_input.attributes_manager.persistent_attributes       
    
    x = OctopusRoom.wardrobe(state_variables)

    return x
    

    

@sb.request_handler(can_handle_func=is_intent_name("MemoryCheckIntent"))
def memory_check_handler(handler_input):
    """
    Handler for checking what has been successfully saved into temp memory
    """
    # type: (HandlerInput) -> Response

    # TODO: REMOVE AS ONLY USED FOR TESTING (Or maybe find away to lock to developer mode only???)

    state_variables = handler_input.attributes_manager.session_attributes

    speech_text = "The last door you tried to go through is " + state_variables['door']
    reprompt = "Default reprompt"

    handler_input.response_builder.speak(speech_text).ask(reprompt)
    return handler_input.response_builder.response


# endregion 

# Custom Intents End 















# Built-In Intents Begin

# region
@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    """
    Handler for Help Intent.
    """
    # type: (HandlerInput) -> Response

    # TODO: Add functionality

    speech_text = "Default response"
    reprompt = "Default reprompt"

    handler_input.response_builder.speak(speech_text).ask(reprompt)
    return handler_input.response_builder.response

@sb.request_handler(
    can_handle_func=lambda input:
        is_intent_name("AMAZON.CancelIntent")(input) or
        is_intent_name("AMAZON.StopIntent")(input))
def cancel_and_stop_intent_handler(handler_input):
    """
    Single handler for Cancel and Stop Intent.
    """
    # type: (HandlerInput) -> Response
    
    speech_text = "Thanks for playing!!"
    
    handler_input.response_builder.speak(
        speech_text).set_should_end_session(True)
    return handler_input.response_builder.response

@sb.request_handler(can_handle_func=lambda input:
                    is_intent_name("AMAZON.FallbackIntent")(input) or
                    is_intent_name("AMAZON.YesIntent")(input) or
                    is_intent_name("AMAZON.NoIntent")(input))
def fallback_handler(handler_input):
    """
    AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    # type: (HandlerInput) -> Response

    # TODO: Customise or delete

    game_variables = handler_input.attributes_manager.session_attributes

    if ("game_state" in game_variables and
            game_variables["game_state"]=="STARTED"):
        speech_text = (
            "The {} skill can't help you with that.  "
            "Try guessing a number between 0 and 100. ".format(SKILL_NAME))
        reprompt = "Please guess a number between 0 and 100."
    else:
        speech_text = (
            "The {} skill can't help you with that.  "
            "It will come up with a number between 0 and 100 and "
            "you try to guess it by saying a number in that range. "
            "Would you like to play?".format(SKILL_NAME))
        reprompt = "Say yes to start the game or no to quit."

    handler_input.response_builder.speak(speech_text).ask(reprompt)
    return handler_input.response_builder.response


# endregion

# Built-In Intents End




@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):
    """
    Handler for Session End.
    """
    # type: (HandlerInput) -> Response
    logger.info(
        "Session ended with reason: {}".format(
            handler_input.request_envelope.request.reason))
    return handler_input.response_builder.response


def currently_playing(handler_input):
    """
    Function that acts as can handle for game state.
    """
    # type: (HandlerInput) -> bool

    # TODO: Decided if need, else delete

    is_currently_playing = False
    session_attr = handler_input.attributes_manager.session_attributes

    if ("game_state" in session_attr
            and session_attr['game_state'] == "STARTED"):
        is_currently_playing = True

    return is_currently_playing


@sb.request_handler(can_handle_func=lambda input:
                    not currently_playing(input) and
                    is_intent_name("AMAZON.YesIntent")(input))
def yes_handler(handler_input):
    """
    Handler for Yes Intent, only if the player said yes for
    a new game.
    """
    # type: (HandlerInput) -> Response


    # TODO: Decided if need, else delete. Useful as reference!!!!
   
    session_attr = handler_input.attributes_manager.session_attributes
    session_attr['game_state'] = "STARTED"
    session_attr['guess_number'] = random.randint(0, 100)
    session_attr['no_of_guesses'] = 0
 


    speech_text = "Great! Try saying a number to start the game."
    reprompt = "Try saying a number."

    handler_input.response_builder.speak(speech_text).ask(reprompt)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=lambda input:
                    not currently_playing(input) and
                    is_intent_name("AMAZON.NoIntent")(input))
def no_handler(handler_input):
    """
    Handler for No Intent, only if the player said no for
    a new game.
    """
    # type: (HandlerInput) -> Response

    # TODO: Decided if need, else delete. Useful as reference!!!!

    session_attr = handler_input.attributes_manager.session_attributes
    session_attr['game_state'] = "ENDED"
    session_attr['ended_session_count'] += 1

    handler_input.attributes_manager.persistent_attributes = session_attr
    handler_input.attributes_manager.save_persistent_attributes()

    speech_text = "Command Recognised"

    handler_input.response_builder.speak(speech_text)
    return handler_input.response_builder.response







@sb.request_handler(can_handle_func=lambda input: True)
def unhandled_intent_handler(handler_input):
    """
    Handler for all other unhandled requests.
    """
    # type: (HandlerInput) -> Response

    # TODO: Customise

    speech = "Say yes to continue or no to end the game!!"
    handler_input.response_builder.speak(speech).ask(speech)
    return handler_input.response_builder.response


@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    """
    Catch all exception handler, log exception and
    respond with custom message.
    """

    # TODO: Customise
    
    # type: (HandlerInput, Exception) -> Response
    logger.error(exception, exc_info=True)
    speech = "Sorry, I can't understand that. Please say again!!"
    handler_input.response_builder.speak(speech).ask(speech)
    return handler_input.response_builder.response


@sb.global_response_interceptor()
def log_response(handler_input, response):
    """
    Response logger.
    """
    # type: (HandlerInput, Response) -> None
    logger.info("Response: {}".format(response))


lambda_handler = sb.lambda_handler()
