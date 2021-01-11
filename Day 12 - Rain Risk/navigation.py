def main():
	# Solution for Day 12 of Advent od Code 2020
	# Link: https://adventofcode.com/2020/day/12
	print("Navigation - suggested route")

	input_test = '''F10
N3
F7
R90
F11'''

	clean_test = input_test.split("\n")
	print(f"Instructions: {clean_test}")

	distance_from_start = [0, 0]
	facing_direction = "E"

	for instruction in clean_test:
		distance_from_start, facing_direction = move(instruction, distance_from_start, facing_direction)

	north_south = "north" if distance_from_start[0] < 0 else "south"
	east_west = "west" if distance_from_start[1] < 0 else "east"

	final_message = f"Distance from start is {abs(distance_from_start[0])} miles {north_south} and {abs(distance_from_start[1])} miles {east_west}, " \
	                f"Manhattan distance is {abs(distance_from_start[0]) + abs(distance_from_start[1])} miles"
	print(final_message)


def move(instruction: str, distance_from_start: list, facing_direction: str) -> list:
	instruction_direction: str = instruction[:1]
	instruction_distance: str = int(instruction[1:])

	movement_north: int = 0
	movement_south: int = 0
	movement_east: int = 0
	movement_west: int = 0

	if instruction_direction == "R":
		facing_direction = rotate(facing_direction, instruction_distance)

	else:
		if instruction_direction == "F":
			instruction_direction = facing_direction

		if instruction_direction == "N":
			movement_north += instruction_distance
			distance_from_start[0] -= movement_north
		elif instruction_direction == "S":
			movement_south += instruction_distance
			distance_from_start[0] += movement_south

		if instruction_direction == "E":
			movement_east += instruction_distance
			distance_from_start[1] += movement_east
		elif instruction_direction == "W":
			movement_west += instruction_distance
			distance_from_start[1] -= movement_west

	return distance_from_start, facing_direction


def rotate(starting_direction: str, rotation_degrees: int) -> str:
	directions: list = ['N', 'E', 'S', 'W']
	turns_needed: int = int(rotation_degrees / 90)

	new_direction = starting_direction
	new_direction_index = directions.index(starting_direction) + turns_needed

	if new_direction_index < len(directions):
		new_direction = directions[new_direction_index]
	else:
		new_direction_index = len(directions) - new_direction_index
		new_direction = directions[new_direction_index]

	return new_direction


if __name__ == '__main__':
	main()
