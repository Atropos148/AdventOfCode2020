def main():
    print('Hello math operations!')
    input_test: str = '''1 + 2 * 3 + 4 * 5 + 6'''

    math_problems: list = input_test.split("\n")
    for math_problem in math_problems:
        while len(math_problem) > 1:
            math_problem = compute_result_for_leftmost_operation(math_problem)
            print(math_problem)


def compute_result_for_leftmost_operation(math_problem):
    from collections import deque
    from itertools import islice

    if (type(math_problem) != deque):
        math_problem: deque = deque(math_problem.split(" "))

    first_number = 0
    second_number = 0
    operation: str = ""
    for index, character in enumerate(math_problem):
        try:
            if not first_number:
                first_number = int(character)
            else:
                second_number = int(character)
        except ValueError:
            operation = character

        if first_number != 0 and second_number != 0 and operation != "":
            result: int = 0
            print(f"{first_number} {operation} {second_number}")
            if operation == "+":
                result = first_number + second_number
            elif operation == "*":
                result = first_number * second_number

            solution: deque = deque(islice(math_problem, index + 1, len(math_problem)))
            solution.appendleft(result)

            return solution


if __name__ == '__main__':
    main()
