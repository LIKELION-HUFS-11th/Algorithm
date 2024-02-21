import sys

people, killNum = map(int, sys.stdin.readline().split())

peopleList = []
for i in range(people):
    peopleList.append(i+1)

russianRoulette = 0
result = []
while len(peopleList) != 1:
    russianRoulette = (russianRoulette + (killNum-1)) % len(peopleList)
    result.append(peopleList[russianRoulette%len(peopleList)])
    del peopleList[russianRoulette%len(peopleList)]
result.append(peopleList[0])

strList = map(str, result)
printResult = ", ".join(strList)
print("<"+printResult+">")
