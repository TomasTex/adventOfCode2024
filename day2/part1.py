nOfSafeReports = 0

def lineIsValid(line:list) -> bool:
    increasing = all(1 <= line[i] - line[i - 1] <= 3 for i in range(1, len(line))) #index = 0 doesnt have any number before
    decreasing = all(-3 <= line[i] - line[i - 1] <= -1 for i in range(1, len(line)))
    return increasing or decreasing
 
with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = [int(n) for n in line.split()]
        if lineIsValid(line): nOfSafeReports += 1
        continue

print(nOfSafeReports)
        