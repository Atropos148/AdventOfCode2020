def main():
    # 336 too low
    print("Hello numbers!")

    starting_numbers: list = [6, 3, 15, 13, 1, 0]

    last_number, spoken_numbers = prepare_starting_numbers(starting_numbers)

    for _ in range(2020 - len(starting_numbers)):
        last_number, spoken_numbers = say_number(last_number, spoken_numbers)

    print(f"Input: {starting_numbers}, 2020th number: {last_number}")


def say_number(given_number: int, spoken_numbers: dict):
    if given_number in spoken_numbers:
        last_number = spoken_numbers[given_number]
        spoken_numbers[given_number] = 0

    else:
        spoken_numbers[given_number] = 0
        last_number = spoken_numbers[given_number]

    for index in spoken_numbers:
        spoken_numbers[index] += 1

    return last_number, spoken_numbers


def prepare_starting_numbers(numbers_list: list):
    spoken_numbers: dict = {}
    for number in numbers_list:
        spoken_numbers[number] = 0

    numbers_list_reversed: list = list(spoken_numbers.keys())
    numbers_list_reversed.reverse()
    for index, number in enumerate(numbers_list_reversed):
        spoken_numbers[number] = index

    last_number = numbers_list_reversed[0]

    return last_number, spoken_numbers


if __name__ == '__main__':
    main()
