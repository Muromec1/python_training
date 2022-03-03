# Hozz létre egy "is_even" nevű függvényt, amely True-t ad vissza, ha a paraméterként megadott érték páros,
# egyéb esetben False-t adjon vissza

# parameter = int(input("Adj meg egy számot! "))
# def is_even(parameter):
#     if parameter % 2 == 0:
#         print(True)
#     else:
#         print(False)

# is_even(3)

# def is_even(value):
#     if value % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even(1))
# print(is_even(2))
#
# def sum_negatives(list):
#     list = [3, 5, 8, 2]
#     sum = 0
#     for sum in list:
#         sum += list
#
# sum_negatives(list)

# sum_negativ, amely parameterul kap egy listat, es osszegzi a benne szereplo negativ szamokat, azzal ter vissza
def sum_negativ(number_list):
    sum_numbers = 0
    for number in number_list:
        if number < 0:
            sum_numbers += number
    return sum_numbers


# to_minutes fv-t, amely parameterul megkapja az orak szamat es visszadaja a perceket
def to_minutes(hours):
    minutes=hours*60
    return minutes


# input_number fv-t egy parameterrel. A fuggveny beker a felhasznalotol egy szoveget
# a parameterrel megadott szoveget szamma konvertalja és azt adja vissza
def input_number():
    input_text = input("Adj meg egy szamot! ")
    return int(input_text)


# irjatok egy annotate_every_even_number fv-t, amely kap egy szam listat
# a lista elemeit kiirja egymas ala, ugy, hogy minden masodik elemet egy karakterrel bentebb ir
def annotate_every_even_number(numbers_list):
    counter = 1
    for number in numbers_list:
        if counter % 2 == 1:
            print(" "+str(number))
        else:
            print(number)
        counter += 1