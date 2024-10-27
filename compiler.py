
instructions = {
    "LDA":	0b00001000,
    "LDB":	0b00010000,
    "LDC":	0b00011000,
    "MOVA":	0b00100000,
    "MOVB":	0b00101000,
    "MOVC":	0b00110000,
    "SETA":	0b00111000,
    "SETB":	0b01000000,
    "SETC":	0b01001000,
    "ADD":	0b01010000,
    "SUB":	0b01011000,
    "AND":	0b01100000,
    "OR":	0b01101000,
    "XOR":	0b01110000,
    "NOT":	0b01111000,
    "HLT":	0b10000000,
    "OUT":	0b10001000,
    "OUTC": 0b11001000,
    "JMP":	0b10010000,
    "JMC":	0b10011000,
    "JMZ":	0b10100000,
    "FLC":	0b10101000,
    "FLZ":	0b10110000,
    "GEC":	0b10111000,
    "GEZ":	0b11000000
}


def translate(code):
    result = []
    markers = {}
    next_markers = []
    next_markers_i = []
    addr = 0
    base_parse = code.split("\n")
    for instruction in base_parse:
        if instruction:
            if instruction[0] == ":":
                marker = instruction[1:]
                markers[marker] = addr
                try:
                    i = next_markers.index(marker)
                    result[next_markers_i[i]] = addr
                except:
                    pass
            else:
                parts = instruction.split(" ")
                result.append(instructions[parts[0]])
                if len(parts) > 1:
                    if parts[1][0] == "$":
                        result.append(int(parts[1][1:])*2-2)
                    elif parts[1][0] == ":":
                        marker = instruction.split(":")
                        try:
                            result.append(markers[marker[1]])
                        except KeyError:
                            result.append(0b00000000)
                            next_markers.append(marker[1])
                            next_markers_i.append(len(result)-1)
                    else:
                        result.append(int(parts[1]))
                    addr += 2
                else:
                    addr += 1
    print(markers)
    return result
