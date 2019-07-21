from os.path import abspath
from audio import Audio

class Translator() :
    """
    Final translator for the whisperer in darkness. Contains links to all audio 
    files when applicable
    """
    #TODO this whole file needs to use audio sources not plain text

    # Audio.FORMAT_STRING.format(".mp3")

    Launch = Audio.Intro
      
    # Generic mesages
    GenericError = "You tried that, but nothing happens"

    WrongThingToDo = "That's the wrong thing to do"

    DebugError = "The logic is hecka funked"

    Help = "You ask for help, but you wont even help yourself"

    EndGame = "You broke the mirror, freed the squid and now you win"

    RepeatRiddle = "You asked fo rthe riddle again. You would be lucky"
    
    # Enter door intent

    LeftDoor = Audio.FORMAT_STRING.format("3_OpenDoorToOctopusRoom.mp3")
   
    RightDoor = Audio.FORMAT_STRING.format("9_EnterBookRoom.mp3")
       
    DoorError = "You cant go through"

    # Investigate chains intent

    InvestigateChains = "The chains seemed tightly bound. You see a lock"

    AlreadyInvestigatedChains = "Not much more to see here "

    ChainsError = "Not the time to investigate chains"

    # Use Key Intent

    UseKey = "You unlocked the chain, now you have acess to the tome "

    UseKeyError_NoKey = "Key? What key?"

    UseKeyError_WrongRoom = "Nothing to unlock right now "

    # Open book room intent 

    OpenBookInMirrorRoom = Audio.FORMAT_STRING.format("13_OpenBookInBookRoom.mp3")

    OpenBookInLobby = Audio.FORMAT_STRING.format("12_UnlockBook.mp3")

    OpenBook_ItsLocked = "The chains wrapped around it prevent you from opening the book"

    OpenBook_ThereNoBook = GenericError

    OpenBookError = GenericError

    OpenBook_NotNeeded = GenericError

    # Leave room intent 

    LeaveRoom = "You left the room back to the lobby"

    LeaveRoomError = "You cant escape this house"
    
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

    Octopus_OpenWardrobeToExitBeach = "Please can I have an audio file"

    Octopus_OpenAquarium = Audio.FORMAT_STRING.format("5_GrabOctopus.mp3")

    Octopus_SearchBeach = Audio.FORMAT_STRING.format("8_SearchBeach.mp3")