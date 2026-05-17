#!/usr/bin/env python3

# ****************************************************************************
#
#    ft_plant_growth.py
#
#    By: ganselmo <ganselmo@student.42.rio>
#
#    Created: 2026/05/16
#
# ****************************************************************************

class Plant:
    def __init__(self, name: str, height: float, current_age: int) -> None:
        self.name = name
        self.height = height
        self.current_age = current_age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.current_age} days old")

    def grow(self, day: int) -> None:
        if day % 2 == 0:
            self.height += 1.6
        else:
            self.height += 1.9

    def age(self) -> None:
        self.current_age += 1


def main() -> None:
    plant: Plant = Plant("Rose", 25.0, 30)
    initial_height: float = plant.height

    print("=== Garden Plant Growth ===")
    plant.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow(day)
        plant.age()
        plant.show()
    total_growth = round((plant.height - initial_height), 1)
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    main()
