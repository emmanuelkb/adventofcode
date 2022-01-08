def aoc1a():
    file = open('aoc1.txt').read().splitlines()
    elements = [int(numbers) for numbers in file]
    temp = 0
    for number in range(len(elements)):
        if elements[number] > elements[number - 1]:
            temp += 1
    return temp


def aoc1b():
    file = open('aoc1.txt').read().splitlines()
    elements = [int(numbers) for numbers in file]
    temp = 0
    for number in range(len(elements)):
        if elements[number] < elements[len(elements) - 3]:
            if elements[number + 1] + elements[number + 2] + elements[number + 3] > elements[number] + elements[
                number + 1] + elements[number + 2]:
                temp += 1
    return temp
