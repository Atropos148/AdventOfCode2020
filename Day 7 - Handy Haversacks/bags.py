def main():
	part_1_test_input = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''

	test_bag_rules: dict = create_rules_dict(part_1_test_input)

	print(test_bag_rules)


def create_rules_dict(raw_rules_input: str) -> dict:
	bag_rules: dict = {}
	for rule_row in raw_rules_input.split(".\n"):
		is_color: bool = True
		rules_for_color: str = ""
		for rule_part in rule_row.split(" bags contain "):
			try:
				if is_color:
					rules_for_color = rule_part
					bag_rules[rules_for_color] = {}
				else:
					for bag_rule in rule_part.split(", "):
						cleaned_bag_rule = bag_rule.split()[:-1]
						if cleaned_bag_rule[0] != "no":
							bag_amount = cleaned_bag_rule[0]
							bag_color = cleaned_bag_rule[1] + " " + cleaned_bag_rule[2]
							bag_rules[rules_for_color][bag_color] = bag_amount
				is_color = not is_color
			except ValueError:
				pass

	return bag_rules


if __name__ == '__main__':
	main()
