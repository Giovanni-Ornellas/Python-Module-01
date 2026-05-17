#!/usr/bin/env python3

# ****************************************************************************
#
#    ft_garden_security.py
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
        print(f"Plant created: {self.name}: "
              f"{self.get_height():.1f}cm, {self.get_age()} days old\n")

    def show(self) -> None:
        print(f"\nCurrent state: {self.name}: "
              f"{self.get_height():.1f}cm, {self.get_age()} days old")

    def _set_height(self, height: float) -> None:
        if height < 0:
            return
        self._height = height

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"\n{self.name}: Error, height can't be negative")
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
            print(f"\n{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._current_age = new_age
        print(f"Age updated: {self.get_age()} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._current_age


def main() -> None:
    print("=== Garden Security System ===")
    plant: Plant = Plant("Rose", 15, 10)

    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-10)
    plant.set_age(-20)
    plant.show()


if __name__ == "__main__":
    main()
