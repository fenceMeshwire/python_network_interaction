#!/usr/bin/env python3

# Python 3.9.5

# 03_patch_area_designation_small_company.py

LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', \
    'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

LETTERS_DIGITS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', \
    'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', \
    1, 2, 3, 4, 5, 6, 7, 8, 9]

def create_designations(LETTERS, LETTERS_DIGITS):
    result = []
    for first in LETTERS:
        designation = str(first)
        for second in LETTERS_DIGITS:           
            designation += str(second)
            result.append(designation)
            designation = str(first)
    return result

if __name__ == '__main__':
    result = create_designations(LETTERS, LETTERS_DIGITS)
    print(result)
    # ['AA', 'AB', 'AC', ..., 'A7', 'A8', 'A9', 'BA', 'BB', ...]
    count_designations = len(result)
    print(count_designations)
    # 792
