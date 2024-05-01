from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon Family"""
    def __init__(self, first_name, is_alive=True):
        """Initialize the Baratheon"""
        self.first_name = first_name
        self.family_name = "Baratheon"
        self.is_alive = is_alive
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Baratheon passes away"""
        self.is_alive = False

    def __str__(self):
        """Return the name of Baratheon"""
        return self.first_name + " " + self.family_name

    def __repr__(self):
        """List all the attributes of Baratheon"""
        classname = self.__class__.__name__
        attributes = ""
        for key, value in self.__dict__.items():
            attributes += "\n\t{:<15} : ".format(key) + str(value)
        return classname + "(" + attributes + ")"


class Lannister(Character):
    """Representing the Lannister Family"""
    def __init__(self, first_name, is_alive=True):
        """Initialize the Lannister"""
        self.first_name = first_name
        self.family_name = "Lannister"
        self.is_alive = is_alive
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Lennister passes away"""
        self.is_alive = False

    def __str__(self):
        """Return the name of Lannister"""
        return self.first_name + " " + self.family_name

    def __repr__(self):
        """List all the attributes of Lannister"""
        classname = self.__class__.__name__
        attributes = ""
        for key, value in self.__dict__.items():
            attributes += "\n\t{:<15} : ".format(key) + str(value)
        return classname + "(" + attributes + ")"

    @staticmethod
    def create_lannister(*args, **kwargs):
        """Create Lannister in case you don't fancy calling the constructor"""
        return Lannister(*args, **kwargs)
