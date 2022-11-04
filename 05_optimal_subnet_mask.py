#!/usr/bin/env python3

# Python 3.9.5

# 05_optimal_subnet_mask.py

# Purpose: Calculate parameters for the optimal subnet mask

# Dependency
import pandas as pd
from numpy import log as ln

def calculate_addresses(digits):
    # Calculate the number of available IP addresses:
    addresses = 2**digits - 2
    return addresses

def calculate_needed_digits(hosts):
    # Calculate the possible number of digits for the number of hosts
    digits = ln(hosts) / ln(2)
    digits = int(digits) + 1
    return digits

def calculate_optimal_subnet_mask(IP):
    parts = IP.split('.')
    subnet_split = IP.split('/')
    parts = [part[0:3] for part in parts]

    if len(subnet_split) > 1:
        subnet_split = subnet_split[1]

    binary_parts = [str(bin(int(part)))[2:10] for part in parts]
    binary_parts = [part.encode() for part in binary_parts]

    available_digits = 24 - int(subnet_split)

    subnet_mask = ''
    for i in range(32):
        if i <= int(subnet_split):
            subnet_mask += '1'
        else:
            subnet_mask += '0'

    first = subnet_mask[0:8]
    second = subnet_mask[8:16]
    third = subnet_mask[16:24]
    fourth = subnet_mask[24:32]

    subnet_mask = [first, second, third, fourth]
    subnet_mask = [mask.encode() for mask in subnet_mask]
    subnet_mask_decimal = [int(mask.decode(), 2) for mask in subnet_mask]
    subnet_mask_decimal

    heading = ['1st octet', '2nd octet', '3rd octet', '4th octet']
    index = ['decimal', 'binary', 'binary_subnet', 'decimal_subnet']

    df = pd.DataFrame(columns=heading, index=index)
    df.loc[index[0]] = parts
    df.loc[index[1]] = binary_parts
    df.loc[index[2]] = subnet_mask
    df.loc[index[3]] = subnet_mask_decimal
    return df, available_digits

def confirm_possible_hosts(number_of_adresses):
    if (number_of_adresses // 255) == 0:
        ubound = 2
        level = number_of_adresses
        counter = 0
    else: 
        ubound = 1 + number_of_adresses // 255
        level = 255
        counter = 2
    for a in range(1, ubound):
        for b in range(1, level + 1):
            counter += 1
    return counter

if __name__ == '__main__':
    IP = '192.168.191.195/18'
    # split at 18th digit -> 6 digits available
    opt_subnet_mask, available_digits = calculate_optimal_subnet_mask(IP)
    print(opt_subnet_mask)
    print()
    number_of_adresses = calculate_addresses(available_digits)
    print("Number of addresses:\t", number_of_adresses)
    digits = calculate_needed_digits(number_of_adresses)
    print("Number of digits:\t", digits)
    print("Test calculation:\t", calculate_addresses(available_digits) == confirm_possible_hosts(number_of_adresses))
