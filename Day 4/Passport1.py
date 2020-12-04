
"""
Robbie Williams 04/12/2020

Use regular expressions to define the parameters

"""

import re

REQUIRED_ATTRIBUTES = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def validate_passport(passport):
    """
    Function to reference when an attibute is present. 

    1. Split batch for each data into individual arrays
    2. Just take the start of that array for characteristic
    """
    passport_attributes = re.split(r"[\n ]",passport)
    #print(passport_attributes)
    passport_attribute_names = set([passport_attribute.split(":")[0] for passport_attribute in passport_attributes])
    #print(passport_attribute_names)

    present_attributes = passport_attribute_names.intersection(REQUIRED_ATTRIBUTES)

    return present_attributes == set(REQUIRED_ATTRIBUTES)


"""
Counting of occurances based on function
"""

if __name__ == '__main__':
    input_data = open("Batch Passport - file.txt", "r").read().split("\n\n")
    #print(input_data)
    valid_passports = 0
    for passport in input_data:
        valid_passports += 1 if validate_passport(passport) else 0
    print(f"Amount of valid passports: {valid_passports}")