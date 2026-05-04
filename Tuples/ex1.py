## Tuples are immutable -- can't change the value
dimensions = (200,500)
print("orginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (200,50)
print("\nmodified dimension:")
for dimension in dimensions:
    print(dimension)