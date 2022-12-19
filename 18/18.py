input = [tuple(int(x) for x in line.split(",")) for line in open("18.in", "r")]


d = (-1, 0, 0)
l = (0, -1, 0)
b = (0, 0, -1)
u = (1, 0, 0)
r = (0, 1, 0)
f = (0, 0, 1)

adj = (d, l, b, u, r, f)


def plus(a, b):
    return tuple(x + y for x, y in zip(a, b))


cnt = 6 * len(input)
cubes = set(input)
for cube in input:
    for a in adj:
        if plus(cube, a) in cubes:
            cnt -= 1
print(cnt)

highestCube = input[0]
for cube in input:
    if cube[0] > highestCube[0]:
        highestCube = cube


def generateAdj(side):
    for i, v in enumerate(side):
        if v == 0:
            tmp = list(side)
            zero = [0, 0, 0]
            negZero = [0, 0, 0]
            for x in [1, -1]:
                tmp[i] = x
                zero[i] = -x
                negZero[i] = x
                yield (
                    (
                        (tuple(tmp), tuple(zero)),
                        (tuple(negZero), tuple(side)),
                        ((0, 0, 0), tuple(negZero)),
                    )
                )


adj2 = {a: tuple(generateAdj(a)) for a in adj}
visited = set()


toVisit = {(highestCube, u)}
while len(toVisit) > 0:
    tmpToVisit = set()
    for pane in toVisit:
        if pane not in visited:
            visited.add(pane)
            for edge in adj2[pane[1]]:
                if plus(pane[0], edge[0][0]) in cubes:
                    tmpToVisit.add((plus(pane[0], edge[0][0]), edge[0][1]))
                elif plus(pane[0], edge[1][0]) in cubes:
                    tmpToVisit.add((plus(pane[0], edge[1][0]), edge[1][1]))
                else:
                    tmpToVisit.add((pane[0], edge[2][1]))

    toVisit = tmpToVisit

print(len(visited))
