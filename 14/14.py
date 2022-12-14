input = open("14.in", "r")

rocks = set()
maxDepth = 0
for line in input:
    points = [list(map(int, point.split(","))) for point in line.split(" -> ")]
    for i, elem in enumerate(points):
        rocks.add(tuple(elem))
        if i < len(points) - 1:
            nextElem = points[i + 1]
            if elem[0] == nextElem[0]:
                for i in range(
                    min(elem[1], nextElem[1]), max(elem[1], nextElem[1]) + 1
                ):
                    rocks.add((elem[0], i))
                maxDepth = max(maxDepth, elem[1])
            else:
                for i in range(
                    min(elem[0], nextElem[0]), max(elem[0], nextElem[0]) + 1
                ):
                    rocks.add((i, elem[1]))
                maxDepth = max(maxDepth, elem[1], nextElem[1])

settled = True
sandNo = 0
part1Done = False
r0 = len(rocks)
while settled:
    sandNo += 1
    pos = (500, 0)
    moved = True
    while moved and pos[1] < maxDepth + 1:
        if not (pos[0], pos[1] + 1) in rocks:
            pos = (pos[0], pos[1] + 1)
        elif not (pos[0] - 1, pos[1] + 1) in rocks:
            pos = (pos[0] - 1, pos[1] + 1)
        elif not (pos[0] + 1, pos[1] + 1) in rocks:
            pos = (pos[0] + 1, pos[1] + 1)
        else:
            moved = False
    if not part1Done and pos[1] >= maxDepth:
        print(len(rocks) - r0)
        part1Done = True
    rocks.add(pos)
    settled = pos[1] != 0

print(len(rocks) - r0)
