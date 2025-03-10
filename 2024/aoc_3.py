import re

with open("inputs/aoc_3.txt") as file:
    data = file.read().splitlines()

result = 0

for line in data:
    line = re.findall(r"mul\((\d\d?\d?,\d\d?\d?)\)", line)
    for string in line:
        a, b = string.split(",")
        result += int(a) * int(b)

print(result) #173785482

result2 = 0

for line in data:
    line = re.findall(r"don't\(\)|do\(\)|mul\(\d\d?\d?,\d\d?\d?\)", line)
    do = True
    for string in line:
        if string == "do()":
            do = True
            continue
        if string == "don't()":
            do = False
            continue

        if do:
            match = re.findall(r"mul\((\d\d?\d?,\d\d?\d?)\)", string)
            if match:
                a, b = match[0].split(",")
                result2 += int(a) * int(b)

print(result2)



