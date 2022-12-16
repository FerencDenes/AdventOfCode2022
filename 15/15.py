#!/opt/homebrew/bin/python
import re

input = open("15.in", "r")
rowNo = 2000000

coords = []
for line in input:
    x = re.search(
        r"Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", line
    )
    coords.append([int(x.group(i)) for i in range(1, 5)])


rowFree = []


def getFree(rn, sensor):
    dist = abs(sensor[0] - sensor[2]) + abs(sensor[1] - sensor[3])
    dist1 = abs(sensor[1] - rn)
    rangeWidth = dist - dist1
    if rangeWidth >= 0:
        return (sensor[0] - rangeWidth, sensor[0] + rangeWidth)
    return None


for sensor in coords:
    fr = getFree(rowNo, sensor)
    if fr != None:
        rowFree.append(fr)


def consolidate(rowFree):
    rowFree.sort()
    ret = []
    currentSlice = None
    for rf in rowFree:
        if currentSlice == None:
            currentSlice = rf
        elif currentSlice[1] + 1 < rf[0]:
            ret.append(currentSlice)
            currentSlice = None
        elif currentSlice[1] < rf[1]:
            currentSlice = (currentSlice[0], rf[1])
    ret.append(currentSlice)
    return ret


rowFreeConsolidated = consolidate(rowFree)
beacons = {coord[2] for coord in filter(lambda c: c[3] == rowNo, coords)}
sum = sum(
    rf[1]
    - rf[0]
    + 1
    - len(list(filter(lambda b, rf0=rf[0], rf1=rf[1]: rf0 <= b <= rf1, beacons)))
    for rf in rowFreeConsolidated
)
print(sum)

i = 0
limit = 4000000
notFound = True
while notFound and i <= limit:
    rowFree = []
    for sensor in coords:
        fr = getFree(i, sensor)
        if fr != None:
            rowFree.append(fr)
    rowFreeConsolidated = consolidate(rowFree)
    if (
        len(rowFreeConsolidated) > 1
        or rowFreeConsolidated[0][0] > 0
        or rowFreeConsolidated[0][1] < limit
    ):
        notFound = False

        print(i + (rowFreeConsolidated[0][1] + 1) * limit)
    i += 1
