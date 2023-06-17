# NOTE:
# read() will result a whole string
# readline() will result a list of each line

Calories = sorted([sum(map(int, calories.split("\n"))) for calories in open("input.txt").read().split("\n\n")], reverse=True)
print(f'Answer of Part 1 is: {Calories[0]}')
print(f'Answer of Part 2 is: {sum(Calories[0:3])}')

