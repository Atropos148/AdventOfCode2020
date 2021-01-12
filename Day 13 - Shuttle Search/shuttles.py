def main():
	input_test = '''939
7,13,x,x,59,x,31,19'''

	clean_input_test = input_test.split("\n")
	current_time = int(clean_input_test[0])
	available_buses = []
	for character in clean_input_test[1].split(","):
		if character != "x":
			available_buses.append(int(character))

	for number in available_buses:
		result = round(current_time / number) * number
		if result >= current_time:
			print(f"Bus_id: {number}, "
			      f"Bus arival time: {result}, "
			      f"Waiting time: {result - current_time}, "
			      f"Answer: {(result - current_time) * number}")


if __name__ == '__main__':
	main()
