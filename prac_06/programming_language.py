class ProgrammingLanguage:
    def __init__(self, name="", typing="",is_reflection=False,year=0):
        """Initialise the "ProgrammingLanguage" attributes"""
        self.name = name
        self.typing = typing
        self.is_reflection = is_reflection
        self.year = year
    def is_dynamic(self):
        """Returning the True when typing is dynamic"""
        return self.typing == "Dynamic"
    def __str__(self):
        """Return a formatted string representation of the object."""
        return f"{self.name},{self.typing} Typing ,Reflection={self.is_reflection},First Appeared in {self.year}"

