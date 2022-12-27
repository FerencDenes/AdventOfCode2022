def to10(snafu: str):
    s = 0
    mult = 1
    for c in snafu:
        s *= 5
        if c == "2":
            s += 2
        elif c == "1":
            s += 1
        elif c == "-":
            s -= 1
        elif c == "=":
            s -= 2
    return s


def toSNAFU(number: int) -> str:
    ret = ""
    while number != 0:
        remainder = number % 5
        if remainder < 3:
            ret = str(remainder) + ret
            number = int((number - remainder) / 5)
        elif remainder == 3:
            ret = "=" + ret
            number = int((number + 2) / 5)
        elif remainder == 4:
            ret = "-" + ret
            number = int((number + 1) / 5)
    return ret


numbers = toSNAFU(sum(to10(line.strip()) for line in open("25.in")))
print(numbers)
