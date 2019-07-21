from test_translator import Translator
# from slot_types import Door
# from slot_types import LeftRight
from audio import Audio
from alexa_helper import StateVariables
from alexa_helper import StateHelper
from slot_types import Room
from response import Response

class TheWhispererInDarkness :

    @staticmethod
    def handle_launch() :
        return Response(Translator.Launch, should_save_speech_text=False) 
    
    @staticmethod
    def enter_door(door, state_variables):
        """ 
        TODO
        """
        speech_text = None
        
        # if door is a Door then use it to choose which door, else assume door is a string
        if (door is None):
            speech_text = Translator.DoorError
        elif (#(isinstance(door, Door) and door == Door.first) or
            #(isinstance(door, LeftRight) and door == LeftRight.left) or
            (isinstance(door, str) and door.upper() in map(str.upper , ["first", "left", "one", "1"]))
            or door == 1):
            state_variables["Room"] = Room.octopus
            speech_text =  Translator.LeftDoor
        elif (#(isinstance(door, Door) and door == Door.second) or
            #(isinstance(door, LeftRight) and door == LeftRight.right) or
            (isinstance(door, str) and door.upper() in map(str.upper , ["second", "right", "two", "2"]))
            or door == 2):
            state_variables["Room"] = Room.mirror
            speech_text =  Translator.RightDoor
        else:
            speech_text = Translator.DoorError

        return Response(speech_text, state_variables = state_variables)

    @staticmethod
    def investigate_chains(state_variables) :
        speech_text = None

        if(Room(state_variables["Room"]) == Room.mirror) :
            if(state_variables["ChainsInvestigated"] == False) :
                speech_text = Translator.InvestigateChains
                state_variables["ChainsInvestigated"] = True
            else : 
                speech_text = Translator.AlreadyInvestigatedChains

        # Error catching   
        if(speech_text == None) :
            speech_text = Translator.ChainsError


        return Response(speech_text, state_variables = state_variables)

    @staticmethod
    def use_key(state_variables):
        speech_text = None

        #In the mirror room 
        if(Room(state_variables["Room"]) == Room.mirror) :

            # And you have the key
            if(state_variables["HasKey"] == True) :
                
                # And you dont already have the book 
                if(state_variables["HasBook"] == False) :
                    state_variables["BookLocked"] = False
                    speech_text = Translator.UseKey
                
                # But you already have the book
                elif(state_variables["HasBook"] == True) :
                    speech_text = Translator.GenericError

            #But you dont have the key 
            elif(state_variables["HasKey"] == False) :
                speech_text = Translator.GenericError

        #If you in any room but the mirror room  
        elif(state_variables["HasKey"] == False) :
            speech_text = Translator.GenericError       

        if(speech_text == None) :
            speech_text = Translator.GenericError

        return Response(speech_text, state_variables = state_variables) 

    @staticmethod
    def open_book(state_variables):
        speech_text = None

        #In the mirror room 
        if(Room(state_variables["Room"]) == Room.mirror) :

            #If book is no longer in chains
            if(state_variables['BookLocked'] == False) :
                
                #If you dont have the book yet / havent tried to open it yet
                if(state_variables['HasBook'] == False) :
                    speech_text = Translator.OpenBookInMirrorRoom
                    state_variables['HasBook'] = True

                #If you have already opened the book in the mirror room
                elif(state_variables['HasBook'] == True) :
                    speech_text = Translator.OpenBook_NotNeeded

            #If book is still in chains
            elif(state_variables['BookLocked'] == True) :
                speech_text = Translator.OpenBook_ItsLocked

        #In the lobby room 
        elif(Room(state_variables["Room"]) == Room.lobby) :

            #If you have the book
            if(state_variables['HasBook'] == True ) :

                #If the mirror has yet to be be broken
                if(state_variables['MirrorBroken'] == False) : 
                    
                    # If the octopus has been released when you break the glass, trigger game exit
                    if(state_variables['OctopusReleased'] == True) :
                        speech_text = Translator.OpenBookInLobby + Translator.EndGame

                    elif(state_variables['OctopusReleased'] == False) :
                        speech_text = Translator.OpenBookInLobby
                        state_variables['MirrorBroken'] = True

                #If the mirror is already broken
                elif(state_variables['MirrorBroken'] == True):
                    speech_text = Translator.OpenBook_NotNeeded
                
            #If you DON'T have the book
            elif(state_variables['HasBook'] == False):
                speech_text = Translator.GenericError

        #In the octopus room 
        elif(Room(state_variables["Room"]) == Room.octopus) :
           speech_text = Translator.GenericError

        #Final error catch
        if(speech_text == None) :
            speech_text = Translator.DebugError
        
        return Response(speech_text, state_variables = state_variables) 

    @staticmethod
    def leave_room(state_variables):
        speech_text = None

        #If the player is in any room EXCEPT for the lobby
        if(Room(state_variables["Room"]) != Room.lobby) :
            state_variables["Room"] = Room.lobby
            speech_text = Translator.LeaveRoom
        
        #If the player is in the lobby
        elif(Room(state_variables["Room"]) == Room.lobby) :
            speech_text =  Translator.LeaveRoomError

        #Final error catch
        if(speech_text == None) :
            speech_text = Translator.DebugError

        return Response(speech_text, state_variables = state_variables)

    @staticmethod
    def throw_book(state_variables) :
        speech_text = None
        
        #if the player has the book
        if(state_variables["HasBook"] == True) :
            speech_text = Translator.ThrowBook
        
        #else if the player doe not have the book
        elif(state_variables["HasBook"] == False) :
            speech_text = Translator.GenericError

        #Final error catch
        if(speech_text == None) :
            speech_text = Translator.DebugError

        return Response(speech_text, state_variables = state_variables) 
    
    @staticmethod
    def open_chest(state_variables) :
        speech_text = None

        #In the mirror room 
        if(Room(state_variables["Room"]) == Room.mirror) :

            #If the player does not already have the key
            if(state_variables['ChestOpened'] == False) :
                state_variables["ChestOpened"] = True
                speech_text = Translator.OpenChest

            #if the player already has the key
            elif(state_variables['ChestOpened'] == True) :
                speech_text = Translator.GenericError

        # If the player is in any room BUT the mirror room
        elif(Room(state_variables["Room"]) != Room.mirror) :
            speech_text = Translator.GenericError

        #Final error catch
        if(speech_text == None) :
            speech_text = Translator.DebugError

        return Response(speech_text, state_variables = state_variables) 

    @staticmethod
    def reach_in_chest(state_variables) :
        speech_text = None

        #In the mirror room 
        if(Room(state_variables["Room"]) == Room.mirror) :

            # And the chest is opened / been investigated
            if(state_variables["ChestOpened"] == True) :
                state_variables["HasKey"] = True
                speech_text = Translator.ReachInChest

            # The chest hasn not been opened yet
            elif(state_variables["ChestOpened"] == False) :
                speech_text = Translator.GenericError

        # If the player is in any room BUT the mirror room
        elif(Room(state_variables["Room"]) != Room.mirror) :
            speech_text = Translator.GenericError
        
        #Final error catch
        if(speech_text == None) :
            speech_text = Translator.DebugError

        return Response(speech_text, state_variables)

    @staticmethod
    def help() :

        speech_text = Translator.Help

        return Response(speech_text) 

    @staticmethod
    def fallback() :

        speech_text = Translator.GenericError
        
        return Response(speech_text) 



        




class OctopusRoom :
    IS_OCTOPUS_RELEASED = "IsOctopusReleased"

    @staticmethod
    def octopus_old(state_variables, save_state_callback=None):
        
        if (not save_state_callback is None):
            StateVariables.set_state_v2(state_variables, save_state_callback, "Error", Audio.octopus_room_error_audio)
    
    @staticmethod
    def wardrobe(state_variables):
        # we use state helper since it automatically converts key errors into None
        state_helper = StateHelper(lambda: state_variables)
        
        is_octopus_released = state_helper.get_state(OctopusRoom.IS_OCTOPUS_RELEASED)
        
        if (is_octopus_released):
            speech_text = "The wardrobe door slams shut. After a moment inside, you open it, and sense the presence again. You have returned to the entry way."
            state_variables["Room"] = Room.lobby

        response = Response(speech_text, state_variables=state_variables)
        return response

    @staticmethod
    def octopus(state_variables):
        should_save_speech_text = True
        # we use state helper since it automatically converts key errors into None
        state_helper = StateHelper(lambda: state_variables)
        is_octopus_released = state_helper.get_state(OctopusRoom.IS_OCTOPUS_RELEASED)

        if (is_octopus_released):
            should_save_speech_text=False
            speech_text = "The Octopus has already been released." + "\nYou hear waves crashing and the squawk of a seagull."
        else:
            speech_text = "The room turns into sand" + "\nYou hear waves crashing and the squawk of a seagull."
            state_variables[OctopusRoom.IS_OCTOPUS_RELEASED]
        
        response = Response(speech_text, state_variables=state_variables, should_save_speech_text=should_save_speech_text)
        return response
    
    
        
        