'''A sql and python program that can:
List countries based on road rules with a advanced filtering system'''
# import required libraries
import sqlite3
import os

# import tabulate library (table formatting)
import subprocess
import sys

try:
    # Try importing tabulate
    from tabulate import tabulate
except ImportError:
    # If not installed, prompt to install
    print("Installing 'tabulate'...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tabulate"])
    print("'tabulate' installed successfully. Please restart the program.")
    sys.exit()
header = ['\033[1mID\033[0m', '\033[1mCOUNTRY CODE\033[0m', '\033[1mNAME\033[0m', '\033[1mLEFT SIDE\033[0m', '\033[1mMIN DRIVING AGE\033[0m']

# establish connection to country.db database
connection = sqlite3.connect("country.db")
cursor = connection.cursor()


# clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# check if order input is valid
def order_check(order_key):
    if order_key.upper() == "I" or order_key.upper() == "N" or order_key.upper() == "D":
        return True
    else:
        return False


# check if style input is valid
def style_check(style_choice):
    if style_choice.upper() == "F" or style_choice.upper() == "S":
        return True
    else:
        return False


# check if style input is valid
def filter_check(filter_choice):
    if filter_choice.upper() == "L" or filter_choice.upper() == "R" or filter_choice.upper() == "A":
        return True
    else:
        return False


while True:
    clear()
    print("Press \033[1;46m L \033[0m to list all countries\n")
    choice = input("").upper()


# List all countries
    if choice == "L":

        # get filter
        print("\n\nWhat do you want to filter by?")
        filter_input = input("Only Include: \nLeft Side Driving: \033[1;46m L \033[0m | Right Side Driving: \033[1;46m R \033[0m | All: \033[1;46m A \033[0m\n").upper()
        while not filter_check(filter_input):
            print("\n\n\033[1;31mInvalid input. Please input either \033[1;46m L \033[0m \033[1;31mor \033[1;46m R \033[0m \033[1;31mor \033[1;46m A \033[0m\n")

            print("\nWhat do you want to filter by?")
            filter_input = input("Only Include: \nLeft Side Driving: \033[1;46m L \033[0m | Right Side Driving: \033[1;46m R \033[0m | All: \033[1;46m A \033[0m\n").upper()

        # get style
        print("\n\nWhat style do you want the information in?")
        style = input("Fancy: \033[1;46m F \033[0m | Simple: \033[1;46m S \033[0m\n").upper()
        while not style_check(style):
            print("\n\n\033[1;31mInvalid input. Please input either \033[1;46m F \033[0m \033[1;31mor \033[1;46m S \033[0m\n")

            print("\nWhat style do you want the information in?")
            style = input("Fancy: \033[1;46m F \033[0m | Simple: \033[1;46m S \033[0m\n").upper()

        # get order
        print("\n\nWhat do you want the list ordered by?")
        order_input = input("ID: \033[1;46m I \033[0m | Name: \033[1;46m N \033[0m | Driving Side: \033[1;46m D \033[0m\n").upper()
        while not order_check(order_input):
            print("\n\n\033[1;31mInvalid input. Please input either \033[1;46m I \033[0m\033[1;31m, \033[1;46m N \033[0m\033[1;31m, or \033[1;46m D \033[0m\n")
            print("\nWhat do you want the list ordered by?")
            order_input = input("ID: \033[1;46m I \033[0m | Name: \033[1;46m N \033[0m | Driving Side: \033[1;46m D \033[0m\n").upper()

        print("\n\n")

        # change filtering to inputed order
        if filter_input == "L":
            filter_setting = True
            filter = "1"
        elif filter_input == "R":
            filter_setting = True
            filter = "0"
        else:
            filter_setting = False

        # change ordering to inputed order
        if order_input == "I":
            order = "country_id"
        elif order_input == "N":
            order = "country_name"
        else:
            order = "left_side"

        # Filter System
        if filter_setting is False:
            data = [order]
            cursor.execute("SELECT * FROM country ORDER BY ?", data)
        else:
            data = [filter, order]
            cursor.execute("SELECT * FROM country WHERE left_side = ? ORDER BY ?", data)
        output = cursor.fetchall()

        formatted_rows = [(id, code, name, 'Left' if side else 'Right', age) for id, code, name, side, age in output]

        # Print Data
        if style.lower() == "f":
            print(tabulate(formatted_rows, headers=header, tablefmt="fancy_grid"))
        else:
            print(tabulate(formatted_rows, headers=header))

        input("\n\nPress \033[1;46m Enter \033[0m to return to the main menu...")

    # Stop when nothing is inputed
