# # Named function
# def add_two_nums(a, b):
#     return a + b


# print(add_two_nums(2, 3))    
# # Lets change the above function to a lambda function
# add_two_nums = lambda a, b: a + b
# print(add_two_nums(2,3))   


# # Self invoking lambda function
# (lambda a, b: a + b)(2,3) 


# square = lambda x : x ** 2
# print(square(3))    # 9
# cube = lambda x : x ** 3
# print(cube(3))    # 27


# # Multiple variables
# multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
# print(multiple_variable(5, 5, 3))

div = lambda a, b : a/b 
print(div(10,2))


add = lambda *args: sum(args)
print(add(2,3,4,5,6,76,7,7,7,7,7,74,3,2))


def power(x):
    return lambda n : x ** n

cube = power(2)(3)  
print(cube)        
two_power_of_five = power(2)(5) 
print(two_power_of_five) 