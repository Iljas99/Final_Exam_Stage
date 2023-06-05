# Appliance selection program (House Equipments)
# Page appliances assistance test
# Final Exam Stage
# Subject theme: Python OOP.TDD.Unit testing with unittest
# Version: 1.0
# Autor: Ilja
# Date: 05.06.2023

import unittest

from container.apartment import Apartment
from entity.appliances import Appliances
from logic.appliances_assistance import AppliancesAssistance


class AppliancesAssistanceTest(unittest.TestCase):
    def test_different_type(self):
        apartment = "string"
        expected = 0

        actual = AppliancesAssistance.calculate_total_price(apartment)

        self.assertEqual(expected, actual)

    def test_empty_apartment(self):
        apartment = Apartment()
        expected = 0

        actual = AppliancesAssistance.calculate_total_price(apartment)

        self.assertEqual(expected, actual)

    def test_apartment_with_None(self):
        apartment = None
        expected = 0

        actual = AppliancesAssistance.calculate_total_price(apartment)

        self.assertEqual(expected, actual)

    def test_apartment_with_appliances_positive(self):
        appliances1 = Appliances(5)
        appliances2 = Appliances(10)
        appliances3 = Appliances(3)

        apartment = Apartment()
        apartment.add(appliances1)
        apartment.add(appliances2)
        apartment.add(appliances3)

        expected = 18

        actual = AppliancesAssistance.calculate_total_price(apartment)

        self.assertEqual(expected, actual)

    def test_apartment_with_one_appliances(self):
        appliances = Appliances(1)

        apartment = Apartment()
        apartment.add(appliances)

        expected = appliances.price

        actual = AppliancesAssistance.calculate_total_price(apartment)

        self.assertEqual(expected, actual)

    def test_apartment_with_appliances_positive(self):
        appliances1 = Appliances(100)
        appliances2 = Appliances(200)
        appliances3 = Appliances(350)

        apartment = Apartment()
        apartment.add(appliances1)
        apartment.add("string")
        apartment.add(appliances2)
        apartment.add(appliances3)
        apartment.add(300)

        expected = 650
        actual = AppliancesAssistance.calculate_total_price(apartment)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
