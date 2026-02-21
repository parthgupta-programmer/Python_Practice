# setdefault method is used to return the specified value for the key ,and if the key does not exist it creates the key
# dictionary.setdefault(keyname,value)

# keyname is required whereas the value is optional and if the value exists the this parameter has no effect.and if the value does not exist this value becomes the key'value.
# default value None 


d1={"Brand":"Ford","Model":"Mustang","Year":1964}
x= d1.setdefault("Color","Black") # value exist
print(x)
print(d1)


# O/P :
# Black
# {'Brand': 'Ford', 'Model': 'Mustang', 'Year': 1964, 'Color': 'Black'}


d2={"Brand":"Ford","Model":"Mustang","Year":1964}
x=d2.setdefault("Color") # value does not exist ,by default the value of this key gets stored as None.
print(x)
print(d2)

# O/P :
# None
# {'Brand': 'Ford', 'Model': 'Mustang', 'Year': 1964, 'Color': None}
