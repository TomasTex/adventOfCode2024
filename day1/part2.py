list1 = []
list2 = []
sScore, index, buffer = 0, 0, 0

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        lineNumbers = line.split()
        list1.append(int(lineNumbers[0]))
        list2.append(int(lineNumbers[1]))

#sorting the first list makes it so that all the same numbers are followed by eachother, reducing the times i call count()
list1.sort() 

for n1 in list1:
    if index > 0 and list1[index] == list1[index - 1]: #if the last one is the same as now, just add the buffer, no need for count()
        sScore += buffer
        continue

    count = list2.count(n1)
    buffer = n1 * count
    sScore += buffer
    index += 1

print(sScore)






