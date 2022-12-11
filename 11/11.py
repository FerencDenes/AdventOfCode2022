#!/opt/homebrew/bin/python


class Monkey:
    def __init__(self, items, expr, div, tm, fm):
        self.items = items
        self.expr = compile(expr, "<string>", "eval")
        self.div = div
        self.tm = tm
        self.fm = fm
        self.observed = 0


monkeys = []
monkeys2 = []

input = open("11.in", "r")

proddiv = 1
line = input.readline()
while line != "":
    line = input.readline()
    items = [int(e) for e in line.split(":")[1].split(",")]
    line = input.readline()
    expr = line.split("= ")[1]
    line = input.readline()
    div = int(line.split(" by ")[1])
    proddiv *= div
    line = input.readline()
    tm = int(line.split(" monkey ")[1])
    line = input.readline()
    fm = int(line.split(" monkey ")[1])
    monkey = Monkey(items, expr, div, tm, fm)
    monkeys.append(monkey)
    monkeys2.append(Monkey(items.copy(), expr, div, tm, fm))
    line = input.readline()
    line = input.readline()

for _ in range(20):
    for monkey in monkeys:
        for item in monkey.items:
            newval = eval(monkey.expr, {"old": item})
            newval = int(newval / 3)
            if newval % monkey.div == 0:
                monkeys[monkey.tm].items.append(newval)
            else:
                monkeys[monkey.fm].items.append(newval)

        monkey.observed += len(monkey.items)
        monkey.items.clear()

obs = [monkey.observed for monkey in monkeys]
obs.sort(reverse=True)
print(obs[0] * obs[1])

for x in range(10000):
    for monkey in monkeys2:
        for item in monkey.items:
            newval = eval(monkey.expr, {"old": item}) % proddiv
            # newval = int(newval / 3)
            if newval % monkey.div == 0:
                monkeys2[monkey.tm].items.append(newval)
            else:
                monkeys2[monkey.fm].items.append(newval)

        monkey.observed += len(monkey.items)
        monkey.items.clear()

obs = [monkey.observed for monkey in monkeys2]
obs.sort(reverse=True)
print(obs[0] * obs[1])
