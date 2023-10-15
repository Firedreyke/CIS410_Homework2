#!/usr/bin/env python3
import temperature as temp

# Display title function
def show_title():
    print()
    print ("=====================")
    print("TEMPERATURE CONVERTER")
    print ("=====================")
    print()

# Display menu options function
def show_menu():
    print("Options")
    print()
    print("1: Convert Fahrenheit to Celsius")
    print("2: Convert Celsius to Fahrenheit")
    print()

# Convert temperature function
def convert_temp():
    option = int(input("Please enter your chosen option: "))

    # Check if option 1 or 2; if 1, run f to c; if 2, run c to f
    # Else, try again
    if option == 1:
        f = int(input("Enter temperature in Fahrenheit: "))

        # Run conversion from temp
        c = temp.to_celsius(f)

        # Round to the nearest whole number (nearest integer) and display
        c = int(round(c))
        print()
        print("Celsius:", c)
    elif option == 2:
        c = int(input("Enter temperature in Celsius: "))

        # Run conversion from temp
        f = temp.to_fahrenheit(c)

        # Round to the nearest whole number (nearest integer) and display
        f = int(round(f))
        print()
        print("Fahrenheit: ", f)
    else:
        print("That is not a valid menu option.")

# Main function
def main():
    # Show title and options
    show_title()
    show_menu()

    # Set loop control variable
    again = "y"

    # While LCV is y, keep looping program; otherwise, exit
    while again.lower() == "y":
        convert_temp()
        print()
        again = input("Would you like to go again? (y/n) ")
        print()

    # Exiting
    print("Have a great day!")
    print()

if __name__=="__main__":
    main()