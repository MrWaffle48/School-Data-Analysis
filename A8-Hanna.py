#A8-Hanna.py
accCount = 0
baCount = 0
isCount = 0
csCount = 0
totalCount = 0
accSum = 0
baSum = 0
isSum = 0
csSum = 0
overallSum = 0
with open("Student-Major-GPA.txt", "r") as file:
    for line in file:
        values = line.strip().split(",")
        print(values)
        if values[2] == "ACC":
            accCount += 1
            accSum += float(values[3])
        elif values[2] == "BA":
            baCount += 1
            baSum += float(values[3])
        elif values[2] == "IS":
            isCount += 1
            isSum += float(values[3])
        elif values[2] == "CS":
            csCount += 1
            csSum += float(values[3])
        totalCount += 1
        overallSum += float(values[3])
accAvg = accSum / accCount
baAvg = baSum / baCount
isAvg = isSum / isCount
csAvg = csSum / csCount
overallAvg = overallSum / totalCount
print(f"ACC count {accCount}")
print(f"BA count {baCount}")
print(f"IS count {isCount}")
print(f"CS count {csCount}")
print(f"Total count {totalCount}")
print(f"ACC average GPA {accAvg:.2f}")
print(f"BA average GPA {baAvg:.2f}")
print(f"IS average GPA {isAvg:.2f}")
print(f"CS average GPA {csAvg:.2f}")
print(f"Overall average GPA {overallAvg:.2f}")
