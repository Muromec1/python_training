print(5 * 6)
print(5 + 6)
print(3 / 2)
print(3 - 2)
print(5 * 6 + 12)
print((1 + 2) * 3)
print("alma" + "körte")

# Mi van ha össze akarsz adni egy stringet és egy int-et?
# Mi van fordítva
# Mi van ha egy stringből ki akarsz vonni egy másikat
# Mi van ha egy stringet megszorzol egy másik stringgel?
# Mi van, ha egy stringet megszorzol egy int-tel?

#print("tojás" * 5)
#print("tojás" + 5)
#print(5 + "tojás")
#print("tojás" - "fehérje")
# print("tojás" * "fehérje")
result = 6 * 5 + 2
print(result)

number_of_apples_per_basket = 5
number_of_baskets = 3
number_of_all_apples = number_of_apples_per_basket * number_of_baskets
print(number_of_all_apples)

name = "John Doe"
message = "A name valtozo tipusa: " + str(type(name))
print(message)

print("Az almák száma: " + str(type(name)))

six = 6
print(six)

print(len("hello"))
length_of_hello = len("Hello")
print(length_of_hello)

# Hozzatok létre egy változót, hogy órák száma, hours - értéke 5
# Hozzatok létre még1 változót, hogy minutes, tartalmazza, hogy - előző változó szorzása 60-nal
# 3 óra az 180 perc - számok helyén használjátok az hours és minutes változókat

hours = 3
minutes = hours * 60
# print(str(hours) + " óra az " + str(minutes) + " perc")
message = str(hours)
message = message + " óra az "
message = message + str(minutes)
message = message + " perc"
print(message)


number = 5
print(number)
number = number + 3
print(number)

# Hozzatok létre egy word nevű változót és adjátok neki értékül egy nagyon hosszú szót:
# számoljátok ki a hosszát
# A "csúnya hosszú" szó pontosan 13 karakter (szavakkal)

word = "kerekpar"
print(len(word))
print("kerekpar szó pontosan" + str(len(word)))

word = "huezdenagyonhosszuszomintahogyafeladatkerte"
print("A " + word + " pontosan " + str(len(word)) + " karakter hosszú.")

fruit = "alma"
print('gyumolcs: "' + fruit + '"')



print(5 // 2)
print(5 % 2)