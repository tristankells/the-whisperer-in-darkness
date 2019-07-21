from translator import Translator
# from slot_types import Door
# from slot_types import LeftRight
from audio import Audio
from alexa_helper import StateVariables
from alexa_helper import StateHelper
from slot_types import Room
from response import Response

class TheWhispererInDarkness :
    ROOM = "Room"
    HAS_KEY = "HasKey"
    CHAINS_INVESTIGATED = "ChainsInvestigated"
    BOOK_UNLOCKED = "BookLocked"
    HAS_BOOK = "HasBook"
    CHEST_OPENED = "ChestOpened"
    MIRROR_BROKEN = "MirrorBroken"

    @staticmethod
    def handle_launch() :
        return Response(Translator.Launch, should_save_speech_text=False) 
    
    @staticmethod
    def generic_error_response():
        return Response(Translator.GenericError, should_save_speech_text=False)

    @staticmethod
    def enter_door(door, state_variables):
        """ 
        TODO
        """
        speech_text = None
        
        # if door is a Door then use it to choose which door, else assume door is a string
        if (door is None):
            speech_text = Translator.DoorError
        elif ((isinstance(door, str) and door.upper() in ["FIRST", "LEFT", "ONE", "1"]) or door == 1):
            state_variables[TheWhispererInDarkness.ROOM] = Room.octopus
            speech_text =  Translator.LeftDoor
        elif ((isinstance(door, str) and door.upper() in ["SECOND", "RIGHT", "TWO", "2"]) or door == 2):
            state_variables[TheWhispererInDarkness.ROOM] = Room.mirror
            speech_text =  Translator.RightDoor
        else:
            speech_text = Translator.DoorError

        return Response(speech_text, state_variables = state_variables)

    @staticmethod
    def investigate_chains(state_variables) :
        speech_text = None

        if(Room(state_variables[TheWhispererInDarkness.ROOM]) == Room.mirror) :
            if(state_variables[TheWhispererInDarkness.CHAINS_INVESTIGATED] == False) :
                speech_text = Translator.InvestigateChains
                state_variables[TheWhispererInDarkness.CHAINS_INVESTIGATED] = True
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
        if(Room(state_variables[TheWhispererInDarkness.ROOM]) == Room.mirror) :

            # And you have the key
            if(state_variables[TheWhispererInDarkness.HAS_KEY] == True) :
                
                # And you dont already have the book 
                if(state_variables[TheWhispererInDarkness.HAS_BOOK] == False) :
                    state_variables[TheWhispererInDarkness.BOOK_UNLOCKED] = True
                    speech_text = Translator.UseKey
                
                # But you already have the book
                elif(state_variables[TheWhispererInDarkness.HAS_BOOK] == True) :
                    speech_text = Translator.GenericError

            #But you dont have the key 
            elif(state_variables[TheWhispererInDarkness.HAS_KEY] == False) :
                speech_text = Translator.GenericError

        #If you in any room but the mirror room  
        elif(state_variables[TheWhispererInDarkness.HAS_KEY] == False) :
            speech_text = Translator.GenericError       

        if(speech_text == None) :
            speech_text = Translator.GenericError

        return Response(speech_text, state_variables = state_variables) 

    @staticmethod
    def open_book(state_variables):
        speech_text = None

        #In the mirror room 
        if(Room(state_variables[TheWhispererInDarkness.ROOM]) == Room.mirror) :

            #If book is no longer in chains
            if(state_variables[TheWhispererInDarkness.BOOK_UNLOCKED] == True) :
                
                #If you dont have the book yet / havent tried to open it yet
                if(state_variables[TheWhispererInDarkness.HAS_BOOK] == False) :
                    speech_text = Translator.OpenBookInMirrorRoom
                    state_variables[TheWhispererInDarkness.HAS_BOOK] = True

                #If you have already opened the book in the mirror room
                elif(state_variables[TheWhispererInDarkness.HAS_BOOK] == True) :
                    speech_text = Translator.OpenBook_NotNeeded

            #If book is still in chains
            elif(state_variables[TheWhispererInDarkness.BOOK_UNLOCKED] == False) :
                speech_text = Translator.OpenBook_ItsLocked

        #In the lobby room 
        elif(Room(state_variables[TheWhispererInDarkness.ROOM]) == Room.lobby) :

            #If you have the book
            if(state_variables[TheWhispererInDarkness.HAS_BOOK] == True ) :

                #If the mirror has yet to be be broken
                if(state_variables[TheWhispererInDarkness.MIRROR_BROKEN] == False) : 
                    
                    # If the octopus has been released when you break the glass, trigger game exit
                    if(state_variables[OctopusRoom.IS_OCTOPUS_RELEASED] == True) :
                        speech_text = Translator.OpenBookInLobby + Translator.EndGame

                    elif(state_variables[OctopusRoom.IS_OCTOPUS_RELEASED] == False) :
                        speech_text = Translator.OpenBookInLobby
                        state_variables[TheWhispererInDarkness.MIRROR_BROKEN] = True

                #If the mirror is already broken
                elif(state_variables[TheWhispererInDarkness.MIRROR_BROKEN] == True):
                    speech_text = Translator.OpenBook_NotNeeded
                
            #If you DON'T have the book
            elif(state_variables[TheWhispererInDarkness.HAS_BOOK] == False):
                speech_text = Translator.GenericError

        #In the octopus room 
        elif(Room(state_variables[TheWhispererInDarkness.ROOM]) == Room.octopus) :
           speech_text = Translator.GenericError

        #Final error catch
        if(speech_text == None) :
            speech_text = Translator.DebugError
        
        return Response(speech_text, state_variables = state_variables) 

    @staticmethod
    def leave_room(state_variables):
        speech_text = None

        #If the player is in any room EXCEPT for the lobby
        if(Room(state_variables[TheWhispererInDarkness.ROOM]) != Room.lobby):
            state_variables[TheWhispererInDarkness.ROOM] = Room.lobby
            speech_text = Translator.LeaveMirrorRoom
        
        #If the player is in the lobby
        elif(Room(state_variables[TheWhispererInDarkness.ROOM]) == Room.lobby):
            speech_text =  Translator.LeaveRoomError

        #Final error catch
        if(speech_text == None) :
            speech_text = Translator.DebugError

        return Response(speech_text, state_variables = state_variables)

    @staticmethod
    def throw_book(state_variables) :
        speech_text = None
        
        #if the player has the book
        if(state_variables[TheWhispererInDarkness.HAS_BOOK] == True) :
            speech_text = Translator.ThrowBook
        
        #else if the player doe not have the book
        elif(state_variables[TheWhispererInDarkness.HAS_BOOK] == False) :
            speech_text = Translator.GenericError

        #Final error catch
        if(speech_text == None) :
            speech_text = Translator.DebugError

        return Response(speech_text, state_variables = state_variables) 
    
    @staticmethod
    def open_chest(state_variables) :
        state_helper = StateHelper(lambda: state_variables)

        room = Room(state_helper.get_state(TheWhispererInDarkness.ROOM))

        speech_text = None

        #In the mirror room 
        if(room == Room.mirror) :

            #If the player does not already have the key
            if(state_variables[TheWhispererInDarkness.CHEST_OPENED] == False) :
                state_variables[TheWhispererInDarkness.CHEST_OPENED] = True
                speech_text = Translator.OpenChest

            #if the player already has the key
            elif(state_variables[TheWhispererInDarkness.CHEST_OPENED] == True) :
                speech_text = Translator.GenericError

        # If the player is in any room BUT the mirror room
        elif(room != Room.mirror) :
            speech_text = Translator.GenericError

        #Final error catch
        if(speech_text == None) :
            speech_text = Translator.DebugError

        return Response(speech_text, state_variables = state_variables) 

    @staticmethod
    def reach_in_chest(state_variables) :
        speech_text = None

        #In the mirror room 
        if(Room(state_variables[TheWhispererInDarkness.ROOM]) == Room.mirror) :

            # And the chest is opened / been investigated
            if(state_variables[TheWhispererInDarkness.CHEST_OPENED] == True) :
                state_variables[TheWhispererInDarkness.HAS_KEY] = True
                speech_text = Translator.ReachInChest

            # The chest hasn not been opened yet
            elif(state_variables[TheWhispererInDarkness.CHEST_OPENED] == False) :
                speech_text = Translator.GenericError

        # If the player is in any room BUT the mirror room
        elif(Room(state_variables[TheWhispererInDarkness.ROOM]) != Room.mirror) :
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
    
    @staticmethod
    def repeat_riddle() :

        speech_text = Translator.RepeatRiddle
        
        return Response(speech_text) 



        




class OctopusRoom :
    IS_OCTOPUS_RELEASED = "IsOctopusReleased"
    IS_AQUARIUM_OPEN = "IsAquariumOpen"

    @staticmethod
    def wardrobe(state_variables):
        should_save_speech_text = True
        # we use state helper since it automatically converts key errors into None
        state_helper = StateHelper(lambda: state_variables)
        is_aquarium_open = state_helper.get_state(OctopusRoom.IS_AQUARIUM_OPEN)
        is_octopus_released = state_helper.get_state(OctopusRoom.IS_OCTOPUS_RELEASED)
        room = state_helper.get_state(TheWhispererInDarkness.ROOM)
       
        in_octopus_room = room is not None and Room(room) == Room.octopus
        if (not in_octopus_room):
            should_save_speech_text=False
            speech_text = Translator.GenericError
        elif (not is_aquarium_open and not is_octopus_released):
            speech_text = Translator.Octopus_OpenWardrobeBeforeAquarium
        elif (is_aquarium_open and not is_octopus_released):
            speech_text = Translator.Octopus_OpenWardrobeBeforeOctopusRelease
        elif (is_aquarium_open and is_octopus_released):
            state_variables[TheWhispererInDarkness.ROOM] = Room.lobby
            if (True):
                speech_text = Translator.Octopus_OpenWardrobeToExitBeach
            else:
                speech_text = Translator.Octopus_OpenWardrobeToExitBeach + Translator.EndGame
        else:
            speech_text = Translator.DebugError
            
        response = Response(speech_text, state_variables=state_variables, should_save_speech_text=should_save_speech_text)
        return response

    @staticmethod
    def octopus(state_variables):
        should_save_speech_text = True
        # we use state helper since it automatically converts key errors into None
        state_helper = StateHelper(lambda: state_variables)
        is_octopus_released = state_helper.get_state(OctopusRoom.IS_OCTOPUS_RELEASED)
        room = state_helper.get_state(TheWhispererInDarkness.ROOM)
        
        in_octopus_room = room is not None and Room(room) == Room.octopus
        if (not in_octopus_room):
            should_save_speech_text=False
            speech_text = Translator.GenericError

        if (is_octopus_released):
            should_save_speech_text=False
            speech_text = Translator.Octopus_OctopusAlreadyReleased + "\n" + Translator.Octopus_ExprienceTheBeach
        else:
            speech_text = Translator.Octopus_ReleaseOctopusBecomeBeach
            state_variables[OctopusRoom.IS_OCTOPUS_RELEASED]
        
        response = Response(speech_text, state_variables=state_variables, should_save_speech_text=should_save_speech_text)
        return response

    @staticmethod
    def bad_octopus(state_variables):
        should_save_speech_text = True
        # we use state helper since it automatically converts key errors into None
        state_helper = StateHelper(lambda: state_variables)
        is_octopus_released = state_helper.get_state(OctopusRoom.IS_OCTOPUS_RELEASED)
        room = state_helper.get_state(TheWhispererInDarkness.ROOM)
        
        in_octopus_room = room is not None and Room(room) == Room.octopus
        if (not in_octopus_room):
            should_save_speech_text=False
            speech_text = Translator.GenericError

        if (is_octopus_released):
            should_save_speech_text=False
            speech_text = Translator.Octopus_OctopusAlreadyReleased + "\n" + Translator.Octopus_ExprienceTheBeach
        else:
            #TODO can we add octopus specific audio here?
            speech_text = Translator.WrongThingToDo
            state_variables[OctopusRoom.IS_OCTOPUS_RELEASED]
        
        response = Response(speech_text, state_variables=state_variables, should_save_speech_text=should_save_speech_text)
        return response

    @staticmethod
    def aquarium(state_variables):
        should_save_speech_text = True
        # we use state helper since it automatically converts key errors into None
        state_helper = StateHelper(lambda: state_variables)
        is_aquarium_open = state_helper.get_state(OctopusRoom.IS_AQUARIUM_OPEN)
        is_octopus_released = state_helper.get_state(OctopusRoom.IS_OCTOPUS_RELEASED)
        room = state_helper.get_state(TheWhispererInDarkness.ROOM)
        
        in_octopus_room = room is not None and Room(room) == Room.octopus
        if (not in_octopus_room):
            should_save_speech_text=False
            speech_text = Translator.GenericError
        elif (is_aquarium_open and is_octopus_released):
            should_save_speech_text = False
            speech_text = Translator.Octopus_AquariumShatters + "\n" + Translator.Octopus_ExprienceTheBeach
        elif (is_aquarium_open and not is_octopus_released):
            state_variables[OctopusRoom.IS_OCTOPUS_RELEASED] = False
            speech_text = Translator.Octopus_ReleaseOctopusBecomeBeach
        elif (not is_aquarium_open and not is_octopus_released):
            state_variables[OctopusRoom.IS_AQUARIUM_OPEN] = True
            speech_text = Translator.Octopus_OpenAquarium
        else:
            speech_text = Translator.DebugError
                    
        response = Response(speech_text, state_variables=state_variables, should_save_speech_text=should_save_speech_text)
        return response
        
    
        
        