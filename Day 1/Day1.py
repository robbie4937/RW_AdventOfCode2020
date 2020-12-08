import re

GOAL = 2020

def integers(s):
    #Takes a string and return digits split by any other character into generator."""
    return [int(i) for i in re.split(r'\D+', s) if i]

def part_1(data: list) -> int:
    for index_a, a in enumerate(data):
        for b in data[index_a:]:
            if a + b == GOAL:
                return a * b

def part_2(data: list) -> int:
    for index_a, a in enumerate(data):
        for index_b, b in enumerate(data[index_a:]):
            for c in data[index_b:]:
                if a + b + c == GOAL:
                    return a * b * c

def main():
    d = integers(open('Day1_input.txt').read())
    print(part_1(d))
    print(part_2(d))


if __name__ == '__main__':
    main()