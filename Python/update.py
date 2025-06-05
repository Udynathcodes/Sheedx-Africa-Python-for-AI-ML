favourite_fruits = ("Apple", "Banana", "Cherry", "Date")
y = list(favourite_fruits)
y[1] = "orange"
favourite_fruits = tuple(y)
print(type(favourite_fruits))  # Output: <class 'tuple'>
print(favourite_fruits)  # Output: ('Apple', 'orange', 'Cherry', 'Date')