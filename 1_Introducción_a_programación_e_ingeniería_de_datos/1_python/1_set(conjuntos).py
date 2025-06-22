set_countries = {"Spain", "France", "Germany", "Italy", "Portugal"}
print(set_countries)
print(type(set_countries))


# Checking if a country is in the set
print("Spain" in set_countries)
# Adding a new country to the set
set_countries.add("Greece")


set_numbers = {1, 2, 2, 3, 4, 5} #Does not repeat
print(set_numbers)

set_types = {1, 2.5, "Hello", (1, 2)} #Has no order
print(set_types)

set_from_string = set("Hello") 
print(set_from_string) 

set_from_tuples = set(("abc", "cbv", "as", "abc"))
print(set_from_tuples)  

numbers = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}  # Duplicates are ignored
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = set(numbers)  # Create a set to ensure uniqueness
print(unique_numbers)


