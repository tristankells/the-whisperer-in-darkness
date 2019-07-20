from test_translator import Translator

class TheWhispererInDarkness :

    @staticmethod
    def handle_launch() :
        return Translator.Launch
    
    @staticmethod
    def enter_door(door):
        """ 
        returns a string to be said by Alexa after entering a door.
        """
        # if door is a Door then use it to choose which door, else assume door is a string
        if (isinstance(door, Door))
        {
            if (door == Door.first)
                return Translator.LeftDoor
            if (door == Door.second)
                return Translator.RightDoor
            
            return Translator.DoorError
        }

        door = str(door)

        if (door == "left" or door == "one"  or door == "first" ) :
            return Translator.LeftDoor

        if (door == "right" or door == "two"  or door == "second" ) :
            return Translator.RightDoor
        
        return Translator.DoorError

    @staticmethod
    def exposition(parameter_list):
        pass




        