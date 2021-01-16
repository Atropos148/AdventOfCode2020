def main():
    import copy
    import os
    # print("Cellular Automata")

    rows = 5
    columns = 5

    board = setup_board(rows, columns)
    for row in board:
        print(board[row])
    input()
    os.system("cls")

    for _ in range(100):
        new_board = copy.deepcopy(board)
        for row in board:
            for index, cell in enumerate(board[row]):
                neighbours = check_neighbours(board, row, index)

                dead_neighbours: int = 0
                alive_neighbours: int = 0
                for neighbour in neighbours:
                    if neighbour == ".":
                        dead_neighbours += 1
                    elif neighbour == "#":
                        alive_neighbours += 1

                if cell == "#":
                    if alive_neighbours == 3 or alive_neighbours == 2:
                        new_board[row][index] = "#"
                    else:
                        new_board[row][index] = "."
                elif cell == ".":
                    if alive_neighbours == 3:
                        new_board[row][index] = "#"
                    else:
                        new_board[row][index] = "."

        board = new_board
        for row in board:
            print(board[row])
        # input()
        os.system("cls")
    input()


def setup_board(rows: int, columns: int) -> dict:
    import random
    board: dict = {}
    for row in range(rows):
        board[row] = []
        for column in range(columns):
            alive: int = random.randint(0, 1)
            if alive:
                board[row].append("#")
            else:
                board[row].append(".")

    return board


def check_neighbours(board: dict, row: int, index: int):
    neighbours: list = []

    exists_up: bool = False
    exists_down: bool = False
    exists_left: bool = False
    exists_right: bool = False

    if row - 1 >= 0:
        up = board[row - 1][index]
        neighbours.append(up)
        exists_up = True
    if row + 1 < len(board.keys()):
        down = board[row + 1][index]
        neighbours.append(down)
        exists_down = True
    if index - 1 >= 0:
        left = board[row][index - 1]
        neighbours.append(left)
        exists_left = True
    if index + 1 < len(board[row]):
        right = board[row][index + 1]
        neighbours.append(right)
        exists_right = True

    if exists_up:
        if exists_left:
            up_left = board[row - 1][index - 1]
            neighbours.append(up_left)
        if exists_right:
            up_right = board[row - 1][index + 1]
            neighbours.append(up_right)

    if exists_down:
        if exists_left:
            down_left = board[row + 1][index - 1]
            neighbours.append(down_left)
        if exists_right:
            down_right = board[row + 1][index + 1]
            neighbours.append(down_right)

    return neighbours


if __name__ == '__main__':
    main()
