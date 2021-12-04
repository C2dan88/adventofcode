def part_1(lines):
    columns = []
    for x in range(0, len(lines[0])):
        bits = ''
        for line in lines:
            bits += line[x]
        columns.append(bits)

    gamma = ''
    epsilon = ''
    for bits in columns:
        ones = bits.count('1')
        zeros = bits.count('0')

        common_bit = '0'
        least_common_bit = '1'
        # swap over bits if ones greater than zero
        if ones > zeros:
            common_bit = '1'
            least_common_bit = '0'

        gamma += common_bit
        epsilon += least_common_bit

    return int(gamma, 2) * int(epsilon, 2)


if __name__ == "__main__":
    f = open('puzzle.txt', 'r')
    lines = [line.strip() for line in f.readlines()]

    print("Part 1:", part_1(lines))
