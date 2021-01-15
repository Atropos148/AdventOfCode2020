def main():
    # Solution for Day 16 of Advent od Code 2020
    # Link: https://adventofcode.com/2020/day/16
    print("Hello Tickets!")
    raw_input_test = '''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12'''

    compute_error_rate(raw_input_test)


def prepare_fields_dictionary(fields_raw: list) -> dict:
    fields_dict: dict = {}
    for field in fields_raw:
        field_name = field.split(": ")[0]
        fields_dict[field_name] = []
        field_values_raw = field.split(": ")[1].split(" or ")
        for value in field_values_raw:
            separated_values = value.split("-")
            fields_dict[field_name].append([separated_values[0], separated_values[1]])

    return fields_dict


def get_values_from_tickets(tickets_list: str):
    other_tickets_raw: list = tickets_list.split("\n")[1:]
    ticket_values_list: list = []
    for ticket in other_tickets_raw:
        current_ticket_values: list = []
        for value in ticket.split(","):
            current_ticket_values.append(int(value))
        ticket_values_list.append(current_ticket_values)
    return ticket_values_list


def find_invalid_values(ticket_values_list: list, fields_dict: dict) -> list:
    invalid_values: list = []
    for ticket in ticket_values_list:
        for value in ticket:
            value = int(value)
            value_invalid_positions: int = 0

            for field in fields_dict:
                invalid_ranges: int = 0
                for number_range in fields_dict[field]:
                    min: int = int(number_range[0])
                    max: int = int(number_range[1])

                    if (min <= value <= max) == False:
                        invalid_ranges += 1

                if invalid_ranges == len(fields_dict[field]):
                    value_invalid_positions += 1

            if value_invalid_positions == len(fields_dict):
                invalid_values.append(value)
    return invalid_values


def compute_error_rate(raw_input: str):
    clean_input_test: list = raw_input.split("\n\n")

    # fields
    fields_raw: list = clean_input_test[0].split("\n")
    fields_dict: dict = prepare_fields_dictionary(fields_raw)

    # my ticket
    # we can ignore this for Part 1
    my_ticket_raw: str = clean_input_test[1]

    # other tickets
    ticket_values_list = get_values_from_tickets(clean_input_test[2])

    # invalid values count
    # test data
    invalid_values = find_invalid_values(ticket_values_list, fields_dict)
    total: int = 0
    for number in invalid_values:
        total += number
    print(f"Invalid values: {invalid_values}, Total: {total}")


if __name__ == '__main__':
    main()
