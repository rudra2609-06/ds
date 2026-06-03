t1 = (1,2,3,4)

# 4 common function for all sequence data types
print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))
print(sorted(t1,reverse=True))


#sum 
print(sum(t1))

#count

print(t1.count(5)) #0
print(t1.count(2)) #0

#index
print(t1.index(2)) #1
print(t1.index(20)) #error


