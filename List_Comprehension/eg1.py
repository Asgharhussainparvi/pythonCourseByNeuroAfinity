# One way
language = 'Python'
lst = list(language) 
print(type(lst))    
print(lst)           

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) 
print(lst)      


# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  
print(even_numbers)                  

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0] 
print(odd_numbers)                   

# Filter numbers:
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)                 


# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)   