# Appliance selection program (House Equipments)
# Page apartment
# Final Exam Stage
# Subject theme: Python OOP.TDD.Unit testing with unittest
# Version: 1.0
# Autor: Ilja
# Date: 05.06.2023

from entity.appliances import Appliances


# объявляем класс "Квартира"
class Apartment:
    def __init__(self, appliances=None):
        if appliances:
            self.__appliances = appliances
        else:
            self.__appliances = []

    @property
    def size(self):
        return len(self.__appliances)

    def get_appliances(self, index):
        if (isinstance(index, int)
                and index >= 0 and index < self.size):
            return self.__appliances[index]

    def add(self, appliances):
        if isinstance(appliances, Appliances):
            self.__appliances.append(appliances)

    def __str__(self):
        msg = "Household appliances list:"

        for i in range(self.size):
            msg += f"\n{i + 1}) " + str(self.__appliances[i])

        return msg
