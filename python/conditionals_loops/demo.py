#345 -> 3 + 4 + 5 -> sum of digits of 3 digit number

# number = input('Enter a number: ')

# sum = 0

# sum = int(number[0]) + int(number[1]) + int(number[2])

# print('Sum is:',sum)


current_population = 10000
rate = 10
last_year_population = None
total_past_years = 10

for i in range(10,0,-1):
	last_year_population = current_population/1.1
	print(last_year_population)
	current_population = last_year_population

# sequence sum 1/1! + 2/2! + 3/3!

n = int(input('Enter n: '))
sum = 0
factorial = 1
for i in range(1,n+1):
	factorial = factorial * i
	sum += i/factorial

print(sum)
