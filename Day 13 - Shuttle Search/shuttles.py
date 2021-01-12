def main():
	for number in [7, 13, 59, 31, 19]:
		result = round(939 / number) * number
		if result >= 939:
			print(number, result, result - 939)


if __name__ == '__main__':
	main()
