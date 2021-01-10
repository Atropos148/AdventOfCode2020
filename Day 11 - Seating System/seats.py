import copy


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

	seats_dict_test_changed = check_all_seats(seats_dict_test)

	occupied_seats_current = 0
	occupied_seats_last = count_occupied_seats(seats_dict_test_changed)

	# for row in seats_dict_test_changed:
	# 	print(seats_dict_test_changed[row])

	while occupied_seats_current != occupied_seats_last:
		occupied_seats_last = occupied_seats_current
		occupied_seats_current, seats_dict_test_changed = another_round(seats_dict_test_changed)
	print(f"final: {occupied_seats_current}")


def create_seats_dict(seats_list: list) -> dict:
	seats_dict: dict = {}
	for index, row in enumerate(seats_list):
		seats_dict[index] = []
		for character in seats_list[index]:
			seats_dict[index].append(character)

	return seats_dict


def check_around_seat(seat_position: tuple, seats_dict: dict) -> str:
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

	seat_state: str = middle_seat

	if middle_seat != ".":
		empty_seats: int = 0
		filled_seats: int = 0
		floor_tiles: int = 0
		checked_tiles: int = 0
		for direction in directions_to_check:
			if direction[0] in seats_dict.keys():
				if 0 <= direction[1] <= len(seats_dict[direction[0]]) - 1:
					checked_tiles += 1
					checked_seat = seats_dict[direction[0]][direction[1]]
					if checked_seat == "L":
						empty_seats += 1
					elif checked_seat == "#":
						filled_seats += 1
					else:
						floor_tiles += 1

		if middle_seat == "L":
			if empty_seats + floor_tiles == checked_tiles:
				seat_state = "#"

		else:
			if filled_seats >= 4:
				seat_state = "L"
	else:
		seat_state = "."

	return seat_state


def check_all_seats(seats_dict: dict) -> dict:
	seats_dict_final = copy.deepcopy(seats_dict)
	for row in seats_dict:
		for column, seat in enumerate(seats_dict[row]):
			seat_state = check_around_seat((row, column), seats_dict)
			seats_dict_final[row][column] = seat_state

	return seats_dict_final


def count_occupied_seats(seats_dict: dict) -> int:
	occupied_seats: int = 0
	for row in seats_dict:
		for seat in seats_dict[row]:
			if seat == "#":
				occupied_seats += 1
	return occupied_seats


def another_round(seats_dict: dict):
	seats_dict_test_changed = check_all_seats(seats_dict)

	occupied_seats_current = count_occupied_seats(seats_dict_test_changed)

	# for row in seats_dict_test_changed:
	# 	print(seats_dict_test_changed[row])

	return occupied_seats_current, seats_dict_test_changed


if __name__ == '__main__':
	main()
