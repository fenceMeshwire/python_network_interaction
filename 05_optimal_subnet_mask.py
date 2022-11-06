#!/usr/bin/env python3

# Python 3.9.5

# 05_optimal_subnet_mask.py

# Purpose: Calculate parameters for the optimal subnet mask

# Dependency
import pandas as pd
from numpy import log as ln

def calculate_needed_digits(hosts):
    # Calculate the possible number of digits for the number of hosts
    digits = ln(hosts) / ln(2)
    digits = int(digits) + 1
    return digits

def calculate_optimal_subnet_mask(IP):
    parts = IP.split('/')
    parts.pop()
    parts = parts[0]
    parts = parts.split('.')

    subnet_split = IP.split('/')
    subnet_split = subnet_split.pop()

    binary_parts = [str(bin(int(part))) for part in parts]
    result = []
    for binary_part in binary_parts:
        bin_part = binary_part.replace('0b', '')
        if len(bin_part) < 8:
            bin_part = '0' * (8-len(bin_part)) + bin_part
        result.append (bin_part)

    binary_parts = result

    subnet_mask = ''
    for i in range(32):
        if i < int(subnet_split):
            subnet_mask += '1'
        else:
            subnet_mask += '0'

    first = subnet_mask[0:8]
    second = subnet_mask[8:16]
    third = subnet_mask[16:24]
    fourth = subnet_mask[24:32]

    binary_subnet_mask = [first, second, third, fourth]
    subnet_mask = [mask.encode() for mask in binary_subnet_mask]
    subnet_mask_decimal = [int(mask.decode(), 2) for mask in subnet_mask]

    heading = ['1st octet', '2nd octet', '3rd octet', '4th octet']
    index = ['decimal', 'binary', 'binary_subnet', 'decimal_subnet']

    df = pd.DataFrame(columns=heading, index=index)
    df.loc[index[0]] = parts
    df.loc[index[1]] = binary_parts
    df.loc[index[2]] = binary_subnet_mask
    df.loc[index[3]] = subnet_mask_decimal

    return df 

if __name__ == '__main__':
    hosts = 505
    needed_digits = calculate_needed_digits(hosts)
    IP = '196.145.16.0' + '/' + str(32 - needed_digits)
    IP_CIDR = IP + '/' + str(32 - needed_digits)
    opt_subnet_mask = calculate_optimal_subnet_mask(IP_CIDR)
    print(opt_subnet_mask)
