class Father:
    def skills(self):
        print("Father's skills are : football player")
class Mother:
    def skills(self):
        print("Mother's skills are : Artist")
class Child(Father, Mother):
    def skills(self):
        super().skills()
        print("Child skills are : Dancer")
child1 = Child()
child1.skills()
child1.Mother_skills()

