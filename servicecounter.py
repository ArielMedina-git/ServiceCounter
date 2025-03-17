#       project: servicecounter.py
#       author: Ariel Medina
#       <amedina2718050@woonsocketschools.com>
#       date written: 3/12/2025
#
#       description: Creating an app for automotive
total = 0
oil = 79.99
standardTire = 30
fourWD = 45
brakes = 120
largeWindow = 69.99
smallWindow = 39.99
smallDent = 5
largeDent = 15

print("Welcome to the Automotive Shop of the WACTC.")
print()

name = input("What is the name of the owner of the vehicle? ")
make = input("What is the make and model of the vehicle? ")
mileage = input("What is the current mileage of the car? ")

print('''We provide 4 services:
1. Oil and Filter Change for $79.99 
2. Tire Rotation; $30 for standard tires
3. Tire Rotation; $45 for 4WD or Truck Tires
4. Brake Pads and Front End Alignment; $120 for the package
5. Broken Glass Repair; $69.99 for a large window
6. Broken Glass Repair; $39.99 for a small window
7. Dent Removal; $5 per small dent
8. Dent Removal; $15 per large dent
''')

services = True
while services:
    try:
        choice = int(input("To select a service, type the number next to that service: "))
        if choice == 1:
            total += oil
            print(f"Oil and Filter Change selected. Current total: ${total:.2f}")
            more = input("Would you like any more services? (Yes or No): ")
            if more == "No":
                services = False
                print(f"\nThank you, {name}. The total for services on your {make} is ${total:.2f}.")
        elif choice == 2:
            total += standardTire
            print(f"Standard Tire Rotation selected. Current total: ${total:.2f}")
            more = input("Would you like any more services? (Yes or No): ")
            if more == "No":
                services = False
                print(f"\nThank you, {name}. The total for services on your {make} is ${total:.2f}.")
        elif choice == 3:
            total += fourWD
            print(f"4WD Tire Rotation selected. Current total: ${total:.2f}")
            more = input("Would you like any more services? (Yes or No): ")
            if more == "No":
                services = False
                print(f"\nThank you, {name}. The total for services on your {make} is ${total:.2f}.")
        elif choice == 4:
            total += brakes
            print(f"Brake Pads and Front End Alignment selected. Current total: ${total:.2f}")
            more = input("Would you like any more services? (Yes or No): ")
            if more == "No":
                services = False
                print(f"\nThank you, {name}. The total for services on your {make} is ${total:.2f}.")
        elif choice == 5:
            total += largeWindow
            print(f"Large Window Repair selected. Current total: ${total:.2f}")
            more = input("Would you like any more services? (Yes or No): ")
            if more == "No":
                services = False
                print(f"\nThank you, {name}. The total for services on your {make} is ${total:.2f}.")
        elif choice == 6:
            total += smallWindow
            print(f"Small Window Repair selected. Current total: ${total:.2f}")
            more = input("Would you like any more services? (Yes or No): ")
            if more == "No":
                services = False
                print(f"\nThank you, {name}. The total for services on your {make} is ${total:.2f}.")
        elif choice == 7:
            total += smallDent
            print(f"Small Dent Removal selected. Current total: ${total:.2f}")
            more = input("Would you like any more services? (Yes or No): ")
            if more == "No":
                services = False
                print(f"\nThank you, {name}. The total for services on your {make} is ${total:.2f}.")
        elif choice == 8:
            total += largeDent
            print(f"Large Dent Removal selected. Current total: ${total:.2f}")
            more = input("Would you like any more services? (Yes or No): ")
            if more == "No":
                services = False
                print(f"\nThank you, {name}. The total for services on your {make} is ${total:.2f}.")
        else:
            print("Invalid choice. Please select a valid service.")
    except ValueError:
        print("Invalid input. Please enter a number corresponding to the service.")
