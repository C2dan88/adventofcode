
def part_1(depths):
    prev_depth = depths[0]
    total = 0
    for depth in depths[1:]:
        if depth > prev_depth:
            total += 1
            #print(f"{line} (increased)")
        prev_depth = depth
    return total


def part_2(lines):
    n = 3  # window size
    window_depths = [sum(lines[i:i + n]) for i in range(0, len(lines))]
    return part_1(window_depths)


if __name__ == "__main__":
    f = open('puzzle.txt', 'r+')
    lines = [int(line) for line in f.readlines()]

    print("Part 1:", part_1(lines))
    print("Part 2:", part_2(lines))


