#!/usr/bin/env Python3

# ****************************************************************************
#
#    ft_garden_date.py
#
#    By: ganselmo <ganselmo@student.42.rio>
#
#    Created: 2026/05/16
#
# ****************************************************************************

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    plant_01: Plant = Plant("Rose", 25, 30)
    plant_02: Plant = Plant("Sunflower", 80, 45)
    plant_03: Plant = Plant("Cactus", 15, 120)

    plant_01.show()
    plant_02.show()
    plant_03.show()


if __name__ == "__main__":
    main()
