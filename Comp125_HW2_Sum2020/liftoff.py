"""
Student Name:Deniz Güneş
File: liftoff.py
--------------------
This file should define a simple program that displays
a rocket launch countdown as specified in the Assignment 2
handout.
"""
def countdown():
    for i in range(11):
        print(10-i)
def liftoff():
    print("liftoff")
def main():
    """
    Replace this comment with a more descriptive one.
    Don't forget to delete the pass statement below.
    """
    countdown()
    liftoff()


if __name__ == "__main__":
    main()

