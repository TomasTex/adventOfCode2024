list1 = []
list2 = []
distSum = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        lineNumbers = line.split()
        list1.append(int(lineNumbers[0]))
        list2.append(int(lineNumbers[1]))

list1.sort()
list2.sort()

for i in range(len(list1)):
    distSum += abs(list1[i] - list2[i])

print(distSum)



