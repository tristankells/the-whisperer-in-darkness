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

SKILL_NAME = 'Language Of Love'
sb = StandardSkillBuilder(table_name="The-Whisperer-In-Darkness", auto_create_table=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    """Handler for Skill Launch."""
    # type: (HandlerInput) -> Response
    state_variables = handler_input.attributes_manager.persistent_attributes
    if not state_variables:
        state_variables['playing'] = True

    handler_input.attributes_manager.session_attributes = state_variables
 
    language_of_love.handleLaunch()

    handler_input.response_builder.speak(language_of_love.Response).ask("What is your name")

    return handler_input.response_builder.response

# # # GENERAL request_handlers # # #
#region
@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    """Handler for Help Intent."""
    # type: (HandlerInput) -> Response

    state_variables = handler_input.attributes_manager.persistent_attributes

    language_of_love.setup(state_variables)

    language_of_love.handleHelpInput()

    handler_input.response_builder.speak(language_of_love.Response)

    handler_input.attributes_manager.session_attributes = language_of_love.getStateVariables()

    return handler_input.response_builder.response

@sb.request_handler(can_handle_func=is_intent_name("TutorialIntent"))
def tutorial_intent_handler(handler_input):
    """
    Handler for Tutorial Intent.
    """
    # type: (HandlerInput) -> Response
    language_of_love.handleHelpInput()

    handler_input.response_builder.speak(language_of_love.Response)

    return handler_input.response_builder.response

@sb.request_handler(can_handle_func = lambda input:
                    is_intent_name("AnswerNameIntent")(input))
def answer_name_handler(handler_input):
    """
    Handler the player answering a question with their name
    """
    # type: (HandlerInput) -> Response

    state_variables = handler_input.attributes_manager.persistent_attributes

    state_variables["name"] = input

    language_of_love.setup(state_variables)

    language_of_love.handleAnswerName()

    handler_input.response_builder.speak(language_of_love.Response).ask("Ask")    

    handler_input.attributes_manager.session_attributes = language_of_love.getStateVariables()

    return handler_input.response_builder.response

# # Handle the player asking where their date is from 
@sb.request_handler(can_handle_func = is_intent_name("QuestionWhereYouFromIntent"))
def question_where_are_you_from_handler(handler_input):
    """Handler for use asking where their date is from"""
    # type: (HandlerInput) -> Response

    state_variables = handler_input.attributes_manager.persistent_attributes

    language_of_love.setup(state_variables)

    language_of_love.handleQuestionWhereAreYouFrom()

    handler_input.response_builder.speak(language_of_love.Response).ask("Ask")    

    handler_input.attributes_manager.session_attributes = language_of_love.getStateVariables()

    return handler_input.response_builder.response

#endregion


# # # Date request_handlers # # # 
#region
@sb.request_handler(can_handle_func = is_intent_name("StartSpeedDateIntent"))
def start_speed_date_handler(handler_input):
    """
    Handler for starting speed dating
    """
    # type: (HandlerInput) -> Response
    
    language_of_love.handleStartDate()

    handler_input.response_builder.speak(language_of_love.Response).ask("Ask")    
   
    return handler_input.response_builder.response


#endregion

# # # Practice request_handlers # # # 
#region
@sb.request_handler(can_handle_func = is_intent_name("StartPracticeIntent"))
def start_practice_handler(handler_input):
    """
    Handler for starting practice
    """
    # type: (HandlerInput) -> Response
    
    language_of_love.handleStartPractice()

    handler_input.response_builder.speak(language_of_love.Response).ask("Ask")    
   
    return handler_input.response_builder.response


#endregion



#
#  MOVE INTENT
#                                 

@sb.request_handler(can_handle_func = lambda input:
                    is_intent_name("MoveIntent")(input))
def movement_handler(handler_input):
    """Handler for processing guess with target."""
    # type: (HandlerInput) -> Response

    direction = str(handler_input.request_envelope.request.intent.slots["movement"].value) # value of movement slot

    game_variables = handler_input.attributes_manager.session_attributes # session variables

    return handler_input.response_builder.response





@sb.request_handler(
    can_handle_func=lambda input:
        is_intent_name("AMAZON.CancelIntent")(input) or
        is_intent_name("AMAZON.StopIntent")(input))
def cancel_and_stop_intent_handler(handler_input):
    """Single handler for Cancel and Stop Intent."""
    # type: (HandlerInput) -> Response
    speech_text = "Thanks for playing!!"

    handler_input.response_builder.speak(
        speech_text).set_should_end_session(True)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):
    """Handler for Session End."""
    # type: (HandlerInput) -> Response
    logger.info(
        "Session ended with reason: {}".format(
            handler_input.request_envelope.request.reason))
    return handler_input.response_builder.response


def currently_playing(handler_input):
    """Function that acts as can handle for game state."""
    # type: (HandlerInput) -> bool
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
    """Handler for Yes Intent, only if the player said yes for
    a new game.
    """
    # type: (HandlerInput) -> Response
   
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
    """Handler for No Intent, only if the player said no for
    a new game.
    """
    # type: (HandlerInput) -> Response
    session_attr = handler_input.attributes_manager.session_attributes
    session_attr['game_state'] = "ENDED"
    session_attr['ended_session_count'] += 1

    handler_input.attributes_manager.persistent_attributes = session_attr
    handler_input.attributes_manager.save_persistent_attributes()

    speech_text = "Command Recognised"

    handler_input.response_builder.speak(speech_text)
    return handler_input.response_builder.response




@sb.request_handler(can_handle_func=lambda input:
                    is_intent_name("AMAZON.FallbackIntent")(input) or
                    is_intent_name("AMAZON.YesIntent")(input) or
                    is_intent_name("AMAZON.NoIntent")(input))
def fallback_handler(handler_input):
    """AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    # type: (HandlerInput) -> Response
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


@sb.request_handler(can_handle_func=lambda input: True)
def unhandled_intent_handler(handler_input):
    """Handler for all other unhandled requests."""
    # type: (HandlerInput) -> Response
    speech = "Say yes to continue or no to end the game!!"
    handler_input.response_builder.speak(speech).ask(speech)
    return handler_input.response_builder.response


@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    # type: (HandlerInput, Exception) -> Response
    logger.error(exception, exc_info=True)
    speech = "Sorry, I can't understand that. Please say again!!"
    handler_input.response_builder.speak(speech).ask(speech)
    return handler_input.response_builder.response


@sb.global_response_interceptor()
def log_response(handler_input, response):
    """Response logger."""
    # type: (HandlerInput, Response) -> None
    logger.info("Response: {}".format(response))


lambda_handler = sb.lambda_handler()
