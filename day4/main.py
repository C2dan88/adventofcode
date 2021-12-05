import re, copy


class Tile:
    def __init__(self, value):
        self.value = int(value)
        self.marked = False

    def cross_off(self):
        self.marked = True

    def is_marked(self):
        return self.marked

    def __int__(self):
        return self.value

    def __str__(self):
        return str(self.value) if self.is_marked() else '--'


def part_1(numbers, boards):
    for chosen_number in numbers:
        markup_tiles(boards, chosen_number)
        for (board_index, winning_board) in check_for_win(boards):
            print(f"Winning Board: {board_index}")
            unmarked_score = calculate_unmarked(winning_board)
            return unmarked_score * chosen_number


def part_2(bingo_numbers, boards):
    for chosen_number in bingo_numbers:
        markup_tiles(boards, chosen_number)
        for (board_index, winning_board) in check_for_win(boards):
            print(f"Winning Board: {board_index}")
            print(f"Bingo Number: {chosen_number}")
            unmarked_score = calculate_unmarked(winning_board) * chosen_number
            print(f"Score: {unmarked_score}")
            print("----------")

    return unmarked_score


def calculate_unmarked(board):
    print_board(board)
    unmarked = 0
    for line in board:
        for tile in line:
            if not tile.is_marked():
                unmarked += int(tile)

    return unmarked


def check_for_win(boards):
    won = False
    for board_index, board in list(boards.items()):
        # check rows
        for line in board:
            count = list(filter(lambda tile: tile.is_marked(), line))
            if len(count) == BOARD_SIZE:
                # remove board from play
                boards.pop(board_index)
                # yield the board
                yield board_index, board

        # check vertical
    for board_index, board in list(boards.items()):
        for x in range(BOARD_SIZE):
            count = 0
            for line in board:
                count += 1 if line[x].is_marked() else 0
            if count == BOARD_SIZE:
                # remove board from play
                boards.pop(board_index)
                # yield the board
                yield board_index, board



def print_board(board):
    for line in board:
        for tile in line:
            print(str(tile).rjust(2), end=' ')
        print()


def print_boards(boards):
    for board in boards:
        print_board(board)



def markup_tiles(boards, number):
    for k, board in boards.items():
        for line in board:
            for tile in line:
                if int(tile) == number:
                    tile.cross_off()


if __name__ == "__main__":
    f = open('puzzle.txt', 'r')
    lines = [line.strip() for line in f.readlines()]
    numbers = [int(x) for x in lines[0].split(',')]

    BOARD_SIZE = 5

    bingo_boards = {}
    bingo_board = []
    x = 0
    for line in lines[1:]:
        if line != '':
            bingo_board.append([Tile(tile_value) for tile_value in re.split(r'\s+', line)])

        if len(bingo_board) == BOARD_SIZE:
            bingo_boards[x] = bingo_board
            x += 1
            bingo_board = []

    bingo_boards2 = copy.deepcopy(bingo_boards)  # hack ^_^ shallowcopy vs deepcopy!!! :/

    print("Part 1:", part_1(numbers, bingo_boards))
    print("Part 2:", part_2(numbers, bingo_boards2))
