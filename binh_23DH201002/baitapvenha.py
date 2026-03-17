def demkhoangcach(text):
    return text.count(' ')

def demso4(text):
    return text.count('4')

def doichuso(text):
    result = ""
    for char in text:
        if char.isdigit():
            result += "số {0}".format(char)
        else:
            result += char
    return result

input_str = "c734 9bc2 d65ca 92 65bf bc8343 6e5 e868"
print(demkhoangcach(input_str))
print(demso4(input_str))
print(doichuso(input_str))