set_a = {"Spain","France","Germany","Italy","Portugal"}
set_b = {"Spain", "Argenitna"}
# Union of two sets
set_union = set_a.union(set_b)
print("Union of set_a and set_b:", set_union)
print("Union of set_a and set_b:", set_a | set_b , "\n\n")

# Intersection of two sets
set_intersection = set_a.intersection(set_b)    
print("Intersection of set_a and set_b:", set_intersection)
print("Intersection of set_a and set_b:", set_a & set_b, "\n\n")

# Difference of two sets
set_difference = set_a.difference(set_b)    
print("Difference of set_a and set_b:", set_difference)
print("Difference of set_a and set_b:", set_a - set_b, "\n\n")

# Symmetric difference of two sets
set_symmetric_difference = set_a.symmetric_difference(set_b)
print("Symmetric difference of set_a and set_b:", set_symmetric_difference)
print("Symmetric difference of set_a and set_b:", set_a ^ set_b, "\n\n")
