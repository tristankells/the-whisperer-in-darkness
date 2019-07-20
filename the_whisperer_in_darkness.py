from test_translator import Translator
from slot_types import Door
from slot_types import Room

class TheWhispererInDarkness :

    @staticmethod
    def handle_launch() :
        return Translator.Launch
    
    @staticmethod
    def enter_door(door):
        """ 
        TODO
        """
        # if door is a Door then use it to choose which door, else assume door is a string
               
        if (door == Door.first):
                return Translator.LeftDoor
        if (door == Door.second):
                return Translator.RightDoor        

        door = str(door)

        if (door == "left" or door == "one" or door == "1" or door == 1  or door == "first" ) :
            return Translator.LeftDoor

        if (door == "right" or door == "two" or door == "2" or door == 2  or door == "second" ) :
            
            return Translator.RightDoor
        
        return Translator.DoorError

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

        





        