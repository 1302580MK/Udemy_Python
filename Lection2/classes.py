# 30.05.2019

# learn how to use classes

class Vehicle:
    speed = 0
    
    # ctor
    #def __new__(cls):
    #    return object.__new__(cls)

    def __init__(self, speed = 0):
        self.speed = speed
        print(f"Init speed with {self.speed}")

    def IncreaseSpeed(self, increaseAmount):
        self.speed += increaseAmount
    
    def __del__(self):
        print("Object has been destroyed")

car1 = Vehicle()
car2 = Vehicle()

car1.speed = 10

print(car1.speed)
print(car2.speed)

car2.IncreaseSpeed(13)
print(f"blub: {car2.speed}")

# destroy an object
del car2
print("test")