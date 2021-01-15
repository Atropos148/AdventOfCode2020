def main():
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
38,6,12
'''

    clean_input_test = raw_input_test.split("\n\n")
    fields_raw = clean_input_test[0].split("\n")
    fields_dict: dict = prepare_fields_dictionary(fields_raw)

    print(fields_dict, len(fields_dict))


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


if __name__ == '__main__':
    main()
