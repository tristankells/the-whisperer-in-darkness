from test_translator import Translator
from slot_types import Door
from audio import Audio
from alexa_helper import StateVariables

class TheWhispererInDarkness :

    @staticmethod
    def handle_launch() :
        return Translator.Launch
    
    @staticmethod
    def enter_door(door, save_state_callback=None):
        """ 
        TODO
        """
        # if door is a Door then use it to choose which door, else assume door is a string
        if (isinstance(door, Door)):        
            if (door == Door.first):
                return Translator.LeftDoor
            if (door == Door.second):
                return Translator.RightDoor
            
            return Translator.DoorError
        

        door = str(door)

        if (door == "left" or door == "one"  or door == "first" ) :
            return Translator.LeftDoor

        if (door == "right" or door == "two"  or door == "second" ) :
            return Translator.RightDoor
        
        return Translator.DoorError

    @staticmethod
    def exposition(parameter_list):
        pass



class OctopusRoom :

    @staticmethod
    def wardrobe(state_variables):
            
        if (not state_variables["InOctopusRoom"]):
            return state_variables["Error"]

        if (state_variables["IsOctopusReleased"]):
            pass

        #TODO error
    
    @staticmethod
    def octopus(state_variables, save_state_callback=None):
        
        if (not save_state_callback is None):
            StateVariables.set_state_v2(state_variables, save_state_callback, "Error", Audio.octopus_room_error_audio)
        
        