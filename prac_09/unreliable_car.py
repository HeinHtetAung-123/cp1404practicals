import random
from car import Car
class UnreliableCar(Car):
    def __init__(self,name,fuel,reliability):
        """Initializing the class with fuel and name"""
        super().__init__(fuel,name)
        self.reliability = reliability

    def drive(self, distance):
        """Generating a random number between 0 and 100 and simulating the probability to drive"""
        random_number = random.randint(0,100)
        if random_number< self.reliability:
            return super().drive(distance)
        else:
            return 0