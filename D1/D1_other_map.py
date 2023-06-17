# Using map() two times

Calories = [list(map(int, calories.split("\n"))) for calories in open("input.txt").read().split("\n\n")]

Calories = list(map(sum, Calories))

print(f'Answer of Part 1 is: {Calories[0]}')
print(f'Answer of Part 2 is: {sum(Calories[0:3])}')