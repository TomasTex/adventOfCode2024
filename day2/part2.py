nOfSafeReports = 0

def lineIsValid(line: list) -> bool:
    alwaysIncreasing = all(1 <= line[i] - line[i - 1] <= 3 for i in range(1, len(line)))
    alwaysDecreasing = all(-3 <= line[i] - line[i - 1] <= -1 for i in range(1, len(line)))
    return alwaysIncreasing or alwaysDecreasing

def validWithAFault(line: list) -> bool:
    for i in range(len(line)):  # Try removing each element one by one
        modified_line = line[:i] + line[i + 1:] 
        if lineIsValid(modified_line): return True
    return False  

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = [int(n) for n in line.split()]  
        if lineIsValid(line):  
            nOfSafeReports += 1
        elif validWithAFault(line): 
            nOfSafeReports += 1

print(nOfSafeReports)
