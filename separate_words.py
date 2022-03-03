# Írj egy olyan függvényt, mely paraméterül kap egy szavak listáját és összefűzi őket vesszővel elválasztva
# és ezzel tér vissza, de ne legyen az utsó után vesszőt

# def print_words_with_comma(words):
#     result = ","
#     for word in words:
#         (word + result)
#     return result
#
# print_words_with_comma(["alma", "banán"])

# def conc_words(words):
#     result = ""
#     i = 0
#     for word in words:
#         if i == 0:
#             result = word
#         else:
#             result = result + "," + word
#         i += 1
#     return result
#
# print(conc_words(["a", "b", "c"]))

# tanár
# def concat_words(words):
#     result = ""
#     counter = 1
#     for word in words:
#         result += word
#         if counter != len(words):
#             result += ","
#         counter += 1
#     return result

# print(concat_words(["a", "xxx", "asd"]))
#
# def concat_words(words):
#     result = ""
#     is_first = True
#     for word in words:
#         if not is_first:
#             result += ","
#         result += word
#         is_first = False
#     return result