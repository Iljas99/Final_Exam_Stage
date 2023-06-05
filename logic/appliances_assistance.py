# Appliance selection program (House Equipments)
# Page appliances assistance
# Final Exam Stage
# Subject theme: Python OOP.TDD.Unit testing with unittest
# Version: 1.0
# Autor: Ilja
# Date: 05.06.2023


from entity.appliances import Appliances
from container.apartment import Apartment


# объявляем класс ассистента по подбору бытовой техники
class AppliancesAssistance:
    @staticmethod
    # задаем функцию по подбору бытовой техники по стоимости
    def calculate_total_price(apartment):
        # задаем условия
        if isinstance(apartment, Apartment) and apartment.size != 0:
            total = 0
            for i in range(apartment.size):
                appliances = apartment.get_appliances(i)

                if isinstance(appliances, Appliances):
                    total += appliances.price

            return total
        else:
            return 0

    # задаем функцию по подбору бытовой техники по мощности
    def calculate_total_power(apartment):
        # задаем условия
        if isinstance(apartment, Apartment) and apartment.size != 0:
            total = 0
            for i in range(apartment.size):
                appliances = apartment.get_appliances(i)

                if isinstance(appliances, Appliances):
                    total += appliances.power

            return total
        else:
            return 0
