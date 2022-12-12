input = open("12.in", "r")
map = [[ord(a) for a in line] for line in input]

for x, row in enumerate(map):
    for y, elem in enumerate(row):
        if elem == ord("S"):
            start = (x, y)
            map[x][y] = ord("a")
        if elem == ord("E"):
            end = (x, y)
            map[x][y] = ord("z")

visited = set()
steps = 0
tovisit = {start}
found = False
while not found:
    tmpTovisit = set()
    steps += 1

    for node in tovisit:
        if not node in visited:
            visited.add(node)
            x = node[0]
            y = node[1]
            val = map[node[0]][node[1]]
            coords = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]

            for n in coords:

                if (
                    n[0] >= 0
                    and n[0] < len(map)
                    and n[1] >= 0
                    and n[1] < len(map[0])
                    and val >= map[n[0]][n[1]] - 1
                    and not n in visited
                ):
                    if n == end:
                        print(steps)
                        found = True
                        break
                    tmpTovisit.add(n)
    tovisit = tmpTovisit

min = steps
for s0, row in enumerate(map):
    for s1, elem in enumerate(row):
        if elem == ord("a"):
            visited = set()
            steps = 0
            tovisit = {(s0, s1)}
            found = False
            while not found and len(tovisit) > 0:
                tmpTovisit = set()
                steps += 1

                for node in tovisit:
                    if not node in visited:
                        visited.add(node)
                        x = node[0]
                        y = node[1]
                        val = map[node[0]][node[1]]
                        coords = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]

                        for n in coords:

                            if (
                                n[0] >= 0
                                and n[0] < len(map)
                                and n[1] >= 0
                                and n[1] < len(map[0])
                                and val >= map[n[0]][n[1]] - 1
                                and not n in visited
                            ):
                                if n == end:
                                    if min > steps:
                                        min = steps
                                    # print(steps, min)

                                    found = True
                                    break
                                tmpTovisit.add(n)
                tovisit = tmpTovisit

print(min)
