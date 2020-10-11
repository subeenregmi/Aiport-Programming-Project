import csv


def main_menu():
    print("Welcome to the airport manager.")
    print("1. Enter Airport Details")
    print("2. Flight Details")
    print("3. Enter Price Plan And Calculate Profit")
    print("4. Clear Data")
    print("5. Quit")

    user_option = int(input("Please enter an option: "))

    if user_option == 1:
        airport_details()
        return

    if user_option == 2:
        flight_details()
        return

    if user_option == 3:
        price_plan()
        return

    if user_option == 4:
        clear_data()
        return

    if user_option == 5:
        print("You are quitting the program.")
        quit()
        return

    else:
        print("lol")
        main_menu()


def airport_details():
    global uk_tlc
    uk_tlc = input("Please enter a UK three letter code: ")
    if uk_tlc == "BOH" or uk_tlc == "LPL":
        global overseas_tlc
        overseas_tlc = input("Please enter a overseas three letter code: ")
        with open("Airport.txt") as f:  # where fn is the file name
            di = {row[0]: row[1] for row in csv.reader(f)}
        print("You have entered " + di[overseas_tlc])
        print("Returning to the main menu.")

    main_menu()


def flight_details():
    row = 0
    print('\nHere is where you type your flight details.')
    aircraft_type = str(input("Enter the type of aircraft: "))

    if aircraft_type == "Medium narrow body" or "Large narrow body" or "Medium wide body":
        if aircraft_type == "Medium narrow body":
            row = 0
            print("Medium narrow body aircraft:"
                    "\n-Running cost per seat per 100km = £8"
                    "\n-Maximum flight range(km) = 2650"
                    "\n-Capacity if all seats are standard-class = 180"
                    "\n-Minimum number of first-class seats = 8")


        if aircraft_type == "Large narrow body":
            row = 1
            print("Large narrow body aircraft:"
                    "\n-Running cost per seat per 100km = £7"
                    "\n-Maximum flight range(km) = 5600"
                    "\n-Capacity if all seats are standard-class = 220"
                    "\n-Minimum number of first-class seats = 10")


        if aircraft_type == "Medium wide body":
            row = 2
            print("Medium wide body aircraft:"
                    "\n-Running cost per seat per 100km = £5"
                    "\n-Maximum flight range(km) = 4050"
                    "\n-Capacity if all seats are standard-class = 406"
                    "\n-Minimum number of first-class seats = 14")




    first_class_seats = int(input("Please enter the number of first class seats: "))

    with open('Figure_2.txt', mode='r') as file:
        csvFile = csv.reader(file)
        x = list(csvFile)

    if first_class_seats != 0:
        if first_class_seats < int(x[row][4]):
            print("Invalid number, try again.")
            flight_details()
        if first_class_seats > (int(x[row][3]))/2:
            print("Invalid number, try again.")
            flight_details()

    standard_seats = int(x[row][3]) - first_class_seats * 2

    print("Returning to the menu")
    main_menu()



def price_plan():
    print("price plan + profit")
    if (uk_tlc != 'BOH') or 'LPL':
        print("No Uk valid code")
        main_menu()
    if (overseas_tlc != 'JFK') or 'ORY' or 'MAD' or 'AMS' or 'CAI':
        print("No valid overseas code, try again")
        main_menu()

def clear_data():
    print("clear data")


main_menu()
