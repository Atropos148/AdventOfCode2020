def main():
	input_test = '''939
7,13,x,x,59,x,31,19'''
	input_real = '''1015292
19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,743,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,643,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23'''

	clean_input_test = input_test.split("\n")
	clean_input_real = input_real.split("\n")

	available_buses_list, current_time = process_input(clean_input_test)
	find_bus(available_buses_list, current_time)

	available_buses_list, current_time = process_input(clean_input_real)
	find_bus(available_buses_list, current_time)


def find_bus(available_buses: list, current_time: int):
	for number in available_buses:
		result = round(current_time / number) * number
		if result >= current_time:
			print(f"Bus_id: {number}, "
			      f"Bus arival time: {result}, "
			      f"Waiting time: {result - current_time}, "
			      f"Answer: {(result - current_time) * number}")


def process_input(cleaned_input: list):
	current_time = int(cleaned_input[0])
	available_buses_list = []
	for character in cleaned_input[1].split(","):
		if character != "x":
			available_buses_list.append(int(character))

	return available_buses_list, current_time


if __name__ == '__main__':
	main()
