board = [line.strip("\n") for line in open("24.in")]
maxx = len(board) - 2
maxy = len(board[0]) - 2


class Blizzard:
    def __init__(self, x, y, dir) -> None:
        self.x = x
        self.y = y
        self.dir = dir

    def move(self):
        if self.dir == "^":
            if self.x == 1:
                self.x = maxx
            else:
                self.x -= 1
        elif self.dir == "v":
            if self.x == maxx:
                self.x = 1
            else:
                self.x += 1
        elif self.dir == "<":
            if self.y == 1:
                self.y = maxy
            else:
                self.y -= 1
        elif self.dir == ">":
            if self.y == maxy:
                self.y = 1
            else:
                self.y += 1
        else:
            print("Error")

    def __repr__(self) -> str:
        return f"({self.x} ,  {self.y} : {self.dir} )"


storm = []
# print(list(enumerate([(i, board[i]) for i in range(len(board))])))
for i, line in enumerate(board):
    for j, ch in enumerate(line):
        if ch in ["<", ">", "^", "v"]:
            storm.append(Blizzard(i, j, ch))


def getTo(endx, endy, states):
    minutes = 0
    while True:
        minutes += 1
        for bl in storm:
            bl.move()
        stormSet = {(bl.x, bl.y) for bl in storm}
        # print(stormSet)
        tmpStates = set()
        for state in states:
            if state == (endx, endy):
                return minutes
            if state not in stormSet:
                tmpStates.add(state)
            if state[0] > 1 and (state[0] - 1, state[1]) not in stormSet:
                tmpStates.add((state[0] - 1, state[1]))
            if (
                state[1] > 1
                and state[0] <= maxx
                and (state[0], state[1] - 1) not in stormSet
            ):
                tmpStates.add((state[0], state[1] - 1))
            if (
                state[1] < maxy
                and state[0] > 0
                and (state[0], state[1] + 1) not in stormSet
            ):
                tmpStates.add((state[0], state[1] + 1))
            if state[0] < maxx and (state[0] + 1, state[1]) not in stormSet:
                tmpStates.add((state[0] + 1, state[1]))
        states = tmpStates


state0 = set()
state0.add((0, 1))
minutes1 = getTo(maxx, maxy, state0)
print(minutes1)

state1 = set()
state1.add((maxx, maxy))
minutes2 = getTo(1, 1, state1)

state2 = set()
state2.add((0, 1))
minutes3 = getTo(maxx, maxy, state2)
print(minutes1 + minutes2 + minutes3)
