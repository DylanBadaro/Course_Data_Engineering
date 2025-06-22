import random

countries = ['Spain', 'France', 'Germany', 'Italy', 'Portugal']
population_v2 = {country: random.randint(1,100) for country in countries}
print(population_v2)  # Output: {'Spain': 23, 'France':


result = {country : population for (country, population) in population_v2.items() if population > 20}
print(result)  # Output: {'Spain': 23, 'France': 45, 'Germany': 67, 'Portugal': 89} (example output)