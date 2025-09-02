class Car:
    # Constructor
    def __init__(self, name, year):
        # Instance Attributes
        self.name = name
        self.year = year
        self.speed = 400
        self.miles = 0  # FIX 2: Initialized the attribute with a value
        print(f"Object created for: {self.name}")

    # Instance Method
    def get_description(self):
        return f"{self.name} from {self.year} has a top speed of {self.speed} km/h."
    
    # FIX 1: Renamed the method to avoid conflict with the attribute
    def update_miles(self, km):
        """Updates the miles driven."""
        if km >= 0:
            self.miles = km
        # This method is for updating data, so we can make it return nothing (or a confirmation)
        print(f"{self.name} has now driven {self.miles} miles.")

    # FIX 3: This is now a proper instance method (not static)
    def hmm(self):
        """A regular instance method that can access self."""
        print(f"This is the hmm method for {self.name}.")

# --- Using the corrected class ---

my_car = Car("Honda", 2002)
# Object created for: Honda

print(my_car.get_description())
# Honda from 2002 has a top speed of 400 km/h.

print(f"Initial miles: {my_car.miles}")
# Initial miles: 0

my_car.update_miles(80)
# Honda has now driven 80 miles.

print(f"Current miles: {my_car.miles}")
# Current miles: 80

my_car01 = Car("Skoda", 2007)
# Object created for: Skoda

my_car01.hmm()
# This is the hmm method for Skoda.