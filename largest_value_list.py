#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Wed/Jun2/2021
# this program generates 10 random numbers between 1 and 100
# then calculates the average of the numbers and display it


import random


def largest_random_number(largest_number):

    largest = 0

    for counter in range(0, len(largest_number)):
        largest = largest_number[counter]

    return largest


def main():
    # this function uses an array
    random_number = []
    random_number.sort()
    # start
    print("Starting ...")
    print("\nHere is a list of random numbers:")
    # input
    for loop_counter in range(0, 10):
        random_ = random.randint(1, 100)
        random_number.append(random_)
        # output
        print(
            "\nThe random number {0} is: {1}"
            .format(loop_counter + 1, random_number[loop_counter]), end="")
    # output
    print("\n\nThe largest number is {0}".format(max(random_number)))
    print("\nDone.")


if __name__ == "__main__":
    main()
