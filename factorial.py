#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Sep 2020
# This program calculates the sum of sequential numbers starting at 0


def main():
    # this function uses a loop

    # this is to keep track of the loop and calculate the sum
    loop_counter = 1
    total = 1

    # input
    user_input_as_string = input("Enter a positive integer : ")

    # process & output
    try:
        user_input = int(user_input_as_string)
        if user_input >= 0:
            while loop_counter <= user_input:
                total = total * loop_counter
                loop_counter = loop_counter + 1
            else:
                print("{0}! = {1}".format(user_input, total))
        else:
            print("Negative integer entered, please try again.")
    except Exception:
        print("Invalid integer entered, please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
