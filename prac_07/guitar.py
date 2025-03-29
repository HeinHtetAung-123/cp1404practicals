CURRENT_YEAR = 2024
VINTAGE_YEAR = 50
class Guitar:
    def __init__(self,name="", year=0,cost=0.0):
        """Initialize the constructor with the respective names, years, and costs of guitars."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Calling this method to print the result in a string format"""
        return f"{self.name},{self.year}, ${self.cost:,.2f}"

    def __repr__(self):
        """Calling this method to print the actual representation of the result"""
        return f"{self.name},{self.year}, ${self.cost:,.2f}"

    def get_age(self):
        """Calculating and returning the age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Returning True or False when the guitar is vintage or not """
        return self.get_age() >= VINTAGE_YEAR

    def __lt__(self, other):
        """Less than method to see the comparison between the years."""
        return self.year < other.year