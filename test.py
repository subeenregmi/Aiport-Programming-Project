import csv

#reader = csv.reader(open("Figure_2.txt", "r"))
##data = []
#for row in reader:
    #data.append(row)

#header = data.pop(0)

#def fixed_length(text, length):
    #if len(text) > length:
        #text = text[:length]
   # elif len(text) > length:
        #text = (text + " " * length)[:length]
    #return text

#print("#" *154)
#print("#  ", end=" ")
#for column in header:
    #print(fixed_length(column, 20), end= "  #  ")
#print()
##print("#" *154)

#for row in data:
#    print("#  ", end=" ")
#    for column in row:
#        print(fixed_length(column, 20), end="  #  ")
#   print()
#
#    if aircraft_type == "medium narrow" or "large narrow" or "medium wide":
#        print("You have entered an invalid type, try again.")
#        main_menu()
#        return
#
#    if aircraft_type == "medium narrow":
#        print("Medium narrow body aircraft:"
#              "\n Running cost per seat per 100km = £8"
#              "\n Maximum flight range(km) = 2650"
#              "\n Capacity if all seats are standard-class = 180"
#              "\n Minimum number of first-class seats = 8")
#
#    if aircraft_type == "large narrow":
#        print("Large narrow body aircraft:"
#              "\n Running cost per seat per 100km = £7"
#              "\n Maximum flight range(km) = 5600"
#              "\n Capacity if all seats are standard-class = 220"
#              "\n Minimum number of first-class seats = 10")
#
#    if aircraft_type == "medium wide":
#        print("Medium wide body aircraft:"
#              "\n Running cost per seat per 100km = £5"
#              "\n Maximum flight range(km) = 4050"
#              "\n Capacity if all seats are standard-class = 406"
#              "\n Minimum number of first-class seats = 14")
#
#    first_class_seats = int(input("Please enter the number of first class seats: "))
#    if first_class_seats != 0:




import csv
with open('Figure_2.txt', mode ='r') as file:
    csvFile = csv.reader(file)
    x = list(csvFile)
    print(x[2])