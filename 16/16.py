#!/opt/homebrew/bin/python
import re

input = open("16.in", "r")


class Valve:
    def __init__(self, rate, to) -> None:
        self.rate = int(rate)
        self.to = to.split(", ")
        self.closed = True


def parse(line):
    x = re.search(
        r"Valve (..) has flow rate=(.+); tunnel.? lead.? to valve.? (.+)", line
    )
    return (x.group(1), Valve(x.group(2), x.group(3)))


valvesTmp = {line[0]: line[1] for line in map(parse, input)}
valveNames = list(valvesTmp.keys())
valveNames.sort()

valves = {i: valvesTmp[valveName] for i, valveName in enumerate(valveNames)}
valveRates = tuple(valvesTmp[vn].rate for vn in valveNames)

for i in range(len(valveNames)):
    valves[i].to = list(
        map(lambda x, valveNames=valveNames: valveNames.index(x), valves[i].to)
    )


def part1():
    states = {(0, valveRates): 0}

    for i in range(29, -1, -1):
        statesTmp = {}
        for current, value in states.items():
            tos = valves[current[0]].to
            # do not open, go forward
            for to in tos:
                statesTmp[(to, current[1])] = max(
                    value,
                    statesTmp[(to, current[1])] if (to, current[1]) in statesTmp else 0,
                )
            # open valve
            if current[1][current[0]] > 0:
                newRates = []
                for j in range(len(current[1])):
                    newRates.append(0 if j == current[0] else current[1][j])
                newRates = tuple(newRates)
                statesTmp[(current[0], newRates)] = max(
                    value + current[1][current[0]] * i,
                    statesTmp[(current[0], newRates)]
                    if (current[0], newRates) in statesTmp
                    else 0,
                )
        states = statesTmp

    maxVal = 0
    for value in states.values():
        if maxVal < value:
            maxVal = value
    print(maxVal)


part1()


def part2():
    states = {((0, 0), valveRates): 0}
    visited = states.copy()
    for i in range(25, -1, -1):
        statesTmp = {}
        for current, value in states.items():
            tos0 = valves[current[0][0]].to
            tos1 = valves[current[0][1]].to
            # do not open, go forward
            for to0 in tos0:
                for to1 in tos1:
                    newState = ((min(to0, to1), max(to0, to1)), current[1])
                    newValue = max(
                        value,
                        statesTmp[newState] if newState in statesTmp else 0,
                    )
                    prevValue = visited.get(newState)
                    if prevValue == None or newValue > prevValue:
                        statesTmp[newState] = newValue
            # open both valves
            if (
                current[1][current[0][0]] > 0
                and current[1][current[0][1]] > 0
                and current[0][1] != current[0][0]
            ):
                newRates = []
                for j in range(len(current[1])):
                    newRates.append(
                        0 if j == current[0][0] or j == current[0][1] else current[1][j]
                    )
                newRates = tuple(newRates)
                newState = (
                    (
                        min(current[0][0], current[0][1]),
                        max(current[0][0], current[0][1]),
                    ),
                    newRates,
                )
                newValue = max(
                    value + (current[1][current[0][0]] + current[1][current[0][1]]) * i,
                    statesTmp[newState] if newState in statesTmp else 0,
                )
                prevValue = visited.get(newState)
                if prevValue == None or newValue > prevValue:
                    statesTmp[newState] = newValue

            if current[1][current[0][0]] > 0:
                newRates = []
                for j in range(len(current[1])):
                    newRates.append(0 if j == current[0][0] else current[1][j])
                newRates = tuple(newRates)
                tos1 = valves[current[0][1]].to
                for to1 in tos1:
                    newState = (
                        (min(current[0][0], to1), max(current[0][0], to1)),
                        newRates,
                    )
                    newValue = max(
                        value + (current[1][current[0][0]]) * i,
                        statesTmp[newState] if newState in statesTmp else 0,
                    )
                    prevValue = visited.get(newState)
                    if prevValue == None or newValue > prevValue:
                        statesTmp[newState] = newValue

            if current[1][current[0][1]] > 0:
                newRates = []
                for j in range(len(current[1])):
                    newRates.append(0 if j == current[0][1] else current[1][j])
                newRates = tuple(newRates)
                tos0 = valves[current[0][0]].to
                for to0 in tos0:
                    newState = (
                        (min(to0, current[0][1]), max(to0, current[0][1])),
                        newRates,
                    )
                    newValue = max(
                        value + (current[1][current[0][1]]) * i,
                        statesTmp[newState] if newState in statesTmp else 0,
                    )
                    prevValue = visited.get(newState)
                    if prevValue == None or newValue > prevValue:
                        statesTmp[newState] = newValue

        states = statesTmp
        for k, v in states.items():
            visited[k] = v
    maxVal = 0
    for value in states.values():
        if maxVal < value:
            maxVal = value
    print(maxVal)


part2()
