from abc import ABC, abstractmethod


class Animal(ABC): #(ABC) Built-in abstract class
    @abstractmethod
    def sound(self):
        pass
    def eat(self):
        print("animal eats")

class Cat(Animal):
    def sound(self):
        print("meow meow")
c1=Cat()
c1.sound()
c1.eat()