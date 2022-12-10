#!/opt/homebrew/bin/python

input = open("10.in", "r")

time = 1
x = 1
ticks = 20
sum = 0
img = ["_" for _ in range(240)]


def noteSignal(t, v):
    global ticks, sum, x
    if t == ticks:
        sum += t * v
        ticks += 40
    if ticks > 220:
        ticks = -1
    if (time - 1) % 40 >= x - 1 and (time - 1) % 40 <= x + 1:
        img[time - 2] = "X"
    else:
        img[time - 2] = "."


for line in input:
    if line.startswith("noop"):
        time += 1
        noteSignal(time, x)
    else:
        time += 1
        noteSignal(time, x)
        val = int(line.split(" ")[1])
        x += val
        time += 1
        noteSignal(time, x)

print(sum)
for i, val in enumerate(img):
    print(val, end="")
    if i % 40 == 39:
        print()
