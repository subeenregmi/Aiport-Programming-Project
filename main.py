import csv  # this is used to read Airport.txt as a cv file

space = "-----------------------------------"  # this makes the code clearer and gives sections to the code


def main_menu():  # this is the main menu function which when called it displays it
    print(space)
    print("Welcome to the airport manager.")  # these are the options of the menu
    print("\n1. Enter Airport Details")
    print("2. Flight Details")
    print("3. Enter Price Plan And Calculate Profit")
    print("4. Clear Data")
    print("5. Quit")
    print(space)

    user_option = int(input("Please enter an option: "))  # this asks the user for an option and stores it as a integer

    if user_option == 1:  # if the user enters one then the function airport_details is called
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
        print(space)
        print("You are quitting the program.")
        print(space)
        quit()  # this quites the program
        return

    else:
        print(space)
        print("Invalid input, try again.")
        main_menu()  # if a input which is not 1, 2, 3, 4 or 5 is typed then it goes back to the main menu


def airport_details():
    global uk_tlc  # this creates a global variable which can be used everywhere in the code
    print(space)
    print("This is where you enter your airport details")
    uk_tlc = input("\nPlease enter a UK three letter code: ")  # this takes the users UK airport code

    with open('Airport.txt', mode='r') as airp:
        airportFile = csv.reader(airp)
        global a
        a = list(airportFile)

    if uk_tlc == "BOH" or uk_tlc == "LPL":
        global overseas_tlc  # another global variable
        overseas_tlc = input("\nPlease enter a overseas three letter code: ")

        if overseas_tlc == str(a[0][0]):
            print('\nThe overseas airport is called ' + str(a[0][1]))

        elif overseas_tlc == str(a[1][0]):
            print('\nThe overseas airport is called ' + str(a[1][1]))

        elif overseas_tlc == str(a[2][0]):
            print('\nThe overseas airport is called ' + str(a[2][1]))

        elif overseas_tlc == str(a[3][0]):
            print('\nThe overseas airport is called ' + str(a[3][1]))

        elif overseas_tlc == str(a[4][0]):
            print('\nThe overseas airport is called ' + str(a[4][1]))

        else:

            print(space)
            print("Invalid input, try again.")
            main_menu()

    else:

        print(space)
        print("Invalid input, try again.")
        main_menu()

    print(space)
    print('You have successfully entered your airport details.')
    print("Returning to the main menu.")
    main_menu()


def flight_details():
    global row
    row = 0
    print('\nHere is where you type your flight details.')
    global aircraft_type
    aircraft_type = str(input("Enter the type of aircraft: "))
    if aircraft_type == "Medium narrow body" or "Large narrow body" or "Medium wide body":
        if aircraft_type == "Medium narrow body":
            row = 0
            print('Medium narrow body aircraft:'
                  '\n-Running cost per seat per 100km = £8'
                  '\n-Maximum flight range(km) = 2650'
                  '\n-Capacity if all seats are standard-class = 180'
                  '\n-Minimum number of first-class seats = 8')

        if aircraft_type == 'Large narrow body':
            row = 1
            print('Large narrow body aircraft:'
                  '\n-Running cost per seat per 100km = £7'
                  '\n-Maximum flight range(km) = 5600'
                  '\n-Capacity if all seats are standard-class = 220'
                  '\n-Minimum number of first-class seats = 10')

        if aircraft_type == "Medium wide body":
            row = 2
            print("Medium wide body aircraft:"
                  "\n-Running cost per seat per 100km = £5"
                  "\n-Maximum flight range(km) = 4050"
                  "\n-Capacity if all seats are standard-class = 406"
                  "\n-Minimum number of first-class seats = 14")
    global first_class_seats
    first_class_seats = int(input("Please enter the number of first class seats: "))

    with open('Figure_2.txt', mode='r') as file:
        csvFile = csv.reader(file)
        global x
        x = list(csvFile)

    if first_class_seats != 0:
        if first_class_seats < int(x[row][4]):
            print("Invalid number, try again.")
            flight_details()
        if first_class_seats > (int(x[row][3])) / 2:
            print("Invalid number, try again.")
            flight_details()
    global standard_seats
    standard_seats = int(x[row][3]) - first_class_seats * 2

    print("Returning to the menu")
    main_menu()


def price_plan():
    if "BOH" == uk_tlc or "LPL" == uk_tlc:
        if aircraft_type == "Medium narrow body" or aircraft_type == 'Large narrow body' or aircraft_type == 'Medium wide body:':
            if first_class_seats != 0:
                




def clear_data():
    print("clear data")


main_menu()
