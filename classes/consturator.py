#
class Car:
    def __init__(self, brand, model, year=None):
        self.brand = brand
        self.model = model
        self.year = year if year else 2023  # Default to 2023 if year is None
    
    def details(self):
        print(f"{self.brand} {self.model}, Year: {self.year}")

# Creating instances
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic")  # Year defaults to 2023

car1.details()  # Output: Toyota Camry, Year: 2020
car2.details()  # Output: Honda Civic, Year: 2023