import copy

nOfSafeReports = 0

def trendOfTheValues(line: list) -> str:
    increases = 0
    decreases = 0

    for i in range(1, len(line)):
        if line[i] > line[i - 1]:
            increases += 1
        elif line[i] < line[i - 1]:
            decreases += 1
    #we will never have lists who arent either increasing or decreasing
    return "increasing" if increases > decreases else "decreasing" 

def getFaultyIndexes(line: list)-> list:
    trend = trendOfTheValues(line)
    listFaultyIndexes = []
    for i in range(1, len(line)):
        diff = line[i] - line[i - 1]
        if not (1 <= abs(diff) <= 3): #if theres a bigger than 3 or smaller than 1 difference regardless of up or down, its a fault
            listFaultyIndexes.append(i)
            listFaultyIndexes.append(i-1)
        elif trend == "increasing" and diff < 0: #if its increasing but decreased
            listFaultyIndexes.append(i)
            listFaultyIndexes.append(i-1)
        elif trend == "decreasing" and diff > 0: #if its decreasing but increased
            listFaultyIndexes.append(i)
            listFaultyIndexes.append(i-1)
        elif diff == 0:
            listFaultyIndexes.append(i)
            listFaultyIndexes.append(i-1)
        elif trend == "increasing" and i == 1 and line[i - 1] > line[i]: #if its the first one that goes against the trend add the first one this case was escaping
            listFaultyIndexes.append(i)
            listFaultyIndexes.append(i-1)
        elif trend == "decreasing" and i == 1 and line[i] > line[i -1]:
            listFaultyIndexes.append(i)
            listFaultyIndexes.append(i-1)
    return list(set(listFaultyIndexes))
    
with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = [int(n) for n in line.split()]
        if all(1 <= line[i] - line[i - 1] <= 3 for i in range(1, len(line))) or all(-3 <= line[i] - line[i - 1] <= -1 for i in range(1, len(line))):
            nOfSafeReports += 1
            continue
        listOfFaultyIndexes = getFaultyIndexes(line)
        for index in listOfFaultyIndexes:
            tempLine = copy.deepcopy(line)
            del tempLine[index]
            if all(1 <= tempLine[i] - tempLine[i - 1] <= 3 for i in range(1, len(tempLine))) or all(-3 <= tempLine[i] - tempLine[i - 1] <= -1 for i in range(1, len(tempLine))):
                nOfSafeReports += 1
                break #prevents a line to be counted multiple times when there are two equal adjacent numbers ;-; 
     
print(nOfSafeReports)
