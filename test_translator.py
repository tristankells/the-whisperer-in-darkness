from os.path import abspath
from audio import Audio

class Translator() :
    """
    Test translator for the whisperer in darkness. Contains shorter, more
    debug focussed test phrases.abspath
    """
    Launch = "welcome to the whisperer in darkness"
      
    # Enter door intent

    LeftDoor = "you enter the door on your left"
   
    RightDoor = "you enter the door on your right"
       
    DoorError = "You cant go through"

    # Investigate chains intent

    InvestigateChains = "The chains seemed tightly bound. You see a lock"

    ChainsError = "Not the time to investigate chains"

    # Use Key Intent

    UseKey = "You unlocked the chain, now you have acess to the tome "

    UseKeyError_NoKey = "Key? What key?"

    UseKeyError_WrongRoom = "Nothing to unlock right now "

    # Open book room intent 

    OpenBook = "You open the book. It screams at you"

    OpenBookError_ItsLocked = "The chains wrapped around it prevent you from opening the book"

    OpenBook_ThereNoBook = "I cant see no book"

    # Leave room intent 

    LeaveRoom = "You left the room back to the lobby"

    LeaveRoomError = "THere is no room to leave"
    
    # Leave room intent 
    ThrowBook = "You try to toss it, but you never seem to be able to muster the strength to get rid of it"

    ThrowBookError = "You try to throw it, but you dont have it"
    

