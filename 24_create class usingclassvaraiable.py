class Car:
    count = 0  

    def __init__(self, brand):
        self.brand = brand
        Car.count += 1

    @classmethod
    def total_cars(cls):
        return f"Total Cars Created = {cls.count}"

c1 = Car("Toyota")
c2 = Car("Honda")
print(Car.total_cars())
