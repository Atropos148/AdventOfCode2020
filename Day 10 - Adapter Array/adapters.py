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

	# will be used later
	device_joltage = calculate_device_joltage(cleaned_test1_part1)

	actual_adapter_list = cleaned_test1_part1
	adapter_difference_results: dict = {
		1: 0,
		2: 0,
		3: 0,
	}

	print(find_adapter_order(actual_adapter_list, adapter_difference_results))


def calculate_device_joltage(list_of_adapters: list) -> int:
	max_joltage_adapter = 0
	for adapter in list_of_adapters:
		if int(adapter) > max_joltage_adapter:
			max_joltage_adapter = int(adapter)
	return max_joltage_adapter + 3


def find_compatible_adapter(list_of_adapters: list, adapter_joltage: int):
	compatible_adapter: int = 0
	for adapter in list_of_adapters:
		if int(adapter_joltage) + 3 >= int(adapter) >= int(adapter_joltage):
			if int(adapter) - adapter_joltage != 2:
				compatible_adapter = int(adapter)
				list_of_adapters.remove(adapter)
				adapter_difference = compatible_adapter - adapter_joltage
				return compatible_adapter, list_of_adapters, adapter_difference


def find_adapter_order(list_of_adapters: list, adapter_difference_results: dict):
	actual_adapter_list = list_of_adapters
	source_joltage = 0
	current_adapter = source_joltage
	for _ in range(len(list_of_adapters)):
		try:
			current_adapter, actual_adapter_list, adapter_difference = find_compatible_adapter(actual_adapter_list,
			                                                                                   current_adapter)
			adapter_difference_results[adapter_difference] += 1
		except TypeError:
			print("One or more adapters are unused: ", actual_adapter_list)

	# including the device itself
	adapter_difference_results[3] += 1
	return f"All adapters used, jolt differences are: {adapter_difference_results}"


if __name__ == '__main__':
	main()
