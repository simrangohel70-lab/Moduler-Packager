import datetime
import time
import math
import random
import uuid

from Packages.math_utils import compound_interest
from Packages.file_utils import write_file, read_file, append_file


def datetime_menu():

    while True:

        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between dates")
        print("3. Stopwatch")
        print("4. Back")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            now = datetime.datetime.now()
            print("\nCurrent Date and Time:",
                  now.strftime("%Y-%m-%d %H:%M:%S"))

        elif ch == 2:
            d1 = input("Enter first date (YYYY-MM-DD): ")
            d2 = input("Enter second date (YYYY-MM-DD): ")

            date1 = datetime.datetime.strptime(d1,"%Y-%m-%d")
            date2 = datetime.datetime.strptime(d2,"%Y-%m-%d")

            diff = abs((date2-date1).days)

            print("Difference:",diff,"days")

        elif ch == 3:

            input("Press Enter to Start")
            start=time.time()

            input("Press Enter to Stop")
            end=time.time()

            print("Elapsed Time:",
                  round(end-start,2),"seconds")

        elif ch==4:
            break


def math_menu():

    while True:

        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Compound Interest")
        print("3. Trigonometry")
        print("4. Back")

        ch=int(input("Enter choice: "))

        if ch==1:

            num=int(input("Enter number: "))
            print("Factorial:",
                  math.factorial(num))

        elif ch==2:

            p=float(input("Principal: "))
            r=float(input("Rate: "))
            t=float(input("Time: "))

            print("Compound Interest:",
                  compound_interest(p,r,t))

        elif ch==3:

            angle=int(input("Enter angle: "))

            print("Sin:",
                  math.sin(math.radians(angle)))

        elif ch==4:
            break


def random_menu():

    while True:

        print("\nRandom Data Generation:")
        print("1. Random Number")
        print("2. Password")
        print("3. OTP")
        print("4. Back")

        ch=int(input("Enter choice: "))

        if ch==1:

            print("Random Number:",
                  random.randint(1,100))

        elif ch==2:

            password="".join(
                random.choices(
                    "abcdefghijklmnopqrstuvwxyz123456789",
                    k=8
                )
            )

            print("Generated Password:",
                  password)

        elif ch==3:

            print("OTP:",
                  random.randint(1000,9999))

        elif ch==4:
            break


def generate_uuid():

    unique_id=uuid.uuid4()

    print("\nGenerated UUID:")
    print(unique_id)


def file_menu():

    while True:

        print("\nFile Operations:")
        print("1.Write")
        print("2.Read")
        print("3.Append")
        print("4.Back")

        ch=int(input("Choice:"))

        filename="sample.txt"

        if ch==1:

            text=input("Enter text:")
            write_file(filename,text)

        elif ch==2:

            read_file(filename)

        elif ch==3:

            text=input("Enter text:")
            append_file(filename,text)

        elif ch==4:
            break

def explore():

    module=input(
        "Enter module (math/random): "
    )

    if module=="math":
        print(dir(math))

    elif module=="random":
        print(dir(random))


# Main Menu
while True:

    print("\n========================")
    print("Welcome to Multi Utility Toolkit")
    print("========================")

    print("1. Datetime Operations")
    print("2. Mathematical Operations")
    print("3. Random Data")
    print("4. Generate UUID")
    print("5. File Operations")
    print("6. Explore Module")
    print("7. Exit")

    choice=int(input("Enter choice: "))

    if choice==1:
        datetime_menu()

    elif choice==2:
        math_menu()

    elif choice==3:
        random_menu()

    elif choice==4:
        generate_uuid()

    elif choice==5:
        file_menu()

    elif choice==6:
        explore()

    elif choice==7:

        print("Thank you for using Multi Utility Toolkit")
        break