# Appliance selection program (House Equipments)
# Page main
# Final Exam Stage
# Subject theme: Python OOP.TDD.Unit testing with unittest
# Version: 1.0
# Autor: Ilja
# Date: 05.06.2023

from entity.electric_kettle import ElectricKettle
from entity.electric_oven import ElectricOven
from entity.electrical_panel import ElectricalPanel
from entity.food_processor import FoodProcessor
from entity.fridge import Fridge
from entity.hair_dryer import HairDryer
from entity.jacuzzi import Jacuzzi
from entity.microwave import Microwave
from entity.personal_computer import PersonalComputer
from entity.personal_computer1 import PersonalComputer1
from entity.printer import Printer
from entity.sound_system import Sound_System
from entity.sound_system1 import Sound_System1
from entity.televisor import Televisor
from entity.televisor1 import Televisor1
from entity.washing_machine import WashingMachine

from container.apartment import Apartment
from logic.appliances_assistance import AppliancesAssistance


# задаем функцию
def main():
    apartment = Apartment()

    k = ElectricKettle()
    o = ElectricOven()
    p = ElectricalPanel()
    f = FoodProcessor()
    fr = Fridge()
    h = HairDryer()
    j = Jacuzzi()
    m = Microwave()
    pc = PersonalComputer()
    pc1 = PersonalComputer1()
    pr = Printer()
    s = Sound_System()
    s1 = Sound_System1()
    t = Televisor()
    t1 = Televisor1()
    w = WashingMachine()

    apartment.add(k)
    apartment.add(o)
    apartment.add(p)
    apartment.add(f)
    apartment.add(fr)
    apartment.add(h)
    apartment.add(j)
    apartment.add(m)
    apartment.add(pc)
    apartment.add(pc1)
    apartment.add(pr)
    apartment.add(s)
    apartment.add(s1)
    apartment.add(t)
    apartment.add(t1)
    apartment.add(w)

    print(apartment)

    total = AppliancesAssistance.calculate_total_price(apartment)
    total1 = AppliancesAssistance.calculate_total_power(apartment)


    print(f"Total price of all appliances - {total} $")
    print(f"Total power of all appliances - {total1} W")


if __name__ == "__main__":
    main()
