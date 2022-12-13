import functools

input = open("13.in", "r")

lines = list(input)

# +1 if in right order, -1 if wrong
def compare(left, right):
    if type(left) == int and type(right) == int:
        return right - left
    if type(left) == list and type(right) == int:
        return compare(left, [right])
    if type(left) == int and type(right) == list:
        return compare([left], right)
    for i in range(min(len(left), len(right))):
        cmp = compare(left[i], right[i])
        if cmp != 0:
            return cmp
    return len(right) - len(left)


def parse(line, pos):
    ret = list()
    valSet = False
    val = 0
    while True:
        pos += 1
        if line[pos] == "[":
            p = parse(line, pos)
            pos = p[1]
            ret.append(p[0])
        elif "0" <= line[pos] <= "9":
            valSet = True
            val *= 10
            val += ord(line[pos]) - ord("0")
        elif line[pos] == "," and valSet:
            ret.append(val)
            valSet = False
            val = 0
        elif line[pos] == "]":
            if valSet:
                ret.append(val)
            return (ret, pos)


lineno = 0
sum = 0

signals = list()
while lineno < len(lines):
    l1 = parse(lines[lineno], 0)
    l2 = parse(lines[lineno + 1], 0)
    signals.append(l1[0])
    signals.append(l2[0])

    if compare(l1[0], l2[0]) > 0:
        sum += int(lineno / 3) + 1
    lineno += 3

print(sum)
signals.append(parse("[[2]]", 0)[0])
signals.append(parse("[[6]]", 0)[0])
sorted_signals = sorted(signals, key=functools.cmp_to_key(compare), reverse=True)

print((sorted_signals.index([[2]]) + 1) * (sorted_signals.index([[6]]) + 1))
