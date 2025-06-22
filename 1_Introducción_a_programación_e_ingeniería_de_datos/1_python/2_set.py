# .add .rmove .discard .clear .pop .union .intersection .difference .symmetric_difference

set_countries = {"Spain", "France", "Germany", "Italy", "Portugal"}
size = len(set_countries)

print("Spain" in set_countries)

# add
set_countries.add("Greece")
print(set_countries)

# update
set_countries.update(["Greece", "Sweden", "Norway"])

# remove
set_countries.remove("Greece")  # Raises KeyError if "Greece" is
print(set_countries)

set_countries.discard("Greece")  # Does not raise an error if "Greece" is not present
print(set_countries)

set_countries.clear()  # Removes all elements from the set
print(set_countries)
print("Size of set_countries:", (len(set_countries)))