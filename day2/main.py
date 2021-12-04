
def part_1(instructions):
    horizontal = 0
    depth = 0

    for [direction, length] in instructions:
        if direction == 'forward':
            horizontal += length
        elif direction == 'up':
            depth -= length
        elif direction == 'down':
            depth += length

    return horizontal * depth


def part_2(instructions):
    horizontal = 0
    depth = 0
    aim = 0

    for [direction, length] in instructions:
        if direction == 'forward':
            horizontal += length
            depth += aim * length
        elif direction == 'up':
            aim -= length
        elif direction == 'down':
            aim += length

    return horizontal * depth


if __name__ == "__main__":
    f = open('puzzle.txt', 'r')
    lines = []
    for line in f.readlines():
        [direction, length] = line.strip().split(' ')
        lines.append([direction, int(length)])

    print("Part 1:", part_1(lines))
    print("Part 2:", part_2(lines))



