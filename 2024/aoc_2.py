with open("aoc_2.txt") as file:
    lines = file.read().splitlines()
    
def is_safe(level):
    level = [int(x) for x in level]
    for i in range(1, len(level)):
        if abs(level[i] - level[i-1]) > 3 or abs(level[i] - level[i-1]) == 0:
            return False

    if level != sorted(level) and level != sorted(level, reverse=True):
        return False

    return True

def is_safe_removing_level(level):
    level = [int(x) for x in level]

    i = 0
    while i < len(level):
        new_level = level[:i] + level[i+1:]  # remove the element at index i
        if is_safe(new_level):
            return True
        i += 1
    
    return False


# part one:
safe1 = 0
for line in lines:
    level = line.split(" ")
    if is_safe(level):
        safe1 += 1
#part two:
safe2 = 0
for line in lines:
    level = line.split(" ")
    if is_safe(level):
        safe2 += 1
    elif is_safe_removing_level(level):
        safe2 += 1


print(safe1) #236
print(safe2) #308