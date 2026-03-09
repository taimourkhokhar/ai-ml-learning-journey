class Car:
    def __init__(self, make, model, year, speed=0):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print(f"Accelerating... Current speed: {self.speed}")

    def brake(self):
        self.speed = max(0, self.speed - 5)
        print(f"Braking Current speed: {self.speed}")

    def display(self):
        print(f"Car Info")
        print(f"{self.year} {self.make} {self.model}")
        print(f"Current Speed: {self.speed} km/h\n")


car1 = Car("Tesla", "Model 3", 2024)
car2 = Car("Ford", "Mustang", 1969)

car1.accelerate()
car1.accelerate()
car1.display()

car2.accelerate()
car2.brake()
car2.display()
