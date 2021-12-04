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


def get_column_bits(lines, col_n):
    column = ''
    for line in lines:
        column += line[col_n]

    return column


def get_co2_scrubber_rating(lines):
    for x in range(len(lines[0])):
        bits = get_column_bits(lines, x)
        ones = bits.count('1')
        zeros = bits.count('0')

        common_bit = '1'
        if ones > zeros or ones == zeros:
            common_bit = '0'

        # filter lines by common bit
        lines = list(filter(lambda line: line[x] == common_bit, lines))

        if len(lines) == 1:
            return int(lines[0], 2)


def get_oxygen_rating(lines):
    for x in range(len(lines[0])):
        bits = get_column_bits(lines, x)
        ones = bits.count('1')
        zeros = bits.count('0')

        common_bit = '0'
        if ones > zeros or ones == zeros:
            common_bit = '1'

        # filter lines by common bit
        lines = list(filter(lambda line: line[x] == common_bit, lines))

        if len(lines) == 1:
            return int(lines[0], 2)

def part_2(lines):

    oxygen = get_oxygen_rating(lines)
    scrubber = get_co2_scrubber_rating(lines)

    return oxygen * scrubber



if __name__ == "__main__":
    f = open('puzzle.txt', 'r')
    lines = [line.strip() for line in f.readlines()]

    print("Part 1:", part_1(lines))
    print("Part 2:", part_2(lines))

