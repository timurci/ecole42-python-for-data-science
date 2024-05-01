from abc import ABC, abstractmethod


class Character(ABC):
    """Character with several attributes"""
    def __init__(self, name, is_alive=True):
        """Initiate first name and alive state of the character"""
        self.first_name = name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Make it obvious the character is dead"""
        self.first_name += " (Dead)"


class Stark(Character):
    """Stark is a very distinguished character"""
    def die(self):
        """Change alive state of Stark to False"""
        self.is_alive = False
