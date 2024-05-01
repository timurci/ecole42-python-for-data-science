from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King"""
    def __init__(self, *args, **kwargs):
        """Initialize a King"""
        # Calling __init__ from the first parent
        super().__init__(*args, **kwargs)

    def get_eyes(self):
        """Return eye color"""
        return self.eyes

    def set_eyes(self, eyes):
        """Set eye color"""
        self.eyes = eyes

    def get_hairs(self):
        """Get hair color"""
        return self.hairs

    def set_hairs(self, hairs):
        """Set hair color"""
        self.hairs = hairs
