#Iterator : An iterator is a Python object that allows you to traverse elements of a collection one by one without needing to know how the collection is stored internally.

# When we do:
nums=[1,2,3,4,5]
for num in nums:
    print(num)

# Output:
# 1
# 2
# 3
# 4
# 5

# Python automatically converts it internally to:

# iterator=iter(nums)
# while True:
#     try:
#         num=next(iterator)
#         print(num)
#     except StopIteration:
#         break

# So for loop works using iterators internally.

print("\n")

# Example of Iterator using Built-in Function

iterator=iter(nums)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# Output:
# 1
# 2
# 3
# 4
# 5

print("\n")

# Creating my own iterator

# Iterator that prints numbers from 1 to 10 

class Counter:
    def __init__(self,max):
        self.max=max
        self.current=1
    def __iter__(self):
        return self
    def __next__(self):
        if(self.current <= self.max):
            value=self.current
            self.current+=1
            return value
        else:
            raise StopIteration
    
counter=Counter(10)
for num in counter:
    print(num)

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10