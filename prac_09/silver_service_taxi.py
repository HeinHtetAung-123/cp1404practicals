from taxi import Taxi
class SilverServiceTaxi(Taxi):
    flag_fall = 4.50

    def __init__(self,name,fuel,fanciness):
        """Initializing the class with the name and fuel"""
        super().__init__(name,fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km*fanciness

    def get_fare(self):
        """Get the fare from the parent class"""
        fare=super().get_fare()
        return round(fare+self.flag_fall,1)

    def __str__(self):
        """Inheriting the string output from the parent class"""
        base_string=super().__str__()
        return f"{base_string}, ${self.price_per_km:.2f}/km plus flag fall of ${self.flag_fall:.2f}"
