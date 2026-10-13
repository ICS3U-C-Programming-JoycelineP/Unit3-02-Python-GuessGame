#!/usr/bin/env python3
# Created by: Your Name
# Created on: Oct 2026
# This program asks the user to guess a number and checks if it is correct or not.

import constants


def main():
    # Get number from user between 0 and 9
    number = int(input("Enter a number between 0 and 9: "))

    # Check if number == correct answer
    if number == constants.CORRECT_ANSWER:

        # Display you are correct
        print("You are correct")

    # Check if number != correct answer
    if number != constants.CORRECT_ANSWER:

        # Display you are not correct
        print( "You are not correct. The correct answer is {}".format( constants.CORRECT_ANSWER ))


if __name__ == "__main__":
    main()
