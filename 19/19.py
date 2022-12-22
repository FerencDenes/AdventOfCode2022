import re

input = open("19.in", "r")


def codify(name: str) -> int:
    return (
        0 if name == "ore" else 1 if name == "clay" else 2 if name == "obsidian" else 3
    )


def more(a, b):
    return all(x <= y for x, y in zip(a, b))


def minus(a, b):
    return tuple(x - y for x, y in zip(a, b))


part1 = 0
part2 = 1
for line in input:
    ruleNum = int(re.search(r"Blueprint (\d+):", line).group(1))

    matchedRules = [
        re.search(r"Each (.+) robot costs (.+)", rule)
        for rule in line.strip().split(". ")
    ]
    prices = {}
    for mr in matchedRules:
        tmp = map(
            lambda x: (int(x.group(1)), codify(x.group(2))),
            [re.search(r"(\d+) ([a-z]+)", pr) for pr in mr.group(2).split(" and ")],
        )
        tmp2 = [0, 0, 0, 0]
        for v in tmp:
            tmp2[v[1]] = v[0]
        prices[codify(mr.group(1))] = tuple(tmp2)
    maxRobots = [val for val in prices.values()]
    maxRobots = [
        max(v) for v in zip(maxRobots[0], maxRobots[1], maxRobots[2], maxRobots[3])
    ]
    # ore, clay, obs, geode
    states = set()
    states.add(((1, 0, 0, 0), (0, 0, 0, 0)))
    endMinute = 32 if ruleNum <= 3 else 24
    for minute in range(endMinute):
        tmpStates = set()
        for state in states:
            # do not need more, than we can consume
            ores = tuple(
                min(
                    a + b,
                    a + b if i == 3 else ((endMinute - minute) * maxRobots[i]),
                )
                for i, (a, b) in enumerate(zip(state[0], state[1]))
            )
            tmpStates.add((state[0], ores))
            for robotNo, robot in prices.items():
                # do not need more robots than we can consume output of them
                if (robotNo == 3 or maxRobots[robotNo] > state[0][robotNo]) and more(
                    robot, state[1]
                ):
                    newState = (
                        tuple(
                            e + (1 if robotNo == i else 0)
                            for i, e in enumerate(state[0])
                        ),
                        minus(ores, robot),
                    )
                    tmpStates.add(newState)

        states = tmpStates
        if minute == 23:
            bpMax = max(state[1][3] for state in states)

    part1 += ruleNum * bpMax
    part2 *= 1 if ruleNum > 3 else max(state[1][3] for state in states)


print(part1)
print(part2)
