# A shallow copy duplicates the top-level structure of an object but shares memory references for nested objects

l1 = [1,2,3,4]
l2 = l1.copy()
l1.append(5)
print(l1)
print(l2)
# although l2 is copy of l1 inserting element in l1 will not affect l2 and inserting l2 will not affect in l1


# A deep copy duplicates the entire object hierarchy, creating completely independent copies of all nested data

l3 = [1,2,3,4]
l4 = l3
l4.append(5)
# here in this appending element in l3 will append element in l4 because it is deep copy 
print(l4)
print(l3)

