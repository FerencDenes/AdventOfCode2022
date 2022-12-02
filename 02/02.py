#!/opt/homebrew/bin/python

input = open("02.in", "r")

sum = 0
sum2 = 0
for line in input:
    if line[2] == "X":
        sum += 1
        if line[0] == "A":
            sum += 3
            sum2 += 3
        elif line[0] == "B":
            sum2 += 1
        elif line[0] == "C":
            sum += 6
            sum2 += 2
    elif line[2] == "Y":
        sum += 2
        sum2 += 3
        if line[0] == "B":
            sum += 3
            sum2 += 2
        elif line[0] == "A":
            sum += 6
            sum2 += 1
        elif line[0] == "C":
            sum2 += 3
    elif line[2] == "Z":
        sum += 3
        sum2 += 6
        if line[0] == "C":
            sum += 3
            sum2 += 1
        elif line[0] == "B":
            sum += 6
            sum2 += 3
        elif line[0] == "A":
            sum2 += 2

print(sum)
print(sum2)
