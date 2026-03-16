class Vehicle:
  def general_usage(self):
    print("General use: Transportation")

class Car(Vehicle):
  def __init__(self):
    print("I am car")
    self.wheels=4
    self.has_roof=True

  def specific_usage(self):
    print("specific use: commute to work , vacation with family")

class MotorCycle(Vehicle):
  def __init__(self):
    print("I am motorcycle")
    self.wheels=2
    self.has_roof=False
  def specific_usage(self):
    print("specific usage: for a relax ride")


c=Car()
c.general_usage()
m=MotorCycle()
m.general_usage()
print(isinstance(c,Car))
print(issubclass(Car,Vehicle))
