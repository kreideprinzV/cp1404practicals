class Band:
    """Band class for associating with Musicians."""

    def __init__(self, name=""):
        """Construct a Band with a name and empty collection of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band and its Musicians."""
        musician_strings = ', '.join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_strings})"

    def add(self, musician):
        """Add a Musician to the band's collection of musicians."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their instrument, or a message if they have none."""
        return '\n'.join(musician.play() for musician in self.musicians)
