def main():
	# Solution for Day 11 of Advent od Code 2020
	# Link: https://adventofcode.com/2020/day/11
	print("Seat occupation prediction")

	input_seats_test: str = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''

	cleaned_seats_test = input_seats_test.split("\n")

	seats_dict_test = create_seats_dict(cleaned_seats_test)
	print(seats_dict_test)
	seats_dict_test = check_around_seat((1, 1), seats_dict_test)
	print(seats_dict_test)


def create_seats_dict(seats_list: list) -> dict:
	seats_dict: dict = {}
	for index, row in enumerate(seats_list):
		seats_dict[index] = []
		for character in seats_list[index]:
			seats_dict[index].append(character)

	return seats_dict


def check_around_seat(seat_position: tuple, seats_dict: dict) -> (dict):
	seat_row = seat_position[0]
	seat_column = seat_position[1]
	middle_seat = seats_dict[seat_row][seat_column]

	up_left: tuple = (seat_row - 1, seat_column - 1)
	up: tuple = (seat_row - 1, seat_column)
	up_right: tuple = (seat_row - 1, seat_column + 1)
	left: tuple = (seat_row, seat_column - 1)
	right: tuple = (seat_row, seat_column + 1)
	down_left: tuple = (seat_row + 1, seat_column - 1)
	down: tuple = (seat_row + 1, seat_column)
	down_right: tuple = (seat_row + 1, seat_column + 1)

	directions_to_check: list = [up_left, up, up_right, left, right, down_left, down, down_right]

	try:
		if middle_seat != ".":
			empty_seats: int = 0
			filled_seats: int = 0
			floor_tiles: int = 0
			for direction in directions_to_check:
				checked_seat = seats_dict[direction[0]][direction[1]]
				if checked_seat == "L":
					empty_seats += 1
				elif checked_seat == "#":
					filled_seats += 1
				else:
					floor_tiles += 1

			if middle_seat == "L":
				if empty_seats + floor_tiles == len(directions_to_check):
					seats_dict[seat_row][seat_column] = "#"

			else:
				if filled_seats >= 4:
					seats_dict[seat_row][seat_column] = "L"

		return (seats_dict)


	except KeyError:
		pass


if __name__ == '__main__':
	main()
