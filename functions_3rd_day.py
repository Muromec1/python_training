# Írjatok egy get_max nevű függvényt, melynek paraméterül át lehet adni 2 lebegőpontos számot.
# Adja vissza a kettő közül a nagyobbat

# def get_max(num1: float, num2: float) -> float:
#     if num1 > num2:
#         return (num1)
#     else:
#         return (num2)
#
#
# print(get_max(4.5, 7.3))
# print(get_max(8.9, 3.7))

# Írjatok egy beszédes print_square függvényt,
# ami paraméterül kap két egész számot.
# Rajzoljon ki egy ekkora téglalapot, csillagokból.
# (ciklusok)
# 4, 3
#
# ****
# *  *
# ****

# def print_square(num1, num2):
#     print(str(num1 * "*"))
#     print("*" + str((num1-2) * " ") + "*")
#     print(str(num1 * "*"))
#
#
# print_square(10, 4)

# Írjatok egy függvényt, ami paraméterül megkapja a szavak listáját
# és visszaadja ezeket összefűzve,
# de mindegyiket gondolatjel között.

# ["alma", "körte", "meggy"]
# "-alma--körte--meggy-"

# def conc_with_dash(list):
#     for word in list:
#         return word += "-" + word + "-"
#
# print(conc_with_dash(["alma", "banán", "körte"]))


# Írjatok egy beszédes print_square függvényt,
# ami paraméterül kap két egész számot.
# Rajzoljon ki egy ekkora téglalapot, csillagokból.

# def print_square(width: int, height: int) -> None:
#     full_row = width * "*"
#     print(full_row)
#     center_row = "*" + (width-2) * " " + "*"
#     for i in range(0, height - 2):
#         print(center_row)
    # print((center_row + "\n") * (width-3) + center_row))
    # print(full_row)
#
# print_square(10, 6)

# def print_square(width: int, height: int) -> None:
#     full_row = width * "*"
#     print(full_row)
#     center_row = "*" + (width-2) * " " + "*"
#     for i in range(0, height - 2):
#         print(center_row)
#     print(full_row)

# Írjatok egy függvényt, ami paraméterül megkapja
# a szavak listáját, és visszaadja ezeket összefűzve,
# de mindegyiket gondolatjel között.
# ["alma", "korte", "meggy"]
# "-alma--korte--meggy-"

def repeat_words_with_hyphens(words: list) -> str:
    result = ""
    for word in words:
        result += "-" + word + "-"
    return result

print(repeat_words_with_hyphens(["körte", "meggy", "alma"]))


# String ismétlő
def repeat_str(s: str, count: int) -> str:
    # return s * count
    result = ""
    for i in range(0, count):
        result += s
    return result

print(repeat_str("XYZ", 3))