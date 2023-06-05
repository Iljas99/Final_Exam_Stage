# Appliance selection program (House Equipments)
# Page jacuzzi
# Final Exam Stage
# Subject theme: Python OOP.TDD.Unit testing with unittest
# Version: 1.0
# Autor: Ilja
# Date: 05.06.2023

from entity.appliances import Appliances


# объявляем класс "Джакуззи"
class Jacuzzi(Appliances):
    def __init__(self, power=500, price=2300):
        super().__init__(price)
        self.__power = power

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self):
        return self.__power

    def __str__(self):
        return (f"Jacuzzi: power = {self.__power}, "
                f"money = ${self.price}")
