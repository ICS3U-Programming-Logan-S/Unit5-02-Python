#!/usr/bin/env python3

# Created by: Logan S
# Created on: Jan. 21, 2022
# This program calculates the area of a triangle in functions.


def calculate_area(base, height):
    # calculate area

    # process
    area = (base * height) / 2

    # output
    print("The area is {0} cm²".format(area))


def main():
    # this function gets length and width

    # input
    base_from_user = float(input("Enter the base of a Triangle (cm): "))
    height_from_user = float(input("Enter the height of a Triangle (cm): "))
    print("")

    # Call the function
    calculate_area(base_from_user, height_from_user)


if __name__ == "__main__":
    main()
