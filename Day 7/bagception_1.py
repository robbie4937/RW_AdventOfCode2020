#!/usr/bin/python3

import re

rules=[]

with open("bagception.txt") as f:
    rules=[line.strip()for line in f]

#print(rules)

contents = {}
for rule in rules:
    bag,contained_bags=rule.split("contain")
    #print(bag)
    #print(contained_bags)
    contained_bags=[b.strip()for b in contained_bags.split(',')]
    #print(contained_bags)
    parsed_contained_bags = [re.match('(\d)\s([\s\w]+)\s((bags)|(bag))', b) for b in contained_bags]
    #print(parsed_contained_bags)
    parsed_contained_bags = [(int(m.group(1)), m.group(2)) for m in parsed_contained_bags if m]
    #print(parsed_contained_bags)

    contents[bag.split('bags')[0].strip()] = parsed_contained_bags

def find(bag_name,searched_bag):
    return bag_name == searched_bag or any([find(b[1],searched_bag) for b in contents[bag_name]])

# part 1

print(sum([any([find(b[1], 'shiny gold') for b in contents[rule]]) for rule in contents]))



