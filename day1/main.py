
def part_1(lines):
    prev_depth = lines[0]
    depth_increases = 0
    for line in lines[1:]:
        if line > prev_depth:
            depth_increases += 1
            #print(f"{line} (increased)")
        prev_depth = line
    print(depth_increases)


if __name__ == "__main__":
    f = open('puzzle.txt', 'r+')
    lines = [int(line) for line in f.readlines()]

    part_1(lines)


