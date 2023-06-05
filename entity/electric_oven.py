# Appliance selection program (House Equipments)
# Page electric oven
# Final Exam Stage
# Subject theme: Python OOP.TDD.Unit testing with unittest
# Version: 1.0
# Autor: Ilja
# Date: 05.06.2023

from entity.appliances import Appliances


# объявляем класс "Электрическая духовка"
class ElectricOven(Appliances):
    def __init__(self, power=1000, price=750):
        super().__init__(price)
        self.__power = power

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self):
        return self.__power

    def __str__(self):
        return (f"Electric oven: power = {self.__power}, "
                f"money = ${self.price}")
