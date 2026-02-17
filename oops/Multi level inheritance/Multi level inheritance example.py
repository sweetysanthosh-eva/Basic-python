
class Animal:
    def __init__(self,sound):
        self.sound=sound
    def speak(self):
        print(self.sound)

class Dog(Animal):
    def __init__(self,food,sound):
        super().__init__(sound)
        self.food=food
    def speak(self):
        super().speak()
        print(self.food)

class puppy(Dog):
    def __init__(self,food,sound,walk):
        super().__init__(food,sound)
        self.walk=walk
    def weep(self):
        print("puppy weep")
        print(self.walk)

puppy1=puppy("cherry","bark","yes")
puppy1.weep()
puppy1.speak()


