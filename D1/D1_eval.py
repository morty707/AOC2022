# The eval() function evaluates the specified expression, if the expression is a legal Python statement,
# it will be executed.

eval('print("hello world")')

Calories = sorted(eval(open("input.txt").read().replace("\n\n", ",").replace("\n", "+")), reverse=True)

print(f'Answer of Part 1 is: {Calories[0]}')
print(f'Answer of Part 2 is: {sum(Calories[0:3])}')