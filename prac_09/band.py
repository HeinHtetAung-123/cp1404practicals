class Band:
    def __init__(self,name=""):
        """Initializing this with  a name and an empty list of musicians"""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Adding a musician to the band"""
        self.musicians.append(musician)
        return self

    def __str__(self):
        """String Representation of the names and musicians separated by commas"""
        musicians_string = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_string})"

    def __repr__(self):
        """An actual representation of the string."""
        return str(vars(self))

    def play(self):
        """Simulating with this play method and returning the combined output"""
        return "\n".join(musician.play() for musician in self.musicians)


