def aoc2a():
    file = open('aoc2.txt').read().splitlines()
    elements = [element.split() for element in file]
    horizontal = 0
    depth = 0
    for i in elements:
        if i[0] == 'forward':
            horizontal += int(i[1])
        elif i[0] == 'up':
            depth -= int(i[1])
        elif i[0] == 'down':
            depth += int(i[1])
    return horizontal * depth

def aoc2b():
    file = open('aoc2.txt').read().splitlines()
    elements = [element.split() for element in file]
    horizontal = 0
    depth = 0
    aim = 0

    for i in elements:
        if i[0] == 'forward':
            horizontal += int(i[1])
            if aim:
                depth = depth + (aim * int(i[1]))
        elif i[0] == 'up':
            aim -= int(i[1])
        elif i[0] == 'down':
            aim += int(i[1])
    return horizontal * depth
