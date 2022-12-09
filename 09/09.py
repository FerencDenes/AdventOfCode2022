#!/opt/homebrew/bin/python

input = open("09.in", "r")

positions = [(0, 0) for i in range(10)]
visited1 = {positions[1]}
visited9 = {positions[9]}

for line in input:
    direction, amt = line.split(" ")

    for _ in range(int(amt)):
        if direction == "R":
            positions[0] = (positions[0][0] + 1, positions[0][1])
        elif direction == "L":
            positions[0] = (positions[0][0] - 1, positions[0][1])
        elif direction == "U":
            positions[0] = (positions[0][0], positions[0][1] + 1)
        elif direction == "D":
            positions[0] = (positions[0][0], positions[0][1] - 1)
        for i in range(9):
            while (
                abs(positions[i][0] - positions[i + 1][0]) > 1
                or abs(positions[i][1] - positions[i + 1][1]) > 1
            ):
                if positions[i][0] - positions[i + 1][0] >= 1:
                    if positions[i][1] - positions[i + 1][1] >= 1:
                        positions[i + 1] = (
                            positions[i + 1][0] + 1,
                            positions[i + 1][1] + 1,
                        )
                    elif positions[i][1] - positions[i + 1][1] <= -1:
                        positions[i + 1] = (
                            positions[i + 1][0] + 1,
                            positions[i + 1][1] - 1,
                        )
                    else:
                        positions[i + 1] = (
                            positions[i + 1][0] + 1,
                            positions[i + 1][1],
                        )
                elif positions[i][0] - positions[i + 1][0] <= -1:
                    if positions[i][1] - positions[i + 1][1] >= 1:
                        positions[i + 1] = (
                            positions[i + 1][0] - 1,
                            positions[i + 1][1] + 1,
                        )
                    elif positions[i][1] - positions[i + 1][1] <= -1:
                        positions[i + 1] = (
                            positions[i + 1][0] - 1,
                            positions[i + 1][1] - 1,
                        )
                    else:
                        positions[i + 1] = (
                            positions[i + 1][0] - 1,
                            positions[i + 1][1],
                        )
                elif positions[i][1] - positions[i + 1][1] > 1:
                    positions[i + 1] = (positions[i + 1][0], positions[i + 1][1] + 1)
                else:
                    positions[i + 1] = (positions[i + 1][0], positions[i + 1][1] - 1)
                visited1.add(positions[1])
                visited9.add(positions[9])

print(len(visited1))
print(len(visited9))
