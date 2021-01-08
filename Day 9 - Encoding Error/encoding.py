def main():
	input_test_part1 = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''

	cleaned_test_part1 = input_test_part1.split("\n")

	test_control_group_size: int = 5
	control_group_start_index: int = 0
	control_group: list = []

	try:
		for _ in cleaned_test_part1:
			if control_group_start_index + test_control_group_size < len(cleaned_test_part1):
				tested_number = cleaned_test_part1[control_group_start_index + test_control_group_size]

			control_group, control_group_start_index = get_control_group(cleaned_test_part1, control_group_start_index,
			                                                             test_control_group_size)
			# print(control_group, tested_number)
			if not is_number_valid(tested_number, control_group):
				print(tested_number)
	except TypeError:
		pass


def get_control_group(input_data: str, current_start_index: int, group_size: int):
	control_group = input_data[current_start_index:current_start_index + group_size]
	if len(control_group) == 5:
		current_start_index += 1
		return (control_group, current_start_index)


def is_number_valid(test_number: int, control_group: list) -> bool:
	for index, number in enumerate(control_group):
		first_number = control_group[index]
		other_numbers = control_group[index + 1:]
		if len(other_numbers) > 0:
			for sum_number in other_numbers:
				if int(first_number) + int(sum_number) == int(test_number):
					return True

	return False


if __name__ == '__main__':
	main()
