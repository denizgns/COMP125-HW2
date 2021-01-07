"""
Student Name:Deniz Güneş
File: hailstone.py
-----------------------
This function should implement a console program that simulates
the execution of the Hailstone sequence, as defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Homework 2 Handout.
"""
import math
def Hailstone(a):
    counter = 0
    while a != 1:
        if (a % 2) == 0:
            a_new = a // 2
            print(a, "is even, so I take half:", a_new)
            a = a_new
            counter += 1
        elif (a % 2) == 1:
            a_new = (3 * a) + 1
            print(a, "is odd, so I make 3n + 1:", a_new)
            a = a_new
            counter += 1
    print("This process took", counter, "step(s) to reach 1")

def main():
    """
    Replace this comment with a more descriptive one.
    Don't forget to delete the pass statement below.
    """
    a = input("Enter a number")
    Hailstone(int(a))



if __name__ == "__main__":
    main()
