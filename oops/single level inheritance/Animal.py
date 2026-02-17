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
dog1=Dog("meat","bark")
dog1.speak()

