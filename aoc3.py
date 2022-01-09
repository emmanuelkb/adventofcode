data = open('aoc3.txt').read().splitlines()


def aoc3a():
    gamma = ''
    epsilon = ''
    for i in range(len(data[0])):
        zeros = 0
        ones = 0
        for number in data:
            if number[i] == '0':
                zeros += 1
            else:
                ones += 1

        if zeros > ones:
            gamma += '0'
            epsilon += '1'
        elif ones > zeros:
            gamma += '1'
            epsilon += '0'

    power_consumption = int(epsilon, 2) * int(gamma, 2)
    return power_consumption


def aoc3b():
    i = 0
    data = open('aoc3.txt').read().splitlines()
    co2data = data.copy()

    while len(data) > 1:
        zeros = 0
        ones = 0
        for number in data:
            if number[i] == '0':
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            data = [number for number in data if number[i] == '0']
        else:
            data = [number for number in data if number[i] == '1']

        i += 1

    i = 0
    while len(co2data) > 1:
        zeros = 0
        ones = 0
        for number in co2data:
            if number[i] == '0':
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            co2data = [number for number in co2data if number[i] == '1']
        else:
            co2data = [number for number in co2data if number[i] == '0']

        i += 1

    return int("".join(data), 2)* int("".join(co2data), 2)
