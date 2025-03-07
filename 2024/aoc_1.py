with open("inputs/aoc_1.txt") as file: 
    data = file.read().splitlines()

list_1 = []
list_2 = []
    
for lines in data:
    line = lines.split("   ")
    
    list_1.append(int(line[0]))
    list_2.append(int(line[1]))

list_1.sort()
list_2.sort()

total_distance = 0
similarity_score = 0

for i in range(len(list_1)):
    total_distance += abs(list_1[i] - list_2[i])
    similarity_score += list_1[i] * list_2.count(list_1[i])

print(total_distance)  #1882714
print(similarity_score) #19437052
