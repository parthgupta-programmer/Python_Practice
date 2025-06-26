s1={1,2,3,4,5}
s2={1,3,5,6,3}

s3= s1 | s2 # Union
print(s3)
s4= s1 & s2 # Intersection
print(s4)
s5= s1-s2   # Difference
print(s5)
s6=s2-s1    # Difference 
print(s6)