#!/usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Nov 2019
# This program uses a for loop


def main():
    counter = 0

    for numbers in range(1000, 2001):
        counter += 1
        print(numbers, end=(" " if counter < 5 else "\n"))

        if counter == 5:
            counter = 0


if __name__ == "__main__":
    main()
