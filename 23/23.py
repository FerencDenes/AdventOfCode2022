board = [line.strip("\n") for line in open("23.in")]


class Elf:
    def __init__(self, x, y) -> None:
        self.i = x
        self.j = y


elves = []
for i, line in enumerate(board):
    for j, ch in enumerate(line):
        if ch == "#":
            elves.append(Elf(i, j))

moved = True
round = 0
while moved:
    places = {(elf.i, elf.j) for elf in elves}
    considered = dict()
    moved = False
    for elf in elves:
        elf.c = None
        if not (
            (elf.i - 1, elf.j - 1) not in places
            and (elf.i - 1, elf.j) not in places
            and (elf.i - 1, elf.j + 1) not in places
            and (elf.i, elf.j - 1) not in places
            and (elf.i, elf.j + 1) not in places
            and (elf.i + 1, elf.j - 1) not in places
            and (elf.i + 1, elf.j) not in places
            and (elf.i + 1, elf.j + 1) not in places
        ):
            for d in range(round, round + 4):
                if d % 4 == 0:
                    if (
                        (elf.i - 1, elf.j - 1) not in places
                        and (elf.i - 1, elf.j) not in places
                        and (elf.i - 1, elf.j + 1) not in places
                    ):
                        elf.c = (elf.i - 1, elf.j)
                        considered[elf.c] = considered.get(elf.c, 0) + 1
                        break
                if d % 4 == 1:
                    if (
                        (elf.i + 1, elf.j - 1) not in places
                        and (elf.i + 1, elf.j) not in places
                        and (elf.i + 1, elf.j + 1) not in places
                    ):
                        elf.c = (elf.i + 1, elf.j)
                        considered[elf.c] = considered.get(elf.c, 0) + 1
                        break
                if d % 4 == 2:
                    if (
                        (elf.i + 1, elf.j - 1) not in places
                        and (elf.i, elf.j - 1) not in places
                        and (elf.i - 1, elf.j - 1) not in places
                    ):
                        elf.c = (elf.i, elf.j - 1)
                        considered[elf.c] = considered.get(elf.c, 0) + 1
                        break
                if d % 4 == 3:
                    if (
                        (elf.i + 1, elf.j + 1) not in places
                        and (elf.i, elf.j + 1) not in places
                        and (elf.i - 1, elf.j + 1) not in places
                    ):
                        elf.c = (elf.i, elf.j + 1)
                        considered[elf.c] = considered.get(elf.c, 0) + 1
                        break

    for elf in elves:
        if elf.c is not None and considered[(elf.c)] == 1:
            elf.i = elf.c[0]
            elf.j = elf.c[1]
            moved = True
    round += 1
    if round == 10:
        mini = 100000000
        minj = 100000000
        maxi = -100000000
        maxj = -100000000
        for elf in elves:
            mini = min(elf.i, mini)
            minj = min(elf.j, minj)
            maxi = max(elf.i, maxi)
            maxj = max(elf.j, maxj)

        print((maxi - mini + 1) * (maxj - minj + 1) - len(places))


print(round)
