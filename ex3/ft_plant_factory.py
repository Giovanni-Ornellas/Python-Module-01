#!/usr/bin/env python3

# ****************************************************************************
#
#    ft_plant_factory.py
#
#    By: ganselmo <ganselmo@student.42.rio>
#
#    Created: 2026/05/17
#
# ****************************************************************************

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


def main() -> None:
    plant_01: Plant = Plant("Rose", 25.0, 30)
    plant_02: Plant = Plant("Oak", 200.0, 365)
    plant_03: Plant = Plant("Cactus", 5.0, 90)
    plant_04: Plant = Plant("Sunflower", 80.0, 45)
    plant_05: Plant = Plant("Fern", 15.0, 120)

    print("=== Plant Factory Output ===")
    print("Created: ", end="")
    plant_01.show()
    print("Created: ", end="")
    plant_02.show()
    print("Created: ", end="")
    plant_03.show()
    print("Created: ", end="")
    plant_04.show()
    print("Created: ", end="")
    plant_05.show()


if __name__ == "__main__":
    main()
