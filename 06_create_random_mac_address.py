#!/usr/bin/env python3

# Python3.9.5

# 06_create_random_mac_address.py

# Purpose: Method to generate a purely random MAC address.

# Dependency
import random

def create_block():
    digits = random.randint(0, 255) # Random decimal number from 0 to 255
    digits = str(hex(digits)) # Convert decimal number to hexadecimal number
    digits = digits[2:4] # Extract the last two digits of the result
    result_digits = ''
    for digit in digits:
        if digit.isalpha():
            # Convert lower case to upper case, if the digit is a letter
            result_digits = result_digits  + digit.upper() 
        else:
            result_digits = result_digits  + digit
    return result_digits

def assemble_mac_address():
    return ':'.join([create_block() for i in range(6)])
        
if __name__ == '__main__':
    random_mac_address = assemble_mac_address()
    print(random_mac_address)
