input = {l[0]: l[1] for l in [line.strip().split(": ") for line in open("21.in")]}
origin = input.copy()


def val(key: str) -> int:
    v = input[key]
    if isinstance(v, str):
        tokens = v.split()
        if len(tokens) == 1:
            input[key] = int(tokens[0])
        elif tokens[1] == "+":
            input[key] = val(tokens[0]) + val(tokens[2])
        elif tokens[1] == "-":
            input[key] = val(tokens[0]) - val(tokens[2])
        elif tokens[1] == "*":
            input[key] = val(tokens[0]) * val(tokens[2])
        elif tokens[1] == "/":
            input[key] = val(tokens[0]) / val(tokens[2])
        else:
            print("Error")
    return input[key]


print(int(val("root")))


input = origin.copy()
root = input["root"].split()


def val2(humn: int) -> int:
    global input
    input = origin.copy()
    input["humn"] = humn
    return val(root[0]) - val(root[2])


max = 100000000000000
up = max
down = -max
mid = 0
mv = val2(mid)

while mv != 0:
    vu = val2(up)
    vd = val2(down)
    if mv * vu > 0:
        up = mid
    elif mv * vd > 0:
        down = mid
    else:
        print("Error 2")
    mid = int((up + down) / 2)
    mv = val2(mid)


print(mid)
