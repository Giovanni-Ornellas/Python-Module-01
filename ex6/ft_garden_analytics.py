#!/usr/bin/env python3

# ****************************************************************************
#
#    ft_garden_analytics.py
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
        self.stats: Plant.Statisticts = self.Statisticts(name)
        self._set_height(height)
        self._set_age(current_age)

    def show(self) -> None:
        self.stats.show_calls()
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
        self.stats.grow_calls()
        if day % 2 == 0:
            self._height += 42
        else:
            self._height += 39

    def age(self, day: int) -> None:
        self.stats.age_calls()
        self._current_age += day

    @staticmethod
    def check_age(day: int) -> None:
        if day > 365:
            print(f"Is {day} days more than a year? -> True")
        else:
            print(f"Is {day} days more than a year? -> False")

    @classmethod
    def anonymous_plant(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)

    class Statisticts:
        def __init__(self,
                     name: str,
                     count_grow: int = 0,
                     count_age: int = 0,
                     count_shows: int = 0,
                     ) -> None:
            self.name = name
            self.count_grow = count_grow
            self.count_age = count_age
            self.count_shows = count_shows

        def grow_calls(self) -> None:
            self.count_grow += 1

        def age_calls(self) -> None:
            self.count_age += 1

        def show_calls(self) -> None:
            self.count_shows += 1

        def display(self) -> None:
            print(f"[statistics for {self.name.capitalize()}]")
            print(f"Stats: {self.count_grow} grow, "
                  f"{self.count_age} age, {self.count_shows} show")


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

    def bloom(self, day: int) -> None:
        print(f" {self.name.capitalize()} has not bloomed yet")
        self.stats.display()
        print(f"[asking the {self.name} to grow and bloom]")
        self.grow(day)
        self.show()
        print(f" {self.name.capitalize()} is blooming beautifully!")
        self.stats.display()


class Tree(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 current_age: int,
                 trunk_diameter: float
                 ) -> None:
        super().__init__(name, height, current_age)
        self.trunk_diameter = trunk_diameter
        self.stats: Tree.TreeStatistics = self.TreeStatistics(name)

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")
        self.stats.display()

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name.capitalize()} now produces a shade of "
              f"{self._height:.1f}cm long "
              f"and {self.trunk_diameter:.1f}cm wide.")
        self.stats.shade_calls()
        self.stats.display()

    class TreeStatistics(Plant.Statisticts):
        def __init__(self,
                     name: str,
                     count_grow: int = 0,
                     count_age: int = 0,
                     count_shows: int = 0,
                     count_shades: int = 0
                     ) -> None:
            super().__init__(name, count_grow, count_age, count_shows)
            self.count_shades = count_shades

        def shade_calls(self) -> None:
            self.count_shades += 1

        def display(self) -> None:
            super().display()
            print(f" {self.count_shades} shade")


class Seed(Flower):
    def __init__(self,
                 name: str,
                 height: float,
                 current_age: int,
                 color: str,
                 seeds: int = 0
                 ) -> None:
        super().__init__(name, height, current_age, color)
        self.seeds = seeds

    def show(self) -> None:
        super().show()
        print(f" {self.name.capitalize()} has not bloomed yet")
        print(f" Seeds: {self.seeds}")

    def bloom(self, day: int) -> None:
        print(f"[make {self.name} grow, age and bloom]")
        self.grow(day)
        self.age(day)
        self.seeds = 42
        super().show()
        print(f" {self.name.capitalize()} is blooming beautifully!")
        print(f" Seeds: {self.seeds}")
        self.stats.display()


def main() -> None:
    flower: Flower = Flower("rose", 15, 10, "red")
    tree: Tree = Tree("oak", 200, 365, 5)
    seed: Seed = Seed("sunflower", 80, 45, "yellow", 0)
    anonymous: Plant = Plant.anonymous_plant()

    print("=== Garden statistics ===")

    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)

    print("\n=== Flower")
    flower.show()
    flower.bloom(10)

    print("\n=== Tree")
    tree.show()
    tree.produce_shade()

    print("\n=== Seed")
    seed.show()
    seed.bloom(20)

    print("\n=== Anonymous")
    anonymous.show()
    anonymous.stats.display()


if __name__ == "__main__":
    main()
