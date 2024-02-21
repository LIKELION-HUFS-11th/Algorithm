selfNumSet = set()
resultSet = set()
for i in range(10000):
    newNum = i
    for j in str(i):
        newNum += int(j)
    selfNumSet.add(newNum)
    resultSet.add(i)
sortedSet = sorted(resultSet-selfNumSet)

for k in sortedSet:
    print(k)