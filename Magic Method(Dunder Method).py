class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,ord2):# __gt__ is dunder function(greater than)
        return self.price>ord2.price

ord1=Order("Chips",20)
ord2=Order("Coffee",15)
print(ord1>ord2) # Returns True 


class Plus: 
    def __init__(self,a):  
        self.a=a
    def __add__(self,sec):# __add__ is dunder function(add)
        return self.a*sec.a  
    
a=Plus(5)
b=Plus(10)
print(a+b)   # Returns 50


# Dunder (double underscore) methods are special methods in Python that begin and end with double underscores.
# They are used to define or override the behavior of built-in operators for your custom classes.
# dunder function is like it denotes a operator like __gt__as greater than(>) and __add__ as (+)
# So,whenever the opeartions under these operators which is used as a dunder function is used or called ,then the operation is performed depending upon the code we have written in that particlar dunder function and will result the value accordingly.
# Like ,in the above example in the Plus Class ,i have made a dunder function to work as i wanted i.e. usually add (+) operator is used to add two numbers but in this i made it to muliply each other and return the value.
# Overall,The + operator is overridden to do multiplication (5 * 10 = 50), not addition.
