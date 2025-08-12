# A Generator in Python is a special kind of function that remembers its state and can be paused and resumed.
# Instead of returning all results at once (like a list), it yields one result at a time when you loop over it.

# yield is like return, but instead of ending the function, it pauses it and remembers where it left off.
# When you call the generator again, it continues right after the last yield.

def normal_function():
    return 1
    return 2
def generator_function():
    yield 1
    yield 2

print(normal_function()) # 1
print(normal_function()) # 1

gen=generator_function() 

print(next(gen))  # 1
print(next(gen))  # 2