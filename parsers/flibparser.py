from utils.exceptions import InvalidFormat
from operator import itemgetter


def FlibParser(input):
    contents = input.split('\n')
    output = []

    for line in contents:
        line = line.lstrip().split()
        if not line or line[0].isalpha() or len(line) != 3:
            continue
        elif line[0].isdigit() and line[1].isdigit():
            if abs(int(line[0]) - int(line[1])) >= 5:
                output.append((int(line[0]), int(line[1]), float(line[2])))

    if not output:
        raise InvalidFormat('Unable to parse contacts')
    else:
        output = sorted(output, key=itemgetter(2), reverse=True)
        return output