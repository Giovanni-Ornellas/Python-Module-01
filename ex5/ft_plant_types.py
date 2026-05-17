#!/usr/bin/env python3

# ****************************************************************************
#
#    ft_plant_types.py
#
#    By: ganselmo <ganselmo@student.42.rio>
#
#    Created: 2026/05/17
#
# ****************************************************************************

class Plant:
    def __init__(self,
                 name: str,
                 height: float,
                 current_age: int
                 ) -> None:
        self.name = name
        self._height: float = 0
        self._current_age: int = 0

        self._set_height(height)
        self._set_age(current_age)

    def show(self) -> None:
        print(f"{self.name.capitalize()}: "
              f"{self.get_height():.1f}cm, {self.get_age()} days old")

    def _set_height(self, height: float) -> None:
        if height < 0:
            return
        self._height = height

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"\n{self.name.capitalize()}: "
                  f"Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = new_height
        print(f"Height updated: {self.get_height():.1f}cm")

    def _set_age(self, age: int) -> None:
        if age < 0:
            return
        self._current_age = age

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"\n{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._current_age = new_age
        print(f"Age updated: {self.get_age()} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._current_age

    def grow(self, day: int) -> None:
        if day % 2 == 0:
            self._height += 42
        else:
            self._height += 39

    def age(self, day: int) -> None:
        self._current_age += day


class Flower(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 current_age: int,
                 color: str
                 ) -> None:
        super().__init__(name, height, current_age)
        self.color = color

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")

    def bloom(self) -> None:
        print(f" {self.name.capitalize()} has not bloomed yet")
        print(f"[asking the {self.name} to bloom]")
        self.show()
        print(f" {self.name.capitalize()} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 current_age: int,
                 trunk_diameter: float
                 ) -> None:
        super().__init__(name, height, current_age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name.capitalize()} now produces a shade of "
              f"{self._height:.1f}cm long "
              f"and {self.trunk_diameter:.1f}cm wide.\n")


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 current_age: int,
                 harvest_season: str,
                 nutritional_value: int
                 ):
        super().__init__(name, height, current_age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def nutritional_update(self, days: int) -> None:
        super().age(days)
        super().grow(days)
        self.nutritional_value += days
        print(f"[make {self.name} grow and age for {days} days]")
        self.show()


def main() -> None:
    flower: Flower = Flower("rose", 15, 10, "red")
    tree: Tree = Tree("oak", 200, 365, 5)
    vegetable: Vegetable = Vegetable("tomato", 5, 10, "April", 0)

    print("== Garden Plant Types ===")

    print("=== Flower")
    flower.show()
    flower.bloom()

    print("=== Tree")
    tree.show()
    tree.produce_shade()

    print("=== Vegetable")
    vegetable.show()
    vegetable.nutritional_update(20)


if __name__ == "__main__":
    main()
