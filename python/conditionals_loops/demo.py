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
	last_year_population = current_population - (current_population/rate)
	print(last_year_population)
	current_population = last_year_population

