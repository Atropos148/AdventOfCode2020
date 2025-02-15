def main():
	"""
	Finds how many outer bags you can use

	Made for AoC 2020 Day 7: https://adventofcode.com/2020/day/7
	"""

	part_1_test_input = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''
	part_1_real_input = '''striped white bags contain 4 drab silver bags.
drab silver bags contain no other bags.
pale plum bags contain 1 dark black bag.
muted gold bags contain 1 wavy red bag, 3 mirrored violet bags, 5 bright gold bags, 5 plaid white bags.
muted teal bags contain 2 pale beige bags, 5 clear beige bags, 2 dotted gold bags, 4 posh cyan bags.
posh coral bags contain 1 light silver bag, 2 dull blue bags, 3 dim fuchsia bags, 2 dotted magenta bags.
faded black bags contain 4 light silver bags.
muted lavender bags contain 1 pale gold bag.
clear fuchsia bags contain 1 dull gray bag, 2 shiny indigo bags, 3 posh olive bags, 5 vibrant plum bags.
shiny olive bags contain 1 dotted gold bag, 5 bright violet bags.
vibrant lavender bags contain 3 dotted aqua bags, 4 pale chartreuse bags, 5 mirrored blue bags.
pale fuchsia bags contain 5 pale crimson bags, 2 dull teal bags.
clear lavender bags contain 5 shiny fuchsia bags, 5 wavy teal bags.
light chartreuse bags contain 5 mirrored yellow bags, 3 bright maroon bags.
mirrored white bags contain 1 bright gray bag, 4 plaid blue bags.
dark teal bags contain 4 bright maroon bags, 5 plaid bronze bags, 1 dark brown bag.
wavy yellow bags contain 4 dim silver bags, 1 striped tomato bag, 5 clear chartreuse bags.
dark turquoise bags contain 4 clear plum bags.
posh gray bags contain 2 faded purple bags, 2 faded orange bags.
wavy tomato bags contain 1 dark purple bag.
vibrant gray bags contain 3 muted gray bags, 1 dark fuchsia bag, 5 posh white bags, 5 posh tomato bags.
light crimson bags contain 2 dotted chartreuse bags.
dull gray bags contain 4 muted brown bags, 2 shiny blue bags, 4 dim crimson bags.
drab red bags contain 2 bright cyan bags, 1 pale brown bag.
dotted salmon bags contain 5 mirrored indigo bags.
vibrant green bags contain 2 dark coral bags.
light magenta bags contain 4 clear bronze bags, 4 dull teal bags, 4 posh salmon bags.
vibrant purple bags contain 4 posh plum bags, 2 bright gray bags.
posh lime bags contain 3 plaid yellow bags, 4 posh salmon bags.
bright white bags contain 4 dull aqua bags, 1 shiny silver bag.
faded blue bags contain 5 muted cyan bags, 2 mirrored coral bags.
dim green bags contain 2 posh lavender bags.
faded gray bags contain 2 dark gold bags, 1 drab turquoise bag.
wavy black bags contain 4 dim fuchsia bags, 1 muted orange bag, 4 drab salmon bags.
plaid plum bags contain 5 dotted tomato bags, 1 shiny beige bag.
bright tan bags contain 2 posh salmon bags.
wavy gold bags contain 1 faded olive bag, 5 vibrant black bags, 3 dull orange bags.
dull fuchsia bags contain 1 faded crimson bag, 5 vibrant white bags.
shiny maroon bags contain 5 dull lavender bags, 1 dim white bag.
wavy white bags contain 5 light teal bags, 4 dim salmon bags, 3 dotted red bags, 5 dark red bags.
dim cyan bags contain 1 muted orange bag.
muted cyan bags contain 4 dull turquoise bags, 5 posh gray bags, 5 clear turquoise bags, 1 shiny plum bag.
posh violet bags contain 5 plaid crimson bags, 5 muted purple bags, 1 wavy beige bag, 2 mirrored orange bags.
faded purple bags contain 3 plaid blue bags, 1 dull lavender bag, 1 muted orange bag, 2 dotted tomato bags.
wavy beige bags contain 1 dotted beige bag.
dim black bags contain 1 wavy blue bag, 1 plaid black bag, 3 pale lavender bags, 2 light violet bags.
dotted lavender bags contain 1 plaid blue bag, 5 dim crimson bags.
dark yellow bags contain 3 posh green bags.
wavy salmon bags contain 1 clear aqua bag, 3 mirrored crimson bags, 3 pale magenta bags, 2 dull teal bags.
clear silver bags contain 3 faded tan bags, 5 faded aqua bags, 1 clear tomato bag.
vibrant bronze bags contain 1 faded maroon bag, 4 plaid indigo bags, 2 bright purple bags, 5 dim violet bags.
pale brown bags contain 1 dull lavender bag, 2 clear turquoise bags.
faded salmon bags contain 1 pale silver bag.
dark gray bags contain 2 pale teal bags.
posh red bags contain 3 faded black bags, 2 dull red bags.
dim indigo bags contain 3 bright green bags, 2 dotted tomato bags, 5 bright magenta bags.
dull maroon bags contain 5 light green bags.
wavy teal bags contain 5 faded tan bags, 4 clear orange bags.
pale chartreuse bags contain 5 bright blue bags, 3 light indigo bags, 3 shiny white bags, 3 wavy bronze bags.
mirrored gray bags contain 4 vibrant tomato bags, 1 dark red bag, 5 drab silver bags, 3 posh magenta bags.
dark lavender bags contain 4 dotted white bags, 5 vibrant chartreuse bags, 2 dim teal bags.
shiny turquoise bags contain 3 dim lime bags, 5 bright cyan bags, 2 pale green bags.
shiny indigo bags contain 2 dark fuchsia bags, 4 posh chartreuse bags.
pale crimson bags contain 5 mirrored silver bags, 2 posh black bags.
light salmon bags contain 2 vibrant orange bags, 2 dotted red bags.
plaid orange bags contain 1 dotted turquoise bag, 4 vibrant brown bags.
dim maroon bags contain 5 shiny gold bags, 4 mirrored maroon bags.
muted green bags contain 1 plaid plum bag.
faded indigo bags contain 3 faded purple bags, 4 vibrant indigo bags, 1 light coral bag.
dull blue bags contain 5 dull salmon bags, 2 wavy magenta bags.
vibrant black bags contain 1 light coral bag, 5 vibrant cyan bags, 3 dim magenta bags.
striped lime bags contain 1 striped maroon bag, 2 vibrant brown bags.
drab brown bags contain 1 faded olive bag, 5 dotted beige bags.
dark plum bags contain 5 faded brown bags.
clear olive bags contain 3 dull aqua bags, 5 drab yellow bags.
wavy crimson bags contain 2 posh plum bags, 2 dull aqua bags, 5 shiny teal bags, 2 vibrant purple bags.
mirrored olive bags contain 2 wavy gold bags.
dim crimson bags contain no other bags.
faded plum bags contain 1 plaid indigo bag.
light maroon bags contain 3 vibrant orange bags, 2 clear olive bags, 3 clear brown bags, 1 pale black bag.
posh white bags contain 3 dull green bags, 3 clear brown bags.
drab black bags contain 2 shiny turquoise bags.
light purple bags contain 2 pale black bags, 5 light silver bags, 1 drab coral bag.
pale yellow bags contain 2 vibrant orange bags, 5 posh black bags, 2 vibrant tomato bags, 3 dotted lavender bags.
dull cyan bags contain 5 wavy beige bags, 1 dull yellow bag, 3 drab lime bags, 3 drab chartreuse bags.
drab lavender bags contain 2 plaid black bags, 4 dotted gray bags, 1 dim silver bag, 2 shiny gold bags.
striped brown bags contain 5 light maroon bags, 3 light red bags, 3 clear indigo bags.
drab tomato bags contain 2 light black bags, 2 clear salmon bags.
dotted red bags contain 4 dim salmon bags, 5 striped indigo bags.
vibrant teal bags contain 5 bright black bags, 1 dark purple bag, 2 bright turquoise bags.
striped teal bags contain 4 mirrored silver bags.
dull beige bags contain 4 clear olive bags, 4 light teal bags, 3 bright plum bags, 4 dotted lavender bags.
light violet bags contain 2 dull lavender bags, 4 bright gray bags, 5 vibrant orange bags, 3 wavy magenta bags.
dim brown bags contain 2 clear plum bags, 2 shiny teal bags, 2 posh salmon bags.
striped magenta bags contain 4 posh turquoise bags, 3 pale cyan bags, 3 faded indigo bags.
bright orange bags contain 4 plaid gray bags, 4 dark black bags, 4 faded red bags, 4 bright black bags.
muted olive bags contain 2 dotted crimson bags, 4 faded lavender bags, 2 vibrant gray bags.
plaid teal bags contain 2 light yellow bags, 4 drab cyan bags, 3 light green bags.
faded fuchsia bags contain 1 posh silver bag, 4 drab chartreuse bags, 4 drab teal bags.
dim silver bags contain 1 pale turquoise bag.
bright lime bags contain 1 striped silver bag, 5 muted teal bags, 1 shiny tan bag, 1 dark silver bag.
dotted green bags contain 3 posh green bags, 1 drab yellow bag.
drab purple bags contain 5 bright violet bags, 1 posh tomato bag.
dull bronze bags contain 4 mirrored black bags.
striped tomato bags contain 1 posh gray bag, 2 posh magenta bags.
bright crimson bags contain 2 light olive bags, 4 clear tan bags, 3 drab fuchsia bags.
bright turquoise bags contain 4 pale teal bags, 3 drab silver bags.
shiny lavender bags contain 2 striped lime bags, 2 plaid tomato bags, 1 faded orange bag, 5 wavy magenta bags.
light tomato bags contain 5 dotted olive bags.
wavy magenta bags contain no other bags.
vibrant fuchsia bags contain 5 posh brown bags, 5 plaid indigo bags.
dark tomato bags contain 3 shiny plum bags.
pale bronze bags contain 5 plaid black bags, 5 vibrant brown bags, 2 dim lime bags, 4 muted bronze bags.
striped fuchsia bags contain 3 muted brown bags, 2 pale chartreuse bags, 1 dim magenta bag.
dark brown bags contain 4 clear bronze bags.
posh teal bags contain 5 dotted plum bags, 2 drab gray bags, 3 dull fuchsia bags.
wavy turquoise bags contain 1 dull lavender bag.
striped maroon bags contain 4 muted yellow bags, 4 clear orange bags, 4 vibrant orange bags.
shiny green bags contain 3 muted brown bags, 1 vibrant black bag, 4 wavy cyan bags, 3 posh brown bags.
plaid salmon bags contain 4 mirrored indigo bags, 2 wavy white bags, 5 mirrored bronze bags, 3 light coral bags.
dotted magenta bags contain 2 light olive bags, 2 dark red bags, 4 clear green bags, 3 dim plum bags.
light orange bags contain 5 dark plum bags, 3 bright maroon bags, 2 dotted lime bags.
clear brown bags contain 3 dim white bags, 2 posh magenta bags.
vibrant turquoise bags contain 2 striped yellow bags, 1 mirrored crimson bag.
muted coral bags contain 4 wavy gold bags, 2 dim tan bags, 1 shiny green bag.
plaid crimson bags contain 1 dull aqua bag.
vibrant plum bags contain 4 striped tomato bags, 1 striped turquoise bag.
dark coral bags contain 5 posh black bags, 1 shiny beige bag, 3 pale brown bags.
mirrored brown bags contain 1 clear blue bag, 1 dull indigo bag.
bright blue bags contain 2 light violet bags, 1 dotted tomato bag.
drab cyan bags contain 2 dim turquoise bags, 5 clear violet bags.
dotted coral bags contain 3 dotted aqua bags.
shiny yellow bags contain 1 wavy cyan bag.
shiny red bags contain 5 shiny beige bags, 3 dotted lime bags, 5 dotted plum bags.
muted lime bags contain 3 dark turquoise bags, 3 bright chartreuse bags.
pale gray bags contain 5 dotted coral bags, 4 wavy teal bags, 2 clear aqua bags.
pale blue bags contain 5 dull salmon bags, 3 posh bronze bags, 2 vibrant tomato bags.
dim turquoise bags contain 4 posh aqua bags, 2 dark turquoise bags.
pale turquoise bags contain 5 vibrant brown bags, 2 shiny maroon bags.
dim gray bags contain 2 faded tomato bags, 2 faded indigo bags.
clear aqua bags contain 1 light turquoise bag, 3 dotted turquoise bags.
faded turquoise bags contain 5 muted lime bags.
clear plum bags contain 2 plaid indigo bags, 5 drab yellow bags.
vibrant white bags contain 2 bright violet bags, 4 dark plum bags, 1 dim plum bag, 4 plaid indigo bags.
dark orange bags contain 3 posh purple bags, 5 clear orange bags, 1 dim white bag.
light olive bags contain 3 drab green bags.
muted salmon bags contain 4 muted cyan bags.
clear maroon bags contain 2 muted yellow bags, 5 plaid crimson bags, 1 clear turquoise bag.
wavy orange bags contain 4 vibrant blue bags, 4 posh brown bags, 2 pale turquoise bags, 5 shiny orange bags.
dotted gold bags contain 3 posh magenta bags, 1 faded crimson bag, 3 dotted olive bags, 3 plaid olive bags.
dull purple bags contain 5 drab salmon bags, 4 dim lavender bags.
light bronze bags contain 2 wavy indigo bags.
muted turquoise bags contain 5 clear turquoise bags, 4 plaid violet bags, 4 clear orange bags, 2 posh maroon bags.
mirrored blue bags contain 4 clear chartreuse bags.
drab tan bags contain 3 striped violet bags, 2 bright silver bags, 2 dark bronze bags, 1 mirrored black bag.
dark maroon bags contain 1 vibrant orange bag.
drab yellow bags contain 1 vibrant blue bag, 2 dim violet bags.
light cyan bags contain 4 posh beige bags.
vibrant salmon bags contain 3 wavy gold bags.
muted orange bags contain 3 dotted tomato bags, 4 vibrant tomato bags, 5 dull lavender bags.
dull turquoise bags contain 1 wavy white bag.
dotted indigo bags contain 3 wavy bronze bags.
dark red bags contain 4 wavy bronze bags, 5 wavy turquoise bags.
light coral bags contain 4 clear tan bags, 2 vibrant beige bags, 1 dull lavender bag, 5 shiny white bags.
mirrored turquoise bags contain 5 clear fuchsia bags, 3 mirrored black bags, 4 plaid tan bags.
mirrored yellow bags contain 4 pale turquoise bags, 2 wavy orange bags, 3 drab coral bags, 4 dim chartreuse bags.
dotted fuchsia bags contain 4 dim bronze bags, 4 striped indigo bags.
dotted purple bags contain 5 posh maroon bags, 1 dim yellow bag.
clear coral bags contain 5 dark olive bags, 2 wavy bronze bags, 3 light red bags.
mirrored teal bags contain 3 drab yellow bags.
faded green bags contain 2 dark purple bags.
light lime bags contain 4 bright chartreuse bags, 5 clear tomato bags, 2 bright green bags, 2 faded teal bags.
bright yellow bags contain 4 dull purple bags, 3 faded beige bags.
bright maroon bags contain 2 vibrant blue bags, 5 bright violet bags, 5 plaid indigo bags, 3 vibrant orange bags.
faded red bags contain 5 pale brown bags, 4 striped tomato bags, 2 bright green bags.
muted maroon bags contain 1 dark tan bag, 5 drab teal bags, 4 dull maroon bags.
plaid coral bags contain 5 bright blue bags, 1 dotted indigo bag.
dotted brown bags contain 1 dull beige bag, 2 bright indigo bags, 2 striped chartreuse bags, 1 muted silver bag.
wavy coral bags contain 2 clear cyan bags, 2 muted teal bags, 1 faded red bag, 2 mirrored silver bags.
faded coral bags contain 3 bright green bags, 1 bright cyan bag, 3 plaid blue bags, 5 wavy lavender bags.
dim gold bags contain 5 dim teal bags, 1 vibrant tomato bag, 5 pale chartreuse bags, 3 bright indigo bags.
bright salmon bags contain 5 plaid chartreuse bags, 5 light tan bags, 5 vibrant maroon bags.
wavy violet bags contain 4 bright green bags.
mirrored lavender bags contain 5 drab plum bags, 2 drab turquoise bags, 2 dark magenta bags.
faded aqua bags contain 3 faded teal bags, 1 dark red bag.
muted yellow bags contain 1 mirrored silver bag, 1 striped white bag, 3 mirrored gold bags, 1 muted gray bag.
pale coral bags contain 2 striped gray bags, 2 clear beige bags.
mirrored cyan bags contain 1 pale beige bag, 4 dim crimson bags.
dotted aqua bags contain 4 dim crimson bags, 3 vibrant beige bags.
dark white bags contain 4 dim maroon bags, 1 light olive bag, 3 dull fuchsia bags, 4 mirrored maroon bags.
dotted chartreuse bags contain 5 clear tan bags, 2 clear white bags, 2 dark coral bags, 4 faded brown bags.
mirrored red bags contain 5 faded violet bags, 2 dark chartreuse bags.
drab maroon bags contain 3 bright violet bags.
dark violet bags contain 5 dark turquoise bags, 1 muted blue bag, 4 plaid bronze bags.
dull silver bags contain 4 dotted lime bags, 3 dotted silver bags, 4 dull red bags, 3 pale white bags.
striped lavender bags contain 5 drab silver bags.
light yellow bags contain 3 posh plum bags, 3 bright olive bags, 4 wavy crimson bags.
posh chartreuse bags contain 2 bright violet bags.
pale green bags contain 5 shiny lime bags, 3 faded teal bags, 5 posh gray bags, 1 posh chartreuse bag.
shiny lime bags contain 1 dull beige bag, 4 light aqua bags, 4 dotted tomato bags.
plaid tan bags contain 1 mirrored chartreuse bag.
drab coral bags contain 5 posh gray bags, 2 dull black bags.
drab salmon bags contain 4 drab yellow bags, 3 mirrored green bags.
faded yellow bags contain 2 mirrored beige bags, 1 bright turquoise bag, 1 vibrant black bag.
bright tomato bags contain 4 clear brown bags.
muted beige bags contain 1 clear turquoise bag.
striped black bags contain 1 plaid chartreuse bag.
bright cyan bags contain 5 clear tomato bags.
striped coral bags contain 2 muted red bags.
posh bronze bags contain 5 striped yellow bags.
mirrored maroon bags contain 4 vibrant tomato bags, 5 bright green bags, 4 vibrant maroon bags, 4 striped violet bags.
dotted turquoise bags contain 1 posh beige bag, 5 muted silver bags.
bright purple bags contain 5 drab silver bags, 5 shiny blue bags, 2 plaid bronze bags, 4 faded magenta bags.
posh plum bags contain 5 striped white bags, 2 pale brown bags, 1 wavy turquoise bag.
dark crimson bags contain 1 dull black bag, 2 dull yellow bags, 1 posh white bag, 3 dotted lime bags.
plaid bronze bags contain 5 striped indigo bags, 5 light indigo bags, 4 wavy magenta bags, 3 vibrant blue bags.
clear red bags contain 4 posh silver bags, 1 dim aqua bag.
striped salmon bags contain 3 bright violet bags, 4 faded olive bags, 5 dim turquoise bags.
dim bronze bags contain no other bags.
wavy brown bags contain 4 vibrant turquoise bags.
wavy maroon bags contain 1 mirrored bronze bag, 2 posh fuchsia bags, 1 mirrored indigo bag.
mirrored salmon bags contain 2 faded lavender bags.
dark aqua bags contain 4 faded teal bags, 1 dim tomato bag.
pale violet bags contain 5 clear blue bags, 3 plaid blue bags, 5 dim teal bags, 2 pale black bags.
mirrored crimson bags contain 2 posh magenta bags, 2 dotted aqua bags, 1 dim bronze bag.
bright indigo bags contain 4 bright violet bags.
muted violet bags contain 4 mirrored maroon bags, 2 dull red bags, 4 plaid tomato bags, 1 pale yellow bag.
shiny gold bags contain 3 vibrant blue bags, 5 plaid blue bags, 2 dark red bags, 1 dull green bag.
clear green bags contain 4 dotted lavender bags.
dark indigo bags contain 2 light lime bags, 3 wavy brown bags.
muted fuchsia bags contain 3 plaid green bags.
bright silver bags contain 4 dim tomato bags, 3 clear olive bags, 1 dull teal bag.
plaid purple bags contain 4 dark silver bags, 1 vibrant crimson bag, 4 dark black bags, 3 faded magenta bags.
clear chartreuse bags contain 4 posh plum bags.
plaid tomato bags contain 2 wavy aqua bags, 3 striped indigo bags, 1 wavy magenta bag.
posh cyan bags contain 3 drab green bags, 3 bright chartreuse bags, 3 muted gray bags, 2 light black bags.
posh turquoise bags contain 5 wavy teal bags, 3 light tan bags, 1 dull gold bag.
plaid olive bags contain 2 dim chartreuse bags.
shiny orange bags contain 4 pale brown bags, 3 dim salmon bags.
clear gray bags contain 4 bright salmon bags, 5 vibrant crimson bags.
shiny brown bags contain 1 bright gold bag, 3 clear tomato bags.
muted aqua bags contain 2 mirrored indigo bags, 1 dim tan bag.
plaid red bags contain 1 clear plum bag.
muted bronze bags contain 4 clear white bags, 3 dotted plum bags.
plaid blue bags contain 2 dull lavender bags, 5 wavy magenta bags, 1 light indigo bag.
shiny salmon bags contain 2 dotted black bags, 1 light magenta bag.
shiny cyan bags contain 5 faded violet bags, 3 mirrored bronze bags, 4 dark maroon bags, 2 wavy lavender bags.
drab magenta bags contain 2 light blue bags, 1 wavy orange bag, 5 posh chartreuse bags.
dim violet bags contain 5 dark red bags, 4 light violet bags, 2 dotted fuchsia bags, 2 plaid tomato bags.
faded crimson bags contain 3 clear silver bags, 1 vibrant beige bag.
plaid fuchsia bags contain 3 plaid red bags, 4 drab purple bags, 4 clear lime bags, 3 dim turquoise bags.
dull green bags contain 5 dotted beige bags, 4 drab silver bags, 4 posh magenta bags, 1 muted orange bag.
wavy indigo bags contain 2 pale tan bags.
plaid lavender bags contain 1 dark black bag.
clear bronze bags contain 3 pale teal bags.
clear blue bags contain 2 light teal bags, 5 dotted olive bags, 3 bright indigo bags.
posh aqua bags contain 2 light violet bags, 2 dull salmon bags, 1 vibrant violet bag.
dark gold bags contain 2 striped maroon bags.
vibrant chartreuse bags contain 3 wavy silver bags.
dark magenta bags contain 1 clear silver bag.
dim red bags contain 3 wavy indigo bags, 2 muted teal bags.
muted silver bags contain 5 pale crimson bags, 2 dotted tomato bags.
mirrored tan bags contain 1 pale salmon bag.
dull violet bags contain 2 dull black bags.
striped beige bags contain 4 dark maroon bags, 2 wavy orange bags.
striped turquoise bags contain 3 light indigo bags, 5 bright maroon bags, 1 light teal bag.
pale gold bags contain 5 dotted teal bags.
wavy olive bags contain 3 dotted fuchsia bags.
clear violet bags contain 1 dotted lavender bag, 5 bright tan bags, 5 dim violet bags, 5 drab salmon bags.
pale maroon bags contain 4 drab red bags, 1 wavy yellow bag, 1 muted green bag, 1 striped fuchsia bag.
drab bronze bags contain 4 light gray bags, 3 posh magenta bags, 1 dull yellow bag.
vibrant gold bags contain 4 dull violet bags, 3 clear white bags, 5 wavy chartreuse bags, 4 pale turquoise bags.
clear beige bags contain 4 plaid blue bags, 3 shiny plum bags, 1 light silver bag.
faded silver bags contain 5 drab turquoise bags, 4 plaid green bags, 4 posh yellow bags, 1 plaid blue bag.
light brown bags contain 1 dark red bag, 1 dotted gray bag.
shiny violet bags contain 5 posh cyan bags, 5 vibrant plum bags, 5 mirrored chartreuse bags, 4 plaid green bags.
dark bronze bags contain 4 bright gold bags, 2 striped maroon bags, 4 dark aqua bags, 5 pale chartreuse bags.
dull black bags contain 2 vibrant tomato bags, 1 vibrant blue bag, 3 pale yellow bags.
dotted beige bags contain 5 dotted tomato bags, 1 striped indigo bag.
clear indigo bags contain 3 dark violet bags.
bright coral bags contain 1 dark indigo bag.
drab turquoise bags contain 5 drab plum bags, 3 pale magenta bags, 5 drab red bags, 4 dull olive bags.
shiny fuchsia bags contain 2 dull lavender bags, 5 striped tomato bags.
dull indigo bags contain 3 pale turquoise bags, 3 faded tomato bags, 5 dim magenta bags, 3 drab indigo bags.
dim aqua bags contain 4 faded brown bags, 1 mirrored lime bag.
muted purple bags contain 3 dim salmon bags, 4 light violet bags, 2 striped turquoise bags, 2 shiny teal bags.
dotted black bags contain 3 dotted cyan bags, 4 wavy magenta bags, 4 posh chartreuse bags.
drab violet bags contain 4 dark gray bags, 5 dull chartreuse bags, 4 plaid gray bags.
plaid green bags contain 3 dark red bags, 1 wavy crimson bag, 4 light coral bags, 4 striped indigo bags.
faded brown bags contain 3 dark orange bags.
light teal bags contain 3 striped indigo bags, 4 dim bronze bags.
plaid black bags contain 2 mirrored crimson bags, 5 dim silver bags, 4 posh purple bags.
shiny blue bags contain 2 plaid green bags, 4 plaid crimson bags, 2 faded plum bags.
plaid lime bags contain 2 striped maroon bags.
pale lavender bags contain 2 mirrored indigo bags, 1 pale green bag, 5 dim chartreuse bags, 3 pale white bags.
drab chartreuse bags contain 1 bright salmon bag, 4 vibrant brown bags, 1 muted violet bag.
light indigo bags contain no other bags.
plaid violet bags contain 2 dim white bags, 4 faded lavender bags.
drab gold bags contain 5 dotted aqua bags, 3 muted beige bags, 4 faded black bags, 5 dark red bags.
mirrored bronze bags contain 2 plaid blue bags, 1 light orange bag.
dim olive bags contain 1 striped silver bag.
plaid white bags contain 5 pale turquoise bags, 4 mirrored orange bags, 2 vibrant aqua bags.
wavy purple bags contain 3 dark silver bags, 1 dull white bag, 3 dotted magenta bags, 2 dim salmon bags.
clear orange bags contain 5 striped indigo bags, 1 wavy bronze bag, 4 vibrant blue bags.
plaid gray bags contain 1 dull aqua bag, 3 dull olive bags, 3 posh black bags.
vibrant violet bags contain 2 vibrant maroon bags.
pale olive bags contain 2 vibrant fuchsia bags.
muted brown bags contain 5 pale teal bags, 2 light brown bags, 4 light tomato bags.
posh lavender bags contain 4 bright indigo bags, 1 striped indigo bag, 5 dark purple bags.
dotted blue bags contain 4 muted salmon bags, 3 mirrored red bags, 5 pale white bags, 3 clear red bags.
dim purple bags contain 4 muted cyan bags.
bright fuchsia bags contain 5 muted black bags.
vibrant lime bags contain 3 posh purple bags, 1 drab aqua bag.
wavy green bags contain 3 drab red bags, 2 faded brown bags, 2 wavy cyan bags.
dull lime bags contain 3 bright salmon bags, 4 posh crimson bags, 1 drab salmon bag, 4 pale yellow bags.
mirrored aqua bags contain 4 striped violet bags, 1 striped indigo bag, 2 striped tomato bags.
striped tan bags contain 4 light blue bags, 4 dull beige bags.
drab green bags contain 5 muted silver bags, 1 vibrant orange bag, 2 striped indigo bags, 4 striped tomato bags.
dotted orange bags contain 5 mirrored white bags, 5 muted orange bags, 2 drab tomato bags, 2 dull white bags.
dim tomato bags contain 2 dull lavender bags.
dull magenta bags contain 3 faded brown bags, 5 faded teal bags.
faded maroon bags contain 4 posh brown bags, 2 dotted aqua bags.
plaid cyan bags contain 4 faded crimson bags, 4 light chartreuse bags, 1 light crimson bag, 1 posh fuchsia bag.
dim salmon bags contain 1 dotted olive bag, 4 light indigo bags.
faded chartreuse bags contain 4 bright gold bags, 4 clear silver bags.
light plum bags contain 2 dotted chartreuse bags, 1 drab white bag.
posh silver bags contain 3 mirrored black bags, 4 dull blue bags.
dull salmon bags contain 4 dim white bags, 5 clear tomato bags, 2 mirrored maroon bags.
light green bags contain 4 plaid chartreuse bags, 5 vibrant aqua bags.
posh indigo bags contain 2 dull olive bags, 2 dotted lime bags, 1 drab red bag.
dark blue bags contain 5 dotted green bags, 3 wavy crimson bags, 4 clear silver bags.
bright black bags contain 5 posh bronze bags, 3 bright cyan bags, 5 muted black bags.
bright lavender bags contain 1 shiny indigo bag, 1 dim yellow bag, 1 wavy yellow bag.
faded white bags contain 1 dotted black bag, 5 wavy red bags.
muted black bags contain 1 mirrored aqua bag, 4 dark red bags, 5 dull yellow bags.
light turquoise bags contain 3 shiny plum bags.
vibrant coral bags contain 2 shiny orange bags, 4 bright olive bags.
vibrant aqua bags contain 2 wavy crimson bags, 2 muted orange bags.
dotted tan bags contain 1 light indigo bag, 2 dim magenta bags.
posh yellow bags contain 4 faded lavender bags.
pale lime bags contain 4 mirrored orange bags, 3 dull gray bags, 1 muted magenta bag.
drab white bags contain 2 faded tan bags, 3 wavy aqua bags.
shiny tomato bags contain 4 dim coral bags, 3 dotted lime bags.
wavy plum bags contain 1 bright orange bag.
dull crimson bags contain 2 pale silver bags, 1 light beige bag, 4 wavy violet bags.
dotted violet bags contain 4 light indigo bags, 1 dark black bag, 3 pale green bags.
dark salmon bags contain 5 light tan bags, 4 dim chartreuse bags, 5 faded green bags, 3 light brown bags.
dull brown bags contain 5 mirrored aqua bags, 5 dim magenta bags, 4 light brown bags, 5 plaid black bags.
shiny chartreuse bags contain 5 wavy yellow bags, 3 faded aqua bags, 1 bright fuchsia bag, 5 drab plum bags.
muted red bags contain 3 drab white bags, 5 dim beige bags, 4 bright olive bags.
posh blue bags contain 1 dotted beige bag, 1 vibrant cyan bag, 4 vibrant brown bags, 2 clear turquoise bags.
wavy bronze bags contain 4 wavy turquoise bags, 4 dim bronze bags, 3 shiny beige bags, 2 dull lavender bags.
posh beige bags contain 3 muted gray bags, 4 light salmon bags, 5 striped turquoise bags.
vibrant red bags contain 5 muted blue bags.
dark olive bags contain 5 dark maroon bags.
dotted gray bags contain 3 wavy magenta bags.
vibrant cyan bags contain 5 dotted lavender bags, 3 vibrant orange bags.
dark chartreuse bags contain 3 pale white bags, 1 dull lavender bag.
faded lime bags contain 4 clear green bags, 3 shiny plum bags, 2 light green bags.
vibrant blue bags contain 1 wavy turquoise bag, 4 dim salmon bags.
dull tan bags contain 3 dim chartreuse bags, 1 plaid tomato bag, 4 dark brown bags.
muted gray bags contain 4 clear tan bags, 3 wavy aqua bags, 5 dim white bags.
clear yellow bags contain 1 drab white bag, 5 dark salmon bags, 2 dull yellow bags.
clear tomato bags contain 2 dotted gray bags, 5 vibrant beige bags, 1 bright maroon bag, 2 drab green bags.
shiny tan bags contain 5 posh lavender bags, 5 pale yellow bags.
dark black bags contain 4 muted purple bags, 5 light gray bags, 5 drab red bags.
striped plum bags contain 3 dull red bags, 1 dark tomato bag, 4 dark yellow bags, 5 plaid cyan bags.
light gray bags contain 3 plaid chartreuse bags.
light aqua bags contain 4 wavy magenta bags, 3 light black bags.
vibrant brown bags contain 1 bright blue bag, 1 posh black bag.
posh tomato bags contain 5 wavy magenta bags.
dotted bronze bags contain 4 mirrored chartreuse bags.
mirrored violet bags contain 2 clear maroon bags, 1 light red bag, 4 mirrored gray bags.
dark purple bags contain 5 bright blue bags, 3 plaid blue bags.
faded beige bags contain 4 plaid bronze bags, 5 vibrant turquoise bags, 3 pale orange bags, 5 mirrored aqua bags.
mirrored green bags contain 1 dotted fuchsia bag, 5 light indigo bags, 3 shiny beige bags.
striped violet bags contain 5 drab silver bags, 2 dim crimson bags, 3 plaid blue bags.
mirrored tomato bags contain 5 light lavender bags.
posh purple bags contain 3 pale orange bags.
dim blue bags contain 5 dotted plum bags, 1 light orange bag, 4 dim maroon bags.
dark cyan bags contain 4 vibrant white bags, 4 dull white bags, 1 posh purple bag.
drab beige bags contain 5 dull purple bags.
vibrant olive bags contain 5 light silver bags.
plaid beige bags contain 3 muted silver bags, 4 vibrant orange bags.
wavy silver bags contain 2 dim crimson bags, 4 shiny maroon bags, 4 pale indigo bags.
posh crimson bags contain 2 light violet bags, 4 pale coral bags, 3 plaid bronze bags.
vibrant crimson bags contain 3 dull red bags.
dotted olive bags contain no other bags.
mirrored beige bags contain 2 plaid gray bags, 5 mirrored yellow bags.
bright brown bags contain 2 faded aqua bags, 1 dim tomato bag, 5 posh magenta bags.
bright magenta bags contain 2 posh gray bags, 3 dim salmon bags.
clear magenta bags contain 2 dim cyan bags, 3 clear red bags, 1 dull fuchsia bag, 4 wavy coral bags.
clear lime bags contain 5 dull green bags, 2 shiny bronze bags, 2 faded orange bags, 1 bright beige bag.
muted tan bags contain 4 vibrant maroon bags, 3 vibrant black bags, 5 shiny maroon bags, 5 vibrant turquoise bags.
pale beige bags contain 3 light tomato bags.
dark fuchsia bags contain 2 faded brown bags, 3 dotted lavender bags, 4 shiny teal bags, 2 bright blue bags.
dim magenta bags contain 4 posh chartreuse bags.
bright aqua bags contain 5 drab violet bags.
striped crimson bags contain 2 bright green bags.
dull chartreuse bags contain 4 plaid bronze bags, 2 shiny gray bags, 4 dull lavender bags.
wavy chartreuse bags contain 1 vibrant tomato bag, 1 dim tomato bag, 3 pale green bags, 1 posh plum bag.
dotted white bags contain 1 dark teal bag, 4 dotted violet bags, 5 bright beige bags, 3 dim silver bags.
mirrored purple bags contain 1 posh green bag.
faded bronze bags contain 4 dotted indigo bags.
faded lavender bags contain 3 muted purple bags.
clear turquoise bags contain 4 muted orange bags, 1 striped violet bag, 5 clear tan bags, 5 dim white bags.
shiny plum bags contain 4 dim crimson bags.
wavy fuchsia bags contain 3 dotted brown bags, 5 dark magenta bags, 2 dark bronze bags.
faded olive bags contain 5 plaid indigo bags.
mirrored orange bags contain 4 striped violet bags, 2 light violet bags, 4 shiny orange bags.
pale indigo bags contain 3 shiny indigo bags.
faded tan bags contain 3 shiny maroon bags, 5 posh aqua bags, 1 striped violet bag, 2 dim white bags.
bright chartreuse bags contain 1 posh black bag, 5 bright gray bags, 3 plaid chartreuse bags.
drab blue bags contain 1 pale violet bag, 4 vibrant green bags.
posh tan bags contain 4 shiny lime bags.
plaid maroon bags contain 2 dotted black bags.
dull coral bags contain 4 posh coral bags, 1 dotted silver bag, 5 drab beige bags, 1 plaid red bag.
striped yellow bags contain 1 plaid tomato bag, 1 dotted lavender bag.
muted magenta bags contain 4 muted black bags.
dotted cyan bags contain 1 vibrant tomato bag, 3 light indigo bags, 1 wavy turquoise bag.
dim lavender bags contain 1 muted black bag, 4 pale white bags, 2 mirrored coral bags, 5 pale brown bags.
bright gold bags contain 5 vibrant green bags.
light white bags contain 2 striped lime bags, 2 muted lime bags, 5 muted brown bags, 4 bright green bags.
wavy lavender bags contain 2 vibrant purple bags, 5 posh white bags.
clear black bags contain 2 posh turquoise bags, 3 dotted orange bags, 3 faded teal bags.
muted crimson bags contain 1 pale violet bag, 5 drab lavender bags.
posh green bags contain 4 vibrant beige bags, 5 dark purple bags, 3 dim salmon bags, 3 light black bags.
vibrant silver bags contain 3 posh coral bags, 4 posh white bags.
dim coral bags contain 2 posh violet bags, 1 dark cyan bag, 3 shiny green bags, 3 vibrant cyan bags.
striped red bags contain 5 muted olive bags, 4 wavy teal bags, 3 shiny gray bags, 1 mirrored coral bag.
bright violet bags contain 3 shiny beige bags, 1 wavy magenta bag, 5 light indigo bags.
vibrant magenta bags contain 4 striped salmon bags, 1 light tan bag.
faded gold bags contain 5 light tomato bags, 1 wavy black bag, 4 faded maroon bags.
muted plum bags contain 1 vibrant brown bag, 2 muted cyan bags, 4 muted salmon bags.
plaid gold bags contain 5 shiny beige bags, 3 faded fuchsia bags, 5 vibrant cyan bags, 5 shiny gold bags.
striped indigo bags contain no other bags.
wavy gray bags contain 2 plaid indigo bags, 3 clear tomato bags, 4 dull blue bags.
plaid silver bags contain 5 clear salmon bags, 5 faded lime bags, 4 shiny tan bags, 5 mirrored chartreuse bags.
plaid yellow bags contain 4 shiny chartreuse bags, 1 light lime bag, 2 dull green bags.
plaid turquoise bags contain 3 dotted aqua bags, 3 posh magenta bags.
striped olive bags contain 2 faded aqua bags, 5 dotted orange bags, 5 dull turquoise bags, 1 pale violet bag.
faded teal bags contain 3 striped indigo bags.
dull red bags contain 1 mirrored gray bag, 4 drab coral bags, 2 bright plum bags, 1 dull green bag.
dull gold bags contain 5 bright blue bags.
shiny magenta bags contain 1 light white bag.
striped green bags contain 1 clear blue bag.
dull teal bags contain 3 dark purple bags, 4 dim lime bags, 5 clear chartreuse bags.
faded magenta bags contain 4 shiny gray bags, 5 pale crimson bags, 5 light coral bags, 2 pale white bags.
pale tomato bags contain 4 dull black bags, 1 posh chartreuse bag, 1 faded cyan bag.
muted blue bags contain 5 striped white bags, 1 faded orange bag.
light blue bags contain 4 posh white bags.
plaid chartreuse bags contain 2 bright gray bags.
dull aqua bags contain 5 clear tan bags, 5 dotted red bags, 5 vibrant tomato bags.
light lavender bags contain 5 clear fuchsia bags, 1 striped olive bag.
bright green bags contain 4 vibrant violet bags, 2 vibrant maroon bags.
light beige bags contain 1 striped maroon bag.
drab indigo bags contain 4 posh tomato bags, 5 faded brown bags.
dotted yellow bags contain 3 wavy violet bags, 4 bright violet bags, 4 vibrant lime bags, 1 pale beige bag.
striped gold bags contain 2 light indigo bags, 3 dull red bags, 5 vibrant beige bags.
muted indigo bags contain 5 bright purple bags, 1 pale plum bag, 5 wavy black bags.
dark lime bags contain 2 faded blue bags.
shiny white bags contain 4 clear tan bags, 3 pale yellow bags, 5 plaid tomato bags, 4 wavy turquoise bags.
vibrant maroon bags contain 4 dark red bags, 2 dull aqua bags, 5 wavy aqua bags.
drab teal bags contain 3 shiny indigo bags.
bright plum bags contain 2 plaid chartreuse bags.
vibrant yellow bags contain 3 posh purple bags.
posh salmon bags contain 4 dim plum bags, 1 pale yellow bag, 2 shiny gold bags.
shiny black bags contain 3 dim magenta bags.
bright gray bags contain no other bags.
dull orange bags contain 3 dotted purple bags.
pale purple bags contain 2 bright cyan bags, 2 drab teal bags, 2 dotted gold bags, 4 mirrored fuchsia bags.
dull yellow bags contain 3 posh gray bags.
muted tomato bags contain 3 faded orange bags.
drab olive bags contain 4 dim maroon bags, 1 bright turquoise bag, 3 shiny indigo bags, 5 vibrant lavender bags.
clear salmon bags contain 2 dim chartreuse bags, 2 shiny black bags, 5 dotted indigo bags, 3 dotted aqua bags.
posh black bags contain 2 wavy turquoise bags, 2 shiny plum bags, 2 mirrored gold bags.
light gold bags contain 5 shiny tomato bags, 4 light cyan bags.
shiny coral bags contain 3 faded silver bags.
plaid magenta bags contain 1 vibrant black bag, 2 bright blue bags.
dotted teal bags contain 4 faded olive bags, 5 vibrant brown bags, 3 clear salmon bags.
striped purple bags contain 5 shiny bronze bags.
dim tan bags contain 2 light tan bags, 1 dotted gold bag, 3 shiny white bags.
light silver bags contain 5 dotted cyan bags, 4 dotted aqua bags.
dull white bags contain 5 striped turquoise bags.
plaid aqua bags contain 3 dim bronze bags, 5 dull brown bags, 3 faded plum bags, 2 mirrored crimson bags.
dotted silver bags contain 1 faded teal bag.
dull olive bags contain 1 dark turquoise bag, 3 muted orange bags.
clear purple bags contain 3 drab salmon bags.
mirrored plum bags contain 1 vibrant lavender bag.
bright beige bags contain 4 plaid magenta bags, 1 dull turquoise bag, 4 dim white bags, 1 light aqua bag.
pale red bags contain 1 muted lavender bag, 2 vibrant teal bags, 4 plaid cyan bags, 5 dull orange bags.
drab orange bags contain 3 bright plum bags, 5 vibrant chartreuse bags.
mirrored gold bags contain 2 wavy magenta bags.
posh maroon bags contain 3 dotted lime bags, 2 muted black bags, 3 faded green bags.
clear white bags contain 4 pale black bags.
pale silver bags contain 2 dim coral bags, 2 dull lavender bags, 2 dark teal bags, 3 wavy green bags.
vibrant tomato bags contain 5 dull lavender bags.
striped orange bags contain 5 shiny salmon bags, 1 pale gold bag, 4 mirrored gray bags, 1 plaid black bag.
dim beige bags contain 5 dim salmon bags, 2 striped yellow bags, 5 shiny orange bags, 5 light salmon bags.
clear gold bags contain 2 dim salmon bags, 4 vibrant cyan bags.
dim teal bags contain 3 light indigo bags, 3 pale green bags, 5 muted bronze bags.
shiny silver bags contain 3 drab red bags, 1 pale magenta bag, 3 plaid blue bags, 4 pale white bags.
dark beige bags contain 4 posh black bags, 1 dark maroon bag.
bright bronze bags contain 4 mirrored yellow bags, 1 vibrant salmon bag, 2 mirrored teal bags, 1 shiny beige bag.
dotted maroon bags contain 1 clear tomato bag.
bright olive bags contain 3 striped tomato bags, 3 plaid indigo bags, 3 posh magenta bags.
faded tomato bags contain 5 bright violet bags.
mirrored magenta bags contain 3 wavy coral bags, 4 dull tan bags, 3 wavy chartreuse bags.
striped aqua bags contain 3 drab teal bags, 3 drab crimson bags, 5 plaid gold bags, 2 vibrant aqua bags.
clear crimson bags contain 5 striped chartreuse bags, 5 vibrant blue bags.
striped blue bags contain 4 dull red bags, 3 vibrant white bags, 4 posh black bags.
posh olive bags contain 5 muted cyan bags.
plaid indigo bags contain 5 dotted fuchsia bags, 2 plaid chartreuse bags, 3 vibrant blue bags.
mirrored lime bags contain 2 dotted lavender bags, 2 wavy bronze bags.
wavy blue bags contain 5 mirrored green bags, 5 faded tomato bags, 1 posh turquoise bag.
light fuchsia bags contain 3 faded tomato bags, 5 muted beige bags, 2 faded beige bags, 4 wavy indigo bags.
dull plum bags contain 4 dark blue bags, 5 shiny maroon bags, 3 pale gray bags, 5 drab lime bags.
drab fuchsia bags contain 3 dark maroon bags.
pale teal bags contain 4 vibrant blue bags, 1 bright green bag, 3 dim crimson bags, 1 posh salmon bag.
dull tomato bags contain 3 dim maroon bags, 4 plaid gray bags, 5 striped gold bags, 5 striped white bags.
pale orange bags contain 4 drab yellow bags.
wavy aqua bags contain 1 dim bronze bag.
dim chartreuse bags contain 2 bright violet bags.
dotted crimson bags contain 5 vibrant orange bags, 4 wavy magenta bags.
faded cyan bags contain 3 mirrored blue bags, 3 shiny fuchsia bags, 4 bright indigo bags.
pale salmon bags contain 2 pale cyan bags, 2 muted lime bags, 2 vibrant plum bags.
drab lime bags contain 2 drab yellow bags, 2 light magenta bags, 3 dotted fuchsia bags.
shiny bronze bags contain 1 posh lavender bag.
dim fuchsia bags contain 5 dotted gold bags, 5 vibrant indigo bags, 4 shiny teal bags, 2 dotted silver bags.
dark green bags contain 2 shiny blue bags.
bright red bags contain 2 pale brown bags, 3 plaid blue bags, 4 drab bronze bags, 3 dim yellow bags.
clear teal bags contain 2 drab white bags, 3 muted beige bags.
pale aqua bags contain 4 light tan bags.
dull lavender bags contain 1 dim bronze bag, 5 dim crimson bags, 1 dotted olive bag.
dotted plum bags contain 1 light black bag.
shiny teal bags contain 3 light indigo bags.
dotted lime bags contain 1 shiny gold bag, 3 plaid crimson bags.
dark tan bags contain 5 faded tan bags.
vibrant indigo bags contain 3 shiny fuchsia bags.
light tan bags contain 4 pale yellow bags, 1 pale crimson bag, 3 light gray bags.
drab plum bags contain 2 shiny turquoise bags, 2 vibrant yellow bags, 4 muted brown bags, 2 drab lavender bags.
dim white bags contain 5 dark red bags, 5 dotted olive bags.
light red bags contain 2 vibrant indigo bags, 1 wavy salmon bag, 3 dull brown bags.
mirrored fuchsia bags contain 5 dotted tomato bags.
mirrored indigo bags contain 5 pale lime bags, 5 light magenta bags, 4 light gray bags, 2 dull red bags.
dim yellow bags contain 2 muted beige bags, 2 plaid olive bags, 3 faded aqua bags.
shiny gray bags contain 1 drab yellow bag, 3 shiny lavender bags, 1 posh white bag.
faded violet bags contain 2 bright olive bags, 5 clear gray bags, 2 dark orange bags, 1 pale magenta bag.
mirrored black bags contain 4 clear blue bags.
drab aqua bags contain 1 vibrant crimson bag, 4 clear fuchsia bags.
pale black bags contain 5 pale turquoise bags, 4 striped yellow bags, 4 dotted beige bags.
wavy cyan bags contain 1 vibrant brown bag.
dark silver bags contain 3 light tomato bags, 5 dotted lavender bags, 3 bright turquoise bags.
faded orange bags contain 3 clear turquoise bags, 3 mirrored gold bags, 2 plaid bronze bags, 2 dotted fuchsia bags.
drab crimson bags contain 5 clear blue bags.
posh magenta bags contain 1 bright violet bag, 2 dotted beige bags, 2 bright gray bags.
posh brown bags contain 3 dim tomato bags, 1 dim chartreuse bag, 5 shiny orange bags.
drab gray bags contain 3 striped violet bags.
pale cyan bags contain 5 dotted aqua bags, 3 striped tomato bags.
wavy tan bags contain 3 pale indigo bags.
plaid brown bags contain 2 dotted indigo bags, 1 dull indigo bag, 2 light brown bags.
vibrant beige bags contain 1 shiny teal bag, 3 vibrant cyan bags, 2 posh gray bags, 3 striped tomato bags.
shiny aqua bags contain 2 vibrant black bags, 2 muted coral bags, 4 vibrant coral bags.
mirrored silver bags contain 3 drab silver bags, 1 clear turquoise bag.
pale tan bags contain 3 pale magenta bags.
striped cyan bags contain 5 drab tomato bags.
mirrored coral bags contain 1 mirrored crimson bag, 1 bright maroon bag.
pale white bags contain 4 shiny beige bags, 1 shiny maroon bag, 5 dim bronze bags.
shiny beige bags contain 3 mirrored gold bags.
mirrored chartreuse bags contain 1 dotted tomato bag, 2 bright cyan bags.
wavy red bags contain 1 posh lavender bag, 1 vibrant blue bag, 3 muted brown bags.
muted chartreuse bags contain 3 dim lavender bags, 4 pale plum bags, 4 light magenta bags.
shiny purple bags contain 4 muted green bags, 5 light white bags, 2 faded tan bags, 5 light beige bags.
clear tan bags contain 3 dotted red bags, 1 striped violet bag, 4 plaid chartreuse bags.
bright teal bags contain 1 faded black bag, 3 faded maroon bags.
posh orange bags contain 5 light gold bags, 3 posh aqua bags.
striped gray bags contain 2 bright plum bags, 2 shiny gray bags.
dim lime bags contain 1 plaid blue bag.
posh fuchsia bags contain 1 dull indigo bag, 2 plaid blue bags.
dotted tomato bags contain no other bags.
dim plum bags contain 1 dim chartreuse bag.
dim orange bags contain 2 muted magenta bags, 5 faded aqua bags.
posh gold bags contain 5 light maroon bags, 4 dark turquoise bags, 1 posh white bag, 5 wavy beige bags.
striped bronze bags contain 1 dark magenta bag.
wavy lime bags contain 4 mirrored lavender bags, 3 pale bronze bags, 1 dull white bag.
pale magenta bags contain 2 dim crimson bags, 4 plaid plum bags, 5 muted silver bags, 2 dim yellow bags.
striped chartreuse bags contain 5 light black bags, 3 bright fuchsia bags, 4 pale black bags.
vibrant tan bags contain 2 dim tan bags.
shiny crimson bags contain 5 pale beige bags, 3 clear purple bags, 2 pale violet bags, 4 dotted chartreuse bags.
vibrant orange bags contain no other bags.
striped silver bags contain 5 clear orange bags, 2 dotted fuchsia bags.
clear cyan bags contain 5 muted gray bags, 3 wavy aqua bags.
light black bags contain 1 striped yellow bag.
muted white bags contain 3 muted tomato bags, 5 light black bags, 4 pale black bags, 5 shiny gold bags.'''

	test_bag_rules: dict = create_rules_dict(part_1_test_input)
	real_bag_rules: dict = create_rules_dict(part_1_real_input)

	part_1_test_result = find_outer_bag_possibilities("shiny gold", test_bag_rules)
	part_1_real_result = find_outer_bag_possibilities("shiny gold", real_bag_rules)

	print(f"Amount of possible outer bags (test): {part_1_test_result}")
	print(f"Amount of possible outer bags (real): {part_1_real_result}")


def create_rules_dict(raw_rules_input: str) -> dict:
	"""
	Creates dict with rules from raw str input

	:param raw_rules_input: String of written rules
	:type raw_rules_input: str
	:return: Dictionary with processed rules
	:rtype: dict
	"""
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


def find_outer_bag_possibilities(bag_color: str, bag_rules: dict) -> int:
	"""
	Finds possible outer bags, based on rules and given bag color

	:param bag_color: String describing chosen color
	:param bag_rules: Dictionary of rules
	:type bag_color: str
	:type bag_rules: dict
	:return: Number of all possible outer bag colors
	:rtype: int
	"""
	allowed_outer_bags: list = []
	for rule in bag_rules:
		if bag_color in can_hold_bags(rule, bag_rules):
			if rule not in allowed_outer_bags:
				allowed_outer_bags.append(rule)
		else:
			for color in can_hold_bags(rule, bag_rules):
				if bag_color in can_hold_bags(color, bag_rules):
					if rule not in allowed_outer_bags:
						allowed_outer_bags.append(rule)

	return len(allowed_outer_bags)


def can_hold_bags(rule: str, bag_rules: dict) -> dict:
	"""
	Returns a dict of all bags that can be held by given bag color

	:param rule: Color of a given bag
	:param bag_rules: Dictionary of rules
	:type rule:  str
	:type bag_rules: dict
	:return:
	"""
	return bag_rules[rule]


if __name__ == '__main__':
	main()
