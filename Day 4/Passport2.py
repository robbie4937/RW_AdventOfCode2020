
"""
Robbie Williams 04/12/2020

Use regular expressions to define the parameters

From task 1 we only specifed the name to check, open up to dictionary allow for name and value
to be referenced

Requires additional code in passport function
"""
import re

REQUIRED_ATTRIBUTES = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: ("cm" in x and (150 <= int(x.replace("cm","")) <= 193)) or
                     ("in" in x and (59 <= int(x.replace("in","")) <= 76)),
    "hcl": lambda x: re.match(r"#[0-9 a-f]{6}",x),
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: len(x) == 9
}

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

    """
    3. Check Attribute aligns with values in array (now Dictionary)

    """

    present_attributes = passport_attribute_names.intersection(REQUIRED_ATTRIBUTES)

    """
    4. Don't check if minimum values exist
    5. Check against dictionary values
    """

    if present_attributes != set(REQUIRED_ATTRIBUTES.keys()):
        return False


    for passport_attribute in passport_attributes:
        name, value = passport_attribute.split(":")
        if name in REQUIRED_ATTRIBUTES.keys() and not REQUIRED_ATTRIBUTES[name](value):
            return False

    return True


"""
Counting of occurances based on function
"""

if __name__ == '__main__':
    input_data = open("Batch Passport - file.txt", "r").read().split("\n\n")
    #print(input_data)
    valid_passports = 0
    for passport in input_data:
        valid_passports += 1 if validate_passport(passport) else 0
    print("Amount of valid passports:", valid_passports)