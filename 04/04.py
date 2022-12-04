#!/opt/homebrew/bin/python

input = open("04.in", "r")

sum = 0
sum2 = 0
for line in input:
    [a, b] = line.split(",")
    [x1, y1] = [int(s) for s in a.split("-")]
    [x2, y2] = [int(s) for s in b.split("-")]
    if (x1 <= x2 and y1 >= y2) or (x1 >= x2 and y1 <= y2):
        sum += 1
    if (
        (x2 >= x1 and x2 <= y1)
        or (y2 >= x1 and y2 <= y1)
        or (x1 >= x2 and x1 <= y2)
        or (y1 >= x2 and y1 <= y2)
    ):
        sum2 += 1
print(sum)
print(sum2)
