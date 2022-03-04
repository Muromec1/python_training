names = []
print(names)

names.append("John Doe")
print(names)

names.append("Jack Doe")
print(names)

names.append("Jane Doe")
print(names)

print(names[0])

print(names[0:2])
print(names[::-1])


names[1] = "Jack Smith"
print(names)

names.remove("Jack Smith")
print(names)

numbers = [1, 2, 3]
print(numbers)

employee = ["John Doe", 20]
print(employee)
print(employee[0])
print(employee[1])



print(len(employee))

print(names)
print("John Doe" in names)
print("Jane Smith" in names)

for name in names:
    print(name)


## Feladat: Írj egy függvényt, ami paraméterül kap egy listát és visszaad egy listát.
## és visszaad egy másik listát. De a másik listában csak
## azok a nevek legyenek benne, akik John-nal kezdődnek.

# ["John Smith", "Jane Smith", "Jack Doe", "John Doe"]

# def filter_out_names():
#     result = ""
#     for names in list:
#         if names in list == "John":
#             result += names
#         return result
#
# print(filter_out_names("John Smith", "Jane Smith", "Jack Doe", "John Doe"))

# Tanár megoldása:
def filter_johns(names: list) -> list:
    result = []
    for name in names:
        if "John" in name and name.index("John") == 0:
            result.append(name)
        return result

print(filter_johns(["John Smith", "Jane Smith", "Jack Doe", "John Doe"]))