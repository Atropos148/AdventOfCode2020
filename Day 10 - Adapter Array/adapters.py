def main():
	# Solution for Day 10 of Advent od Code 2020
	# Link: https://adventofcode.com/2020/day/10

	input_test1_part1: str = '''16
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
	input_test2_part1: str = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''
	input_real_part1: str = '''99
104
120
108
67
136
80
44
129
113
158
157
89
60
138
63
35
57
61
153
116
54
7
22
133
130
5
72
2
28
131
123
55
145
151
42
98
34
140
146
100
79
117
154
9
83
132
45
43
107
91
163
86
115
39
76
36
82
162
6
27
101
150
30
110
139
109
1
64
56
161
92
62
69
144
21
147
12
114
18
137
75
164
33
152
23
68
51
8
95
90
48
29
26
165
81
13
126
14
143
15'''

	cleaned_test1_part1 = input_test1_part1.split("\n")
	cleaned_test2_part1 = input_test2_part1.split("\n")
	cleaned_real_part_1 = input_real_part1.split("\n")

	# will be used later
	device_joltage = calculate_device_joltage(cleaned_test1_part1)

	actual_adapter_list_test1 = cleaned_test1_part1
	actual_adapter_list_test2 = cleaned_test2_part1
	actual_adapter_list_real = cleaned_real_part_1

	print(find_adapter_order(actual_adapter_list_test1))
	print(find_adapter_order(actual_adapter_list_test2))
	print(find_adapter_order(actual_adapter_list_real))


def calculate_device_joltage(list_of_adapters: list) -> int:
	max_joltage_adapter = 0
	for adapter in list_of_adapters:
		if int(adapter) > max_joltage_adapter:
			max_joltage_adapter = int(adapter)
	return int(max_joltage_adapter) + 3


def find_compatible_adapter(list_of_adapters: list, adapter_joltage: int):
	possible_adapters: list = []
	for adapter in list_of_adapters:
		if int(adapter_joltage) + 3 >= int(adapter) >= int(adapter_joltage):
			if int(adapter) - adapter_joltage != 2:
				compatible_adapter = int(adapter)
				possible_adapters.append(compatible_adapter)

	possible_adapters.sort()
	compatible_adapter = possible_adapters[0]
	list_of_adapters.remove(str(compatible_adapter))
	adapter_difference = compatible_adapter - adapter_joltage

	return compatible_adapter, list_of_adapters, adapter_difference


def find_adapter_order(list_of_adapters: list):
	adapter_difference_results: dict = {
		1: 0,
		2: 0,
		3: 0,
	}

	actual_adapter_list = list_of_adapters
	source_joltage = 0
	current_adapter = source_joltage
	for _ in range(len(actual_adapter_list)):
		try:
			current_adapter, actual_adapter_list, adapter_difference = find_compatible_adapter(actual_adapter_list,
			                                                                                   current_adapter)
			adapter_difference_results[adapter_difference] += 1

		except TypeError:
			print("One or more adapters are unused: ", actual_adapter_list)
			break

		except KeyError:
			print("Unexpected joltage difference for: ", current_adapter)
			break

	# including the device itself
	adapter_difference_results[3] += 1
	return f"All adapters used, jolt differences are: {adapter_difference_results}, " \
	       f"multiplied differences of 1 and 3: {adapter_difference_results[1] * adapter_difference_results[3]}"


if __name__ == '__main__':
	main()
