# {key:value for vars in iterable}

# print 1st 10 numbers with their squares

# d1 = {}
# d1 = {x:x**2 for x in range(1,11)}
# print(d1)

#convert km to miles 1 km  = 0.62 miles assume

# distances = {'delhi':1000,'mumbai': 2000,'banglore': 8000}
# d2 = {key:value*0.62 for (key,value) in distances.items()}
# print(d2)


# using zip

# days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

# temp_c = [30.5,29.02,31.87,30.78,35.9,34.8,32.6]

# d1 = {key:value for (key,value) in zip(days,temp_c)}
# print(d1)

#nested comprehension 
#print table for 2 to 4 {2:{1:2,2:4},3:{1:3,2:9}}

d1 = {}

d1 = {key:{k1:k1*key for k1 in range(1,11)} for key in range(2,5)}

print(d1)

