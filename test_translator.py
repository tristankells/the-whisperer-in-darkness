from os.path import abspath
from audio import Audio

class Translator() :
    """
    Test translator for the whisperer in darkness. Contains shorter, more
    debug focussed test phrases.abspath
    """
    Launch = "Welcome to whisperer in the darkness"
      
    # Enter door intent

    LeftDoor = "you enter the door on your left"
   
    RightDoor = "you enter the door on your right"
       
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

    OpenBookInMirrorRoom = "You open the book. It screams at you"

    OpenBookInLobby = "It breaks the mirror into a million piece "

    OpenBook_ItsLocked = "The chains wrapped around it prevent you from opening the book"

    OpenBook_ThereNoBook = "I cant see no book"

    OpenBookError = "Book error message"

    OpenBook_NotNeeded = "Nothing more happens, except you increased descent in insanity"

    # Leave room intent 

    LeaveRoom = "You left the room back to the lobby"

    LeaveRoomError = "You cant escape this house"
    
    # Leave room intent 
    ThrowBook = "You try to toss it, but you never seem to be able to muster the strength to get rid of it"

    ThrowBookError = "You try to throw it, but you dont have it"

    # Open chest intent
    OpenChest = "You open the chest. Its fucking gross in there"

    # Reach in chest intent
    ReachInChest = "You reach through the grossness and grab a key"

    # Generic mesages
    GenericError = "You tried that, but nothing happens"

    WrongThingToDo = "That's the wrong thing to do"

    DebugError = "The logic is hecka funked"

    Help = "You ask for help, but you wont even help yourself"

    EndGame = "You broke the mirror, freed the squid and now you win"

    RepeatRiddle = "You asked fo rthe riddle again. You would be lucky"
    
    # Octopus messages

    Octopus_OctopusAlreadyReleased = "The Octopus has already been released."

    Octopus_ExprienceTheBeach = "You hear waves crashing and the squawk of a seagull."

    Octopus_ReleaseOctopusBecomeBeach = "Sand appears at your feat, you hear a sea breeze and waves crashing."

    Octopus_NoReturningTheOctopus = "You can't put the octopus back."

    Octopus_ReturnTheOctopus = "A demonic voice congratulate you on returning the octopus."

    Octopus_AquariumShatters = "The glass shatters into millions of tiny shards, the cuts sting your hands."