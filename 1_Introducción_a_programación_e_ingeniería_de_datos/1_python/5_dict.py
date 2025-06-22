#{    key : value  for var in iterable if condition  }
# elem llave-valor           ciclo            if

'''dict = {}
for i in range(1, 5):
    dict[i] = i * 2

print(dict)  # Output: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

dict_comprehension = {i: i * 2 for i in range(1,5)}
print(dict_comprehension)  # Output: {1: 2, 2: 4, 3: 6, 4: 8}


import random
countries = ['Spain', 'France', 'Germany', 'Italy', 'Portugal']
population = {}
for country in countries:
    population[country] = random.randint(1,100)

print(population)  # Output: {'Spain': 23, 'France': 45, 'Germany': 67, 'Italy': 12, 'Portugal': 89}



population_v2 = {country: random.randint(1,100) for country in countries}
print(population_v2)  # Output: {'Spain': 23, 'France':
'''

names = ['Alice', 'Bob', 'Charlie', 'David']
ages = [25, 30, 35, 40]


#print(list(zip(names, ages)))  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35), ('David', 40)]

new_dict = {name : age for (name,age) in zip(names, ages)}
print(new_dict)  # Output: {'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}