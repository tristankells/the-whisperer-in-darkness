from os.path import abspath
from audio import Audio
import test_translator

class Translator() :
    """
    Final translator for the whisperer in darkness. Contains links to all audio 
    files when applicable
    """
    #TODO this whole file needs to use audio sources not plain text

    # Audio.FORMAT_STRING.format(".mp3")

    Launch = Audio.Intro
      
    # Generic mesages
    GenericError = Audio.FORMAT_STRING.format("19_Error.mp3")

    WrongThingToDo = GenericError

    DebugError = "Ok this ones on me I've made a mistake"

    Help = test_translator.Translator.Help

    EndGame = Audio.FORMAT_STRING.format("18_Epilogue.mp3")

    RepeatRiddle = test_translator.Translator.RepeatRiddle
    
    # Enter door intent

    LeftDoor = Audio.FORMAT_STRING.format("3_OpenDoorToOctopusRoom.mp3")
   
    RightDoor = Audio.FORMAT_STRING.format("9_EnterBookRoom.mp3")
       
    DoorError = GenericError

    # Investigate chains intent

    InvestigateChains = "The chains seemed tightly bound. You see a lock"

    AlreadyInvestigatedChains = GenericError

    ChainsError = test_translator.Translator.ChainsError

    # Use Key Intent

    UseKey = Audio.FORMAT_STRING.format("12_UnlockBook.mp3") #TODO why is this same as OpenBookInLobby

    UseKeyError_NoKey = GenericError

    UseKeyError_WrongRoom = GenericError

    # Open book room intent 

    OpenBookInMirrorRoom = Audio.FORMAT_STRING.format("13_OpenBookInBookRoom.mp3")

    OpenBookInLobby = Audio.FORMAT_STRING.format("12_UnlockBook.mp3")

    OpenBook_ItsLocked = GenericError

    OpenBook_ThereNoBook = GenericError

    OpenBookError = GenericError

    OpenBook_NotNeeded = GenericError

    # Leave room intent 

    LeaveMirrorRoom = "You left the room back to the lobby"

    LeaveRoomError = GenericError
    
    # Leave room intent 
    ThrowBook = Audio.FORMAT_STRING.format("14_ThrowBookAway.mp3")

    ThrowBookError = GenericError

    # Open chest intent
    OpenChest = Audio.FORMAT_STRING.format("10_Investigate_Chest.mp3")

    # Reach in chest intent
    ReachInChest = Audio.FORMAT_STRING.format("11_HandInBugChest.mp3")

    # Octopus messages

    Octopus_OctopusAlreadyReleased = GenericError

    Octopus_ReleaseOctopusBecomeBeach = Audio.FORMAT_STRING.format("7_ReleaseOctopus")

    Octopus_NoReturningTheOctopus = GenericError

    Octopus_AquariumShatters = GenericError

    Octopus_OpenWardrobeBeforeAquarium = Audio.FORMAT_STRING.format("4_OpenWardrobeWhenFirstInRoom.mp3")

    Octopus_OpenWardrobeBeforeOctopusRelease = Audio.FORMAT_STRING.format("6_WardrobeOnBeachWithOctopus.mp3")

    Octopus_OpenWardrobeToExitBeach = Audio.FORMAT_STRING.format("17_SearchForWardrobeOnBeach.mp3")

    Octopus_OpenAquarium = Audio.FORMAT_STRING.format("5_GrabOctopus.mp3")

    Octopus_SearchBeach = Audio.FORMAT_STRING.format("8_SearchBeach.mp3")