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

	seats_list_test = create_seats_dict(cleaned_seats_test)
	print(seats_list_test)


def create_seats_dict(seats_list: list) -> dict:
	seats_dict: dict = {}
	for index in range(len(seats_list)):
		seats_dict[index] = seats_list[index]

	return seats_dict


if __name__ == '__main__':
	main()
