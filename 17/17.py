line = open("17.in").readline().strip()
elems = (
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)),
    ((0, 0), (0, 1), (0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((0, 0), (-0, 1), (1, 0), (1, 1)),
)
tower = set()
for i in range(7):
    tower.add((0, i))

max = 0
windPos = 0
state = set()
stateRev = {}
periodFound = False
periodState0 = None
for i in range(20220000):
    currentShape = elems[i % len(elems)]
    pos = (max + 4, 2)
    moving = True
    while moving:
        tmpPos = (
            pos[0],
            pos[1] + (-1 if line[windPos % len(line)] == "<" else 1),
        )
        windPos += 1
        if all(
            [
                (e[0] + tmpPos[0], e[1] + tmpPos[1]) not in tower
                and 0 <= e[1] + tmpPos[1] <= 6
                for e in currentShape
            ]
        ):
            pos = tmpPos
        tmpPos = (pos[0] - 1, pos[1])
        if all(
            [(e[0] + tmpPos[0], e[1] + tmpPos[1]) not in tower for e in currentShape]
        ):
            pos = tmpPos
        else:
            moving = False

    if not periodFound and (i % len(elems), windPos % len(line)) in state:
        periodFound = True
        periodState0 = (i, windPos, max)
        stateRev[i] = (i % len(elems), windPos % len(line), max)
    elif (
        periodFound
        and i % len(elems) == periodState0[0] % len(elems)
        and windPos % len(line) == periodState0[1] % len(line)
    ):
        periodState1 = (i, windPos, max)
        stateRev[i] = (i % len(elems), windPos % len(line), max)
        break
    else:
        state.add((i % len(elems), windPos % len(line)))
        stateRev[i] = (i % len(elems), windPos % len(line), max)
    for e in currentShape:
        tower.add((e[0] + pos[0], e[1] + pos[1]))
        if max < e[0] + pos[0]:
            max = e[0] + pos[0]


def printRes(rounds):
    remaining = (rounds - periodState0[0]) % (periodState1[0] - periodState0[0])
    roundHeight = periodState1[2] - periodState0[2]
    print(
        int(
            (rounds - periodState0[0] - remaining)
            / (periodState1[0] - periodState0[0])
            * roundHeight
        )
        + periodState0[2]
        - (
            stateRev[periodState0[0]][2]
            - (
                stateRev[
                    (periodState0[0] + remaining) % (periodState1[0] - periodState0[0])
                ][2]
                + roundHeight
            )
        )
    )


printRes(2022)
printRes(1000000000000)
