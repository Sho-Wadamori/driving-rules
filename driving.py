"""
A SQL and python program that can:
- List countries based on road rules with an advanced filtering and ordering
- Search for a specific country
- Compare two countries based on their road rules
- Show statistics about the countries in the database
More information can be found on the GitHub repository README.md:
https://github.com/Sho-Wadamori/driving-rules?tab=readme-ov-file#readme
"""
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

# -------------------------- Configuration --------------------------
last_updated = "29th of May 2025"  # manually updated date that is used in stats
country_columns = (
    "country.country_code, country.country_name, country.left_side, country.min_licence_age, "
    "traffic_rules.rule_name, traffic_rules.rule_value FROM country "
    "JOIN traffic_rules ON country.country_id = traffic_rules.country_id"
)  # join query used in almost all SELECTs that doesn't use ID.
loading_time = 0.1


# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# check if order input is valid
def order_check(order_choice):
    valid_order = ["N", "M", "D", "A", "S"]
    return order_choice in valid_order


# check if style input is valid
def style_check(style_choice):
    valid_style = ["F", "S"]
    return style_choice in valid_style


# check if rule input is valid
def rule_check(rule_choice):
    valid_rule = ["A", "S"]
    return rule_choice in valid_rule


# check if country ID exists
def id_check(input_id):
    data = [input_id]
    cursor.execute("SELECT * FROM country WHERE country.country_id = ?;", data)
    found_countries = cursor.fetchall()

    # Check if country ID exists
    if found_countries:
        return True

    else:
        return False


# check if choice input is valid
def choice_check(choice_input):
    valid_choice = ["L", "F", "C", "S", "Q"]
    return choice_input in valid_choice


# title display
def display_header(title):
    clear()
    print("="*70)
    print("\033[1m{:^70}\033[0m".format(title))
    print("="*70)


# returns header text (without id)
def get_header():
    return ['\033[1mCOUNTRY CODE\033[0m', '\033[1mNAME\033[0m', '\033[1mDRIVING SIDE\033[0m', '\033[1mMIN DRIVING AGE\033[0m', '\033[1mRULE NAME\033[0m', '\033[1mRULE VALUE\033[0m']


# returns formatted rows (without id)
def get_format(data):
    return [(code, name, 'Left' if side else 'Right', age, rule_name, 'None' if rule_value == -1 else rule_value) for code, name, side, age, rule_name, rule_value in data]


# -------------------------- Main Menu Loop --------------------------
while True:
    # clear terminal and ask for what they want to do
    clear()
    print("Press \033[1;46m L \033[0m to list all countries\n")
    print("Press \033[1;46m F \033[0m to find a specific country\n")
    print("Press \033[1;46m C \033[0m to compare two countries\n")
    print("Press \033[1;46m S \033[0m to show statistics\n")
    print("Press \033[1;46m Q \033[0m to quit\n")
    choice = input("> ").upper().strip()

    # continue to ask question if invalid
    while not choice_check(choice):
        clear()
        print("\n\n\033[1;31mInvalid input.\033[0m\n\n")
        time.sleep(0.4)  # pause to show that there was an error
        clear()
        print("Press \033[1;46m L \033[0m to list all countries\n")
        print("Press \033[1;46m F \033[0m to find a specific country\n")
        print("Press \033[1;46m C \033[0m to compare two countries\n")
        print("Press \033[1;46m S \033[0m to show statistics\n")
        print("Press \033[1;46m Q \033[0m to quit\n")
        choice = input("> ").upper().strip()

    # -------------------------- Country Search --------------------------
    # find a country by country name or code
    if choice == "F":
        # display header title
        display_header(" COUNTRY SEARCH ")

        country_search = input("\nEnter the name of the country you want to find:\n> ").upper().strip()
        while not country_search:
            print("\n\n\033[1;31mCountry name cannot be empty.\033[0m\n")
            country_search = input("Enter the name of the country you want to find:\n> ").upper().strip()

        # ask what rule to display
        print("\n\nWhich traffic rule do you want to view?")
        rule_choice = input("Alcohol Limit: \033[1;46m A \033[0m | Max Speed: \033[1;46m S \033[0m\n> ").upper().strip()
        while not rule_check(rule_choice):
            print("\n\n\033[1;31mInvalid input. Please input either \033[1;46m A \033[0m \033[1;31mor \033[1;46m S \033[0m\n")

            print("\nWhich traffic rule do you want to view?")
            rule_choice = input("Alcohol Limit: \033[1;46m A \033[0m | Max Speed: \033[1;46m S \033[0m\n> ").upper().strip()

        # change rule_name to input
        if rule_choice == "A":
            rule_name = "Alcohol Limit"
        else:
            rule_name = "Max Speed"

        # loading screen to allow time for processing what is happening
        clear()
        print("\n\n\033[1;42m Loading. \033[0m\n\n")
        time.sleep(loading_time)
        clear()
        print("\n\n\033[1;42m Loading.. \033[0m\n\n")
        time.sleep(loading_time)
        clear()
        print("\n\n\033[1;42m Loading... \033[0m\n\n")
        time.sleep(loading_time)

        # search for inputed country
        data = ('%' + country_search + '%', '%' + country_search + '%', rule_name)
        cursor.execute(f"SELECT {country_columns} WHERE (UPPER(country.country_name) LIKE ? OR UPPER(country.country_code) LIKE ?) AND traffic_rules.rule_name = ?;", data)
        found_countries = cursor.fetchall()
        header = get_header()

        # print country data if found
        if found_countries:
            # display header title
            display_header(" COUNTRIES FOUND: ")

            formatted_rows = get_format(found_countries)
            print(tabulate(formatted_rows, headers=header))

        # error if no matching found
        else:
            print(f"\n\n\033[1;31mNo countries found matching: \033[100m {country_search} \033[0m.\n")

        # main menu return
        input("\n\nPress \033[1;46m Enter \033[0m to return to the main menu...\n")

    # -------------------------- Comparison Tool --------------------------
    # compares two country using country ids
    elif choice == "C":
        # display header title
        display_header(" COMPARISON TOOL ")

        # show the full table
        cursor.execute("SELECT * FROM country")
        output = cursor.fetchall()
        header = ['\033[1mCOUNTRY ID\033[0m', '\033[1mCOUNTRY CODE\033[0m', '\033[1mNAME\033[0m', '\033[1mDRIVING SIDE\033[0m', '\033[1mMIN DRIVING AGE\033[0m']
        formatted_rows = [(id, code, name, 'Left' if side else 'Right', age) for id, code, name, side, age in output]
        print(tabulate(formatted_rows, headers=header, tablefmt="fancy_grid"))

        # get id for first country
        compare_id_1 = input("\n\nEnter the country id of the first country you want to compare:\n> ").strip()
        while not id_check(compare_id_1):
            print(f"\n\n\033[1;31mNo countries found matching the id: \033[100m {compare_id_1} \033[0m.\n")
            compare_id_1 = input("\n\nEnter the country id of the first country you want to compare:\n> ").strip()

        # get id for second country
        compare_id_2 = input("\n\nEnter the country id of the second country you want to compare:\n> ").strip()
        while not id_check(compare_id_2):
            print(f"\n\n\033[1;31mNo countries found matching the id: \033[100m {compare_id_2} \033[0m.\n")
            compare_id_2 = input("\n\nEnter the country id of the second country you want to compare:\n> ").strip()

        # ask what rule to display
        print("\n\nWhich traffic rule do you want to view?")
        rule_choice = input("Alcohol Limit: \033[1;46m A \033[0m | Max Speed: \033[1;46m S \033[0m\n> ").upper().strip()
        while not rule_check(rule_choice):
            print("\n\n\033[1;31mInvalid input. Please input either \033[1;46m A \033[0m \033[1;31mor \033[1;46m S \033[0m\n")

            print("\nWhich traffic rule do you want to view?")
            rule_choice = input("Alcohol Limit: \033[1;46m A \033[0m | Max Speed: \033[1;46m S \033[0m\n> ").upper().strip()

        # change rule_name to input
        if rule_choice == "A":
            rule_name = "Alcohol Limit"
        else:
            rule_name = "Max Speed"

        # loading screen to allow time for processing what is happening
        clear()
        print("\n\n\033[1;42m Loading. \033[0m\n\n")
        time.sleep(loading_time)
        clear()
        print("\n\n\033[1;42m Loading.. \033[0m\n\n")
        time.sleep(loading_time)
        clear()
        print("\n\n\033[1;42m Loading... \033[0m\n\n")
        time.sleep(loading_time)

        # print the two countries
        data = [compare_id_1, compare_id_2, rule_name]
        cursor.execute("SELECT country.*, traffic_rules.rule_name, traffic_rules.rule_value FROM country JOIN traffic_rules ON country.country_id = traffic_rules.country_id WHERE (country.country_ID = ? OR country.country_ID = ?) AND rule_name = ?;", data)
        compare_results = cursor.fetchall()
        header = ['\033[1mCOUNTRY ID\033[0m', '\033[1mCOUNTRY CODE\033[0m', '\033[1mNAME\033[0m', '\033[1mDRIVING SIDE\033[0m', '\033[1mMIN DRIVING AGE\033[0m', '\033[1mRULE NAME\033[0m', '\033[1mRULE VALUE\033[0m']
        formatted_rows = [(id, code, name, 'Left' if side else 'Right', age, rule_name, 'None' if rule_value == -1 else rule_value) for id, code, name, side, age, rule_name, rule_value in compare_results]

        # display header title
        display_header(" RESULTS ")

        print(tabulate(formatted_rows, headers=header, tablefmt="fancy_grid"))

        # main menu return
        input("\n\nPress \033[1;46m Enter \033[0m to return to the main menu...\n")

    # -------------------------- Show Statistics --------------------------
    # shows general statistics for the databse
    elif choice == "S":
        # display header title
        display_header(" STATISTICS ")

        # retrieve information
        left_count = cursor.execute("SELECT COUNT(*) FROM country WHERE left_side=1").fetchall()
        right_count = cursor.execute("SELECT COUNT(*) FROM country WHERE left_side=0").fetchall()
        min_licence_count_14 = cursor.execute("SELECT COUNT(*) FROM country WHERE min_licence_age = 14").fetchall()
        min_licence_count_15 = cursor.execute("SELECT COUNT(*) FROM country WHERE min_licence_age = 15").fetchall()
        min_licence_count_16 = cursor.execute("SELECT COUNT(*) FROM country WHERE min_licence_age = 16").fetchall()
        min_licence_count_17 = cursor.execute("SELECT COUNT(*) FROM country WHERE min_licence_age = 17").fetchall()
        min_licence_count_18 = cursor.execute("SELECT COUNT(*) FROM country WHERE min_licence_age = 18").fetchall()
        min_licence_count_21 = cursor.execute("SELECT COUNT(*) FROM country WHERE min_licence_age = 21").fetchall()
        avg_min_licence = cursor.execute("SELECT AVG(min_licence_age) FROM country").fetchall()
        avg_alcohol_limit = cursor.execute("SELECT AVG(rule_value) FROM traffic_rules WHERE rule_name = 'Alcohol Limit' AND rule_value != -1").fetchall()
        avg_max_speed = cursor.execute("SELECT AVG(rule_value) FROM traffic_rules WHERE rule_name = 'Max Speed' AND rule_value != -1").fetchall()
        country_count = cursor.execute("SELECT COUNT(*) FROM country").fetchall()

        # print information
        print("Driving Side Distribution:")
        print(f"Left\033[0m - \033[100m {left_count[0][0]} \033[0m | Right\033[0m - \033[100m {right_count[0][0]} \033[0m\n")
        print("Minimum Licence Distribution: ")
        print(f"14yrs - \033[100m {min_licence_count_14[0][0]} countries \033[0m | 15yrs - \033[100m {min_licence_count_15[0][0]} countries \033[0m | 16yrs - \033[100m {min_licence_count_16[0][0]} countries \033[0m")
        print(f"17yrs - \033[100m {min_licence_count_17[0][0]} countries \033[0m | 18yrs - \033[100m {min_licence_count_18[0][0]} countries \033[0m | 21yrs - \033[100m {min_licence_count_21[0][0]} countries \033[0m")
        print(f"\nAverage Minimum Driving Age:\033[0m \033[100m {round(avg_min_licence[0][0], 2)} \033[0m")
        print(f"Average Alcohol Limit:\033[0m \033[100m {round(avg_alcohol_limit[0][0], 2)} \033[0m")
        print(f"Average Max Speed:\033[0m \033[100m {round(avg_max_speed[0][0], 2)} \033[0m")
        print(f"Number of Countries in the Database:\033[0m \033[100m {country_count[0][0]} \033[0m")
        print(f"Last Updated:\033[0m \033[100m {last_updated} \033[0m")

        # main menu return
        input("\n\nPress \033[1;46m Enter \033[0m to return to the main menu...\n")

    # -------------------------- List all countries --------------------------
    # lists all countries with a ordering and filtering tool
    elif choice == "L":
        # display header title
        display_header(" COUNTRY LIST ")

        # get filter
        print("What do you want to filter by?")
        filter_input = input("Only Include: \nLeft Side Driving: \033[1;46m L \033[0m | Right Side Driving: \033[1;46m R \033[0m | All: \033[1;46m A \033[0m\n> ").upper().strip()
        # check if filter input is valid (not function as only used once)
        valid_filter = ["L", "R", "A"]
        while filter_input not in valid_filter:
            print("\n\n\033[1;31mInvalid input. Please input either \033[1;46m L \033[0m \033[1;31mor \033[1;46m R \033[0m \033[1;31mor \033[1;46m A \033[0m\n")

            print("\nWhat do you want to filter by?")
            filter_input = input("Only Include: \nLeft Side Driving: \033[1;46m L \033[0m | Right Side Driving: \033[1;46m R \033[0m | All: \033[1;46m A \033[0m\n> ").upper().strip()

        # get style
        print("\n\nWhat style do you want the information in?")
        style = input("Fancy: \033[1;46m F \033[0m | Simple: \033[1;46m S \033[0m\n> ").upper().strip()
        while not style_check(style):
            print("\n\n\033[1;31mInvalid input. Please input either \033[1;46m F \033[0m \033[1;31mor \033[1;46m S \033[0m\n")

            print("\nWhat style do you want the information in?")
            style = input("Fancy: \033[1;46m F \033[0m | Simple: \033[1;46m S \033[0m\n> ").upper().strip()

        # get order
        print("\n\nWhat do you want the list ordered by?")
        order_input = input("Name: \033[1;46m N \033[0m | Driving Side: \033[1;46m D \033[0m | Minimum Licence Age: \033[1;46m M \033[0m | Alcohol Limit: \033[1;46m A \033[0m | Max Speed: \033[1;46m S \033[0m\n> ").upper().strip()
        while not order_check(order_input):
            print("\n\n\033[1;31mInvalid input. Please input either \033[1;46m N \033[0m\033[1;31m, \033[1;46m D \033[0m\033[1;31m, \033[1;46m M \033[0m\033[1;31m, \033[1;46m A \033[0m\033[1;31m or \033[1;46m S \033[0m\n")
            print("\nWhat do you want the list ordered by?")
            order_input = input("Name: \033[1;46m N \033[0m | Driving Side: \033[1;46m D \033[0m | Minimum Licence Age: \033[1;46m M \033[0m | Alcohol Limit: \033[1;46m A \033[0m | Max Speed: \033[1;46m S \033[0m\n> ").upper().strip()

        # ask for which rule to display if not ordered by rule
        if order_input != "A" and order_input != "S":
            # ask what rule to display
            print("\n\nWhich traffic rule do you want to view?")
            rule_choice = input("Alcohol Limit: \033[1;46m A \033[0m | Max Speed: \033[1;46m S \033[0m\n> ").upper().strip()
            while not rule_check(rule_choice):
                print("\n\n\033[1;31mInvalid input. Please input either \033[1;46m A \033[0m \033[1;31mor \033[1;46m S \033[0m\n")

                print("\nWhich traffic rule do you want to view?")
                rule_choice = input("Alcohol Limit: \033[1;46m A \033[0m | Max Speed: \033[1;46m S \033[0m\n> ").upper().strip()

            # change rule_name to input
            if rule_choice == "A":
                rule_name = "Alcohol Limit"
            else:
                rule_name = "Max Speed"

        # change filtering to inputted order
        if filter_input == "L":
            filter_toggle = True
            filter_setting = "1"
        elif filter_input == "R":
            filter_toggle = True
            filter_setting = "0"
        else:
            filter_toggle = False

        # change ordering to inputted order
        if order_input == "N":
            order = "country_name"
        elif order_input == "M":
            order = "min_licence_age"
        elif order_input == "A":
            order = "Alcohol Limit"
        elif order_input == "S":
            order = "Max Speed"
        else:
            order = "left_side"

        # --- Filter System ---
        # connecting with traffic_rules.db database
        if order_input == "A" or order_input == "S":
            if filter_toggle is True:
                data = [order, filter_setting]
                cursor.execute(f"SELECT {country_columns} WHERE traffic_rules.rule_name = ? AND country.left_side = ? ORDER BY CAST(traffic_rules.rule_value AS FLOAT) ASC;", data)
            else:
                data = [order]
                cursor.execute(f"SELECT {country_columns} WHERE traffic_rules.rule_name = ? ORDER BY CAST(traffic_rules.rule_value AS FLOAT) ASC;", data)
            header = get_header()
            output = cursor.fetchall()
            formatted_rows = get_format(output)

        # when not ordering by rule
        else:
            header = get_header()
            if filter_toggle is False:
                data = [rule_name]
                cursor.execute(f"SELECT {country_columns} WHERE traffic_rules.rule_name = ? ORDER BY {order};", data)

            else:
                data = [rule_name, filter_setting]
                cursor.execute(f"SELECT {country_columns} WHERE traffic_rules.rule_name = ? AND left_side = ? ORDER BY {order};", data)

            output = cursor.fetchall()
            formatted_rows = get_format(output)

        # loading screen to allow time for processing what is happening
        clear()
        print("\n\n\033[1;42m Loading. \033[0m\n\n")
        time.sleep(loading_time)
        clear()
        print("\n\n\033[1;42m Loading.. \033[0m\n\n")
        time.sleep(loading_time)
        clear()
        print("\n\n\033[1;42m Loading... \033[0m\n\n")
        time.sleep(loading_time)

        # display header title
        display_header(" RESULTS: ")

        # print data (either fancy or simple)
        if style.lower() == "f":
            print(tabulate(formatted_rows, headers=header, tablefmt="fancy_grid"))
        else:
            print(tabulate(formatted_rows, headers=header))

        # main menu return
        input("\n\nPress \033[1;46m Enter \033[0m to return to the main menu...\n")

    # -------------------------- Quit --------------------------
    # ends program and closes database
    elif choice == "Q":
        clear()
        print("\n\n\033[1;42m  Exiting Program. Goodbye! \033[0m\n\n")
        connection.close()
        sys.exit()
