'''A sql and python program that can:
List countries based on road rules with a advanced filtering system'''
# import required libraries
import sqlite3
import os
import time

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

# establish connection to country.db database
connection = sqlite3.connect("country.db")
cursor = connection.cursor()


# clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# check if order input is valid
def order_check(order_choice):
    valid_order = ["I", "N", "D", "A"]
    return order_choice in valid_order


# check if style input is valid
def style_check(style_choice):
    valid_style = ["F", "S"]
    return style_choice in valid_style


# check if style input is valid
def filter_check(filter_choice):
    valid_filter = ["L", "R", "A"]
    return filter_choice in valid_filter


# check if style input is valid
def choice_check(choice_input):
    if choice_input.upper() == "L" or choice_input.upper() == "S":
        return True
    else:
        return False


while True:
    clear()
    print("Press \033[1;46m L \033[0m to list all countries\n")
    print("Press \033[1;46m S \033[0m to show statistics\n")
    choice = input("").upper()
    while not choice_check(choice):
        print("\n\n\033[1;31mInvalid input.\033[0m\n\n")

        print("Press \033[1;46m L \033[0m to list all countries\n")
        print("Press \033[1;46m S \033[0m to show statistics\n")
        choice = input("").upper()

    # --- Show Statistics ---
    if choice == "S":

        # retrieve information
        avg_min_licence = cursor.execute("SELECT AVG(min_licence_age) FROM country").fetchall()
        left_count = cursor.execute("SELECT COUNT(*) FROM country WHERE left_side=1").fetchall()
        right_count = cursor.execute("SELECT COUNT(*) FROM country WHERE left_side=0").fetchall()
        country_count = cursor.execute("SELECT COUNT(*) FROM country").fetchall()
        last_updated = "20th of May 2025"

        # print information
        print(f"\n\n\033[1mAverage Minimum Driving Age:\033[0m \033[100m {avg_min_licence[0][0]} \033[0m")
        print(f"\033[1mLeft\033[0m - \033[100m {left_count[0][0]} \033[0m | \033[1mRight\033[0m - \033[100m {right_count[0][0]} \033[0m")
        print(f"\033[1mNumber of Countries in the Database:\033[0m \033[100m {country_count[0][0]} \033[0m")
        # print(f"Minimum Licence Distribution: \n16 - {} countries | 17 - {} countries | 18 - {} countries")
        print(f"\033[1mLast Updated:\033[0m \033[100m {last_updated} \033[0m")

        # Main menu return
        input("\n\nPress \033[1;46m Enter \033[0m to return to the main menu...\n")

    # --- List all countries ---
    elif choice == "L":

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
        order_input = input("ID: \033[1;46m I \033[0m | Name: \033[1;46m N \033[0m | Driving Side: \033[1;46m D \033[0m | Alcohol Limit: \033[1;46m A \033[0m\n").upper()
        while not order_check(order_input):
            print("\n\n\033[1;31mInvalid input. Please input either \033[1;46m I \033[0m\033[1;31m, \033[1;46m N \033[0m\033[1;31m, \033[1;46m D \033[0m\033[1;31m or \033[1;46m A \033[0m\n")
            print("\nWhat do you want the list ordered by?")
            order_input = input("ID: \033[1;46m I \033[0m | Name: \033[1;46m N \033[0m | Driving Side: \033[1;46m D \033[0m | Alcohol Limit: \033[1;46m A \033[0m\n").upper()

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
        elif order_input == "A":
            order = "alcohol"
        else:
            order = "left_side"

        # --- Filter System ---
        # connecting with traffic_rules.db database
        if order == "alcohol":
            header = ['\033[1mCOUNTRY ID\033[0m', '\033[1mCOUNTRY CODE\033[0m', '\033[1mNAME\033[0m', '\033[1mLEFT SIDE\033[0m', '\033[1mMIN DRIVING AGE\033[0m', '\033[1mRULE NAME\033[0m', '\033[1mRULE VALUE\033[0m']
            cursor.execute("SELECT c.*, rr.rule_name, rr.rule_value FROM country c JOIN traffic_rules rr ON c.country_id = rr.country_id WHERE rr.rule_name = 'Alcohol Limit' ORDER BY CAST(rr.rule_value AS FLOAT) ASC;")
            output = cursor.fetchall()
            formatted_rows = [(id, code, name, 'Left' if side else 'Right', age, rule_name, rule_value) for id, code, name, side, age, rule_name, rule_value in output]

        # when only connecting to country.db
        else:
            header = ['\033[1mCOUNTRY ID\033[0m', '\033[1mCOUNTRY CODE\033[0m', '\033[1mNAME\033[0m', '\033[1mLEFT SIDE\033[0m', '\033[1mMIN DRIVING AGE\033[0m']
            if filter_setting is False:
                cursor.execute(f"SELECT * FROM country ORDER BY {order}")

            else:
                data = [filter]
                cursor.execute(f"SELECT * FROM country WHERE left_side = ? ORDER BY {order}", data)

            output = cursor.fetchall()
            formatted_rows = [(id, code, name, 'Left' if side else 'Right', age) for id, code, name, side, age in output]

        # loading screen to allow time for processing what is happening
        clear()
        print("\n\n\033[1;42m Loading. \033[0m\n\n")
        time.sleep(0.2)
        clear()
        print("\n\n\033[1;42m Loading.. \033[0m\n\n")
        time.sleep(0.2)
        clear()
        print("\n\n\033[1;42m Loading... \033[0m\n\n")
        time.sleep(0.2)

        # print data (either fancy or simple)
        if style.lower() == "f":
            print(tabulate(formatted_rows, headers=header, tablefmt="fancy_grid"))
        else:
            print(tabulate(formatted_rows, headers=header))

        # main menu return
        input("\n\nPress \033[1;46m Enter \033[0m to return to the main menu...\n")

    # stop when nothing is inputed
