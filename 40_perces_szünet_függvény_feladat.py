# def sum_of_numbers(a_szam, b_szam):
#     print(a_szam+b_szam)
#
#
# a_szam = int(input("Adj meg egy számot! "))
# b_szam = int(input("Adj meg még egy számot! "))
# sum_of_numbers(a_szam, b_szam)

# def sum_list():
#     numbers = [1, 2, 5, 8]
#     print(sum(numbers))

# numbers = [2, 3, 6, 8, 4]
#
# def sum_list(numbers):
#     sum = 0
#     for i in numbers:
#         sum += i
#     print(sum)
#
# sum_list(numbers)
#
numbers = [1, 2, 5, 8]
#
# def sum_list(numbers):
#     print(sum(numbers))
#
# sum_list(numbers)

def sum_list(numbers):
    result = 0
    for number in numbers:
        result += number
    print(result)

sum_list(numbers)