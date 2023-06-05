# Appliance selection program (House Equipments)
# Page sound system
# Final Exam Stage
# Subject theme: Python OOP.TDD.Unit testing with unittest
# Version: 1.0
# Autor: Ilja
# Date: 05.06.2023

from entity.appliances import Appliances


# объявляем класс "Звуковая система"
class Sound_System(Appliances):
    def __init__(self, power=150, price=610):
        super().__init__(price)
        self.__power = power

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self):
        return self.__power

    def __str__(self):
        return (f"Sound system: power = {self.__power}, "
                f"money = ${self.price}")
