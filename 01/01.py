#!/opt/homebrew/bin/python

input = open('01.in','r')
maxFood = 0
elfCnt=0
elfCnts = []

for line in input:
  if len(line) == 1:
    maxFood = max([maxFood,elfCnt])
    elfCnts.append(elfCnt)
    elfCnt=0
  else:
    elfCnt += int(line)

maxFood = max(maxFood,elfCnt)
print(maxFood)
elfCnts.append(elfCnt)
elfCnts.sort(reverse=True)
print(elfCnts[0]+elfCnts[1]+elfCnts[2])
