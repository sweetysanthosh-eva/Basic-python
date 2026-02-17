class Vehicle:
    def vehicle_details(self,wheels):
        print("Vehicle contains",wheels)
class Bike(Vehicle):
    def bike_details(self,wheels,model):
        super().vehicle_details(wheels)
        print("Bike model is",model)
bike1=Bike()
bike1.bike_details(2,"Honda")

class Car(Vehicle):
    def car_details(self,wheels,model):
        super().vehicle_details(wheels)
        print("Car model is",model)
car1=Car()
car1.car_details(4,"punch")