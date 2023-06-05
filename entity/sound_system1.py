# Appliance selection program (House Equipments)
# Page sound system 1
# Final Exam Stage
# Subject theme: Python OOP.TDD.Unit testing with unittest
# Version: 1.0
# Autor: Ilja
# Date: 05.06.2023

from entity.appliances import Appliances


# объявляем класс "Звуковая система 1"
class Sound_System1(Appliances):
    def __init__(self, power=250, price=760):
        super().__init__(price)
        self.__power = power

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self):
        return self.__power

    def __str__(self):
        return (f"Sound system 1: power = {self.__power}, "
                f"money = ${self.price}")
