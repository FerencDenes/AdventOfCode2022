input = [int(line) for line in open("20.in")]

input = [(v, i) for i, v in enumerate(input)]

originalPos = input.copy()


def mix(input, originalPos, iter):
    for _ in range(iter):
        for _, val in enumerate(originalPos):
            pos = input.index(val)
            input.pop(pos)
            newPos = (pos + val[0]) % len(input)
            input.insert(newPos, val)

    i = 0
    while input[i][0] != 0:
        i += 1
    return sum([input[(v + i) % len(input)][0] for v in (1000, 2000, 3000)])


print(mix(input, originalPos, 1))

originalPos = [(v[0] * 811589153, v[1]) for v in originalPos]
input = originalPos.copy()
print(mix(input, originalPos, 10))
