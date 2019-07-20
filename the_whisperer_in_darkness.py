from test_translator import Translator
from slot_types import Door
from slot_types import Room

class TheWhispererInDarkness :

    @staticmethod
    def handle_launch() :
        return Translator.Launch
    
    @staticmethod
    def enter_door(door, state_variables):
        """ 
        TODO
        """
        response = {}
        speech_text = None
        
        # if door is a Door then use it to choose which door, else assume door is a string
            

        if (door == "left" or door == "one" or door == "1" or door == 1  or door == "first" or door == Door.first ) :
            state_variables["Room"] = Room.octopus
            speech_text =  Translator.LeftDoor

        if (door == "right" or door == "two" or door == "2" or door == 2  or door == "second" or door == Door.second ) :
            state_variables["Room"] = Room.mirror
            speech_text =  Translator.RightDoor
        
        response["state_variables"] = state_variables

        if(speech_text == None) : 
            speech_text = Translator.DoorError

        response["speech_text"] = speech_text

        response["speech_text"] = "Slot value is " + door + " " + response["speech_text"]
        
        return response

    @staticmethod
    def exposition(parameter_list):
        pass

    @staticmethod
    def investigate_chains(room) :
        if(room != Room.mirror) :
           return Translator.ChainsError
        return Translator.InvestigateChains

    @staticmethod
    def use_key(room, has_key):
        if(room != Room.mirror) :
           return Translator.UseKeyError_WrongRoom
        if(has_key == False) :
            return Translator.UseKeyError_NoKey
        return Translator.UseKey

        





        