numbers = []
for element in range(1, 11):
    numbers.append(element*2)  

print(numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




# List comprehension 
numbers_v2 = [element*2 for element in range(1, 11)]
#             element      ciclo for element in range(1, 11)
print(numbers_v2)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# [element     for element in iterable            if condition]
# elemento              ciclo            condicion opcional para filtrar

prueba = [i*2 for i in range(1, 11) if i % 2 == 0]
print(prueba)  # Output: [4, 8, 12, 16, 20]

