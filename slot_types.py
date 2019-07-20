import enum

class Door(enum.Enum):
    """
    Enum represeting what door the the player has tried to enter
    """
    first = 1
    second = 2

class Room(enum.Enum):
    """
    Enum represeting what room the player is in currently
    """
    lobby = 1
    octopus = 2
    mirror = 3