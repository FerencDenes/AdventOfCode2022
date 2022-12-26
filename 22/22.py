board = [line.strip("\n") for line in open("22.in")]

rule = board.pop()
# remove empty
board.pop()
boardMax = max(len(row) for row in board)

board = tuple(map(lambda row: row + " " * (boardMax - len(row)), board))


def part1():
    dir = 0
    pos = (0, board[0].index("."))
    # pos = (52, 70)

    rulePos = 0
    num = 0
    while rulePos < len(rule):

        if "0" <= rule[rulePos] <= "9":
            num *= 10
            num += ord(rule[rulePos]) - ord("0")

        elif rulePos >= len(rule) or not "0" <= rule[rulePos] <= "9":
            # step
            for step in range(num):
                if dir == 0:
                    if (
                        pos[1] + 1 >= len(board[pos[0]])
                        or board[pos[0]][pos[1] + 1] == " "
                    ):
                        dotInd = board[pos[0]].index(".")
                        if dotInd > 0 and board[pos[0]][dotInd - 1] == "#":
                            break
                        pos = (pos[0], dotInd)
                    elif board[pos[0]][pos[1] + 1] == ".":
                        pos = (pos[0], pos[1] + 1)
                    else:
                        break
                elif dir == 1:
                    if pos[0] + 1 >= len(board) or board[pos[0] + 1][pos[1]] == " ":
                        p = 0
                        while board[p][pos[1]] != "." and p < len(board):
                            p += 1
                        if p > 0 and board[p - 1][pos[1]] == "#":
                            break
                        pos = (p, pos[1])
                    elif board[pos[0] + 1][pos[1]] == ".":
                        pos = (pos[0] + 1, pos[1])
                    else:
                        break
                elif dir == 2:
                    if pos[1] == 0 or board[pos[0]][pos[1] - 1] == " ":
                        p = len(board[pos[0]]) - 1
                        while p >= 0 and board[pos[0]][p] != ".":
                            p -= 1
                        if p + 1 < len(board[pos[0]]) and board[pos[0]][p + 1] == "#":
                            break
                        pos = (pos[0], p)
                    elif board[pos[0]][pos[1] - 1] == ".":
                        pos = (pos[0], pos[1] - 1)
                    else:
                        break
                elif dir == 3:
                    if pos[0] == 0 or board[pos[0] - 1][pos[1]] == " ":
                        p = len(board) - 1
                        while board[p][pos[1]] != ".":
                            p -= 1
                        if p + 1 < len(board) and board[p + 1][pos[1]] == "#":
                            break
                        pos = (p, pos[1])
                    elif board[pos[0] - 1][pos[1]] == ".":
                        pos = (pos[0] - 1, pos[1])
                    else:
                        break
            # turn
            if rulePos < len(rule):
                # turn
                if rule[rulePos] == "R":
                    dir = (dir + 1) % 4
                elif rule[rulePos] == "L":
                    dir = (dir + 3) % 4
                else:
                    print("Error")
            num = 0
        rulePos += 1

    print((pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + dir)


part1()


def moveTest(p1, p2, dir, side):
    if dir == 0:
        if p2 == side * 3 - 1 and p1 < side:
            if board[side * 3 - 1 - p1][side * 4 - 1] == ".":
                return ((side * 3 - 1 - p1, side * 4 - 1), 2)
        elif p2 == side * 3 - 1 and side * 2 > p1 >= side - 1:
            if board[side * 2][side * 3 + (side * 2 - p1) + 1] == ".":
                return ((side * 2, side * 3 + (side * 2 - p1) + 1), 1)
        elif p2 == side * 4 - 1:
            if board[3 * side - p1 - 1][side * 3 - 1] == ".":
                return ((3 * side - p1 - 1, side * 3 - 1), 2)
        else:
            if board[p1][p2 + 1] == ".":
                return ((p1, p2 + 1), dir)
    elif dir == 1:
        if p1 == side * 2 - 1 and p2 < side:
            if board[side * 3 - 1][side * 3 - p2 - 1] == ".":
                return ((side * 3 - 1, side * 3 - p2 - 1), 3)
        elif p1 == side * 2 - 1 and side <= p2 < 2 * side:
            if board[side * 2 - p2 + side * 2 - 1][side * 2] == ".":
                return ((side * 2 - p2 + side * 2 - 1, side * 2), 0)
        elif p1 == side * 3 - 1 and side * 2 <= p2 <= side * 3:
            if board[side * 2 - 1][side * 3 - p2 - 1] == ".":
                return ((side * 2 - 1, side * 3 - p2 - 1), 3)
        elif p1 == side * 3 - 1 and p2 >= side * 3:
            if board[side * 4 - p2 + side - 1][0] == ".":
                return ((side * 4 - p2 + side - 1, 0), 0)
        else:
            if board[p1][p2 + 1] == ".":
                return ((p1 + 1, p2), 1)
    elif dir == 2:
        if p1 < side and p2 == 2 * side:
            if board[side][side + p1]:
                return ((side, side + p1), 1)
        elif side <= p1 < 2 * side and p2 == 0:
            if board[3 * side - 1][3 * side + 2 * side - p1 - 1] == ".":
                return ((3 * side - 1, 3 * side + 2 * side - p1 - 1), 3)
        elif p1 > side * 2 and p2 == 2 * side:
            if board[2 * side - 1][2 * side + 2 * side - p1 - 1] == ".":
                return ((2 * side - 1, 2 * side + 2 * side - p1 - 1), 3)
        else:
            if board[p1][p2 - 1] == ".":
                return ((p1, p2 - 1), 2)
    elif dir == 3:
        if p1 == side and p2 < side:
            if board[0][3 * side - p2 - 1] == ".":
                return ((0, 3 * side - p2 - 1), 1)
        elif p1 == side and side <= p2 < 2 * side:
            if board[p2 - side][2 * side] == ".":
                return ((p2 - side, 2 * side), 0)
        elif p1 == 0:
            if board[side][3 * side - p2 - 1] == ".":
                return ((side, 3 * side - p2 - 1), 1)
        elif p1 == 3 * side and 3 * side <= p2:
            if board[3 * side - p2 + 2 * side - 1][3 * side - 1] == ".":
                return ((3 * side - p2 + 2 * side - 1, 3 * side - 1), 2)
        else:
            if board[p1 - 1][p2] == ".":
                return ((p1 - 1, p2), 3)
    return None


def move(p1, p2, dir, side):
    if dir == 0:
        if p2 == side * 3 - 1 and p1 < side:
            if board[3 * side - p1 - 1][side * 2 - 1] == ".":
                return ((3 * side - p1 - 1, side * 2 - 1), 2, 1)
        elif p2 == side * 2 - 1 and side * 2 > p1 >= side:
            if board[side - 1][side + p1] == ".":
                return ((side - 1, side + p1), 3, 2)
        elif p2 == side * 2 - 1 and side * 2 <= p1 < side * 3:
            if board[3 * side - p1 - 1][side * 3 - 1] == ".":
                return ((3 * side - p1 - 1, side * 3 - 1), 2, 3)
        elif p2 == side - 1 and p1 >= 3 * side:
            if board[3 * side - 1][p1 - side * 2] == ".":
                return ((3 * side - 1, p1 - side * 2), 3, 3)
        else:
            if board[p1][p2 + 1] == ".":
                return ((p1, p2 + 1), 0, 4)
    elif dir == 1:
        if p1 == side * 4 - 1:
            if board[0][side * 2 + p2] == ".":
                return ((0, side * 2 + p2), 1, 5)
        elif p1 == side * 3 - 1 and side <= p2 < 2 * side:
            if board[p2 + 2 * side][side - 1] == ".":
                return ((p2 + 2 * side, side - 1), 2, 6)
        elif p1 == side - 1 and side * 2 <= p2:
            if board[p2 - side][side * 2 - 1] == ".":
                return ((p2 - side, side * 2 - 1), 2, 7)
        else:
            if board[p1 + 1][p2] == ".":
                return ((p1 + 1, p2), 1, 8)
    elif dir == 2:
        if p1 < side and p2 == side:
            if board[3 * side - p1 - 1][0] == ".":
                return ((3 * side - p1 - 1, 0), 0, 9)
        elif side <= p1 < 2 * side and p2 == side:
            if board[2 * side][p1 - side] == ".":
                return ((2 * side, p1 - side), 1, 10)
        elif side * 3 > p1 >= side * 2 and p2 == 0:
            if board[3 * side - p1 - 1][side] == ".":
                return ((3 * side - p1 - 1, side), 0, 11)
        elif side * 3 <= p1 and p2 == 0:
            if board[0][p1 - side * 2] == ".":
                return ((0, p1 - side * 2), 1, 18)
        else:
            if board[p1][p2 - 1] == ".":
                return ((p1, p2 - 1), 2, 12)
    elif dir == 3:
        if p1 == side * 2 and p2 < side:
            if board[p2 + side][side] == ".":
                return ((p2 + side, side), 0, 13)
        elif p1 == 0 and side <= p2 < 2 * side:
            if board[p2 + 2 * side][0] == ".":
                return ((p2 + 2 * side, 0), 0, 14)
        elif p1 == 0 and 2 * side <= p2:
            if board[4 * side - 1][p2 - 2 * side] == ".":
                return ((4 * side - 1, p2 - 2 * side), 3, 15)
        else:
            if board[p1 - 1][p2] == ".":
                return ((p1 - 1, p2), 3, 17)
    return None


def part2():
    errcnt = 0
    side = int(len(board[len(board) - 1]) / 3)
    dir = 0
    pos = (0, board[0].index("."))

    rulePos = 0
    num = 0
    while rulePos <= len(rule):
        if rulePos < len(rule) and "0" <= rule[rulePos] <= "9":
            num *= 10
            num += ord(rule[rulePos]) - ord("0")

        elif rulePos >= len(rule) or not "0" <= rule[rulePos] <= "9":
            # step
            for step in range(num):
                tmp = move(pos[0], pos[1], dir, side)
                if None == tmp:
                    break
                else:
                    (pos, dir, rn) = tmp
                    if board[pos[0]][pos[1]] != ".":
                        print("Error", pos, dir, rn)
                        errcnt += 1
            # turn
            if rulePos < len(rule):
                # turn
                if rule[rulePos] == "R":
                    dir = (dir + 1) % 4
                elif rule[rulePos] == "L":
                    dir = (dir + 3) % 4
                else:
                    print("Error")
            num = 0
        rulePos += 1

    print((pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + dir)


part2()
