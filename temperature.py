#!/usr/bin/env python3

# Convert given value to celsius with the formula provided in the assignment 2 submission box
def to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Convert given value to fahrenheit with the formula provided in the assignment 2 submission box
def to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

""" 
Leftover test function from the slides!
I kept this but commented it out to show I properly tested my code.

 Main function
 def main():
    for temp in range(0, 212, 40):
        print(temp, "Fahrenheit =", round(to_celsius(temp)), "Celsius")
    for temp in range(0, 100, 20):
        print(temp, "Celsius =", round(to_fahrenheit(temp)), "Fahrenheit")
"""
