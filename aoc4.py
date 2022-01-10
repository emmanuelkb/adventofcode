data = open('aoc4.txt').read().splitlines()

def aoc4a():
    order = data[0].split(',')
    for i in data[2:]:
        print(i)
