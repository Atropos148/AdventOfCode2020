def main():
	# Solution for Day 10 of Advent od Code 2020
	# Link: https://adventofcode.com/2020/day/10

	input_test1_part1 = '''16
10
15
5
1
11
7
19
6
12
4'''
	cleaned_test1_part1 = input_test1_part1.split("\n")

	device_joltage = calculate_device_joltage(cleaned_test1_part1)

	print(device_joltage)


def calculate_device_joltage(list_of_adapters: list) -> int:
	max_joltage_adapter = 0
	for adapter in list_of_adapters:
		if int(adapter) > max_joltage_adapter:
			max_joltage_adapter = int(adapter)
	return max_joltage_adapter + 3


if __name__ == '__main__':
	main()
