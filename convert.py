import table

TABLE = table.TABLE

def inverse_dic(d):
    return {v: k for k, v in d.items()}


def conv2smile(code, line_length=80):
    converted = ""
    count = 0
    table = inverse_dic(TABLE)
    print(table)
    for ch in code:
        if ch == " " or ch == "\n":
            continue
        print(ch,end="")
        print(table[ch])
        converted += table[ch]
        count += 1
        if count == line_length:
            converted += "\n"
            count = 0
    return converted

def conv2fuck(code, line_length=80):
    converted = ""
    count = 0
    for ch in code:
        if ch == " " or ch == "\n":
            continue
        converted += TABLE[ch]
        count += 1
        if count == line_length:
            converted += "\n"
            count = 0
    return converted