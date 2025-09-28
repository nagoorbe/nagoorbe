#using built in methods

print(len("Hello"))    # 5  (length of string)
print(len([1, 2, 3]))  # 3  (length of list)
print(len({1: "a", 2: "b"}))  # 2  (length of dictionary)


#using  with operator overlaoding
print(10 + 20)       # 30  (addition of integers)
print("Hello " + "World")  # Hello World (string concatenation)
print([1, 2] + [3, 4])     # [1, 2, 3, 4] (list concatenation)


# using method overriding
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

# Using polymorphism
animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.speak()
