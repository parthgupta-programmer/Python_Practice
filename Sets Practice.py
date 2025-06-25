# Sets are mutable(add/remove),unordered,and unindexed.
# But ,we cannot change the items of a set , only adding and removing can be done.
# Sets cannot have a duplicate value.
# This is used when we want only unique items and do not care about the order.

# True and 1 is considered as the same value , False and 0 is considered as the same value.
# The output depends on what comes first in the sets i.e. when the 1 comes first ,it will be considered for the True
# but when the True comes first , it will be considered for the value 1 

s1={1,2,3,2,3,True} 
print(s1) #O/P: {1,2,3} In this case,1 is printed

# But in this case:
s2={True,1,2,3,2,3,1,8,7}
print(s2)  #O/P: {True,2,3} In this case ,True is printed

# We cannot change the item of a set,rather we can add or remove the item fron the sets.
# add() method 

s1.add(4)
print(s1)   # O/P : {1, 2, 3, 4}

# update() method

s1.update((5,6,7)) 
print(s1)   # O/P : {1, 2, 3, 4, 5, 6, 7}

# remove() method

s2.remove(1) # s2 does not contain 1 but True is deleted as True and 1 is considered as same.
print(s2) # O/P : {2, 3, 8 ,7}

# pop() method 

s2.pop() #Since ,sets are unindexed ,there is no parameter passed into the pop method here.If any integer is passed it will raise a Type Error.
print(s2) # O/P :  {3, 7, 8} [Any random value is deleted from the set]


# clear() method 

s1.clear()  
print(s1) # O/P : set() [It deletes all the elements present in the set]

# del method 

del s2
print(s2)


