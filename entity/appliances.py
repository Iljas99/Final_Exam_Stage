# Appliance selection program (House Equipments)
# Page appliances
# Final Exam Stage
# Subject theme: Python OOP.TDD.Unit testing with unittest
# Version: 1.0
# Autor: Ilja
# Date: 05.06.2023

# объявляем класс "Бытовая техника"
class Appliances:
    def __init__(self, price=0):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        # задаем условия стоимости
        if isinstance(price, (int, float)) and price > 0:
            self.__price = price

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        # задаем условия по мощности
        if isinstance(power, (int, float)) and power > 0:
            self.__power = power

