#!/usr/bin/env python3

# ****************************************************************************
#
#    ft_garden_intro.py
#
#    By: ganselmo <ganselmo@student.42.rio>
#
#    Created: 2026/05/16
#
# ****************************************************************************

def ft_garden_intro() -> None:
    name: str = input("Plant: ")
    height: int = int(input("Height: "))
    age: int = int(input("Age: "))

    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")


if __name__ == "__main__":
    ft_garden_intro()
