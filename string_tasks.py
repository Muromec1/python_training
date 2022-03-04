## Írj egy olyan függvényt, ami megszámolja, hogy
## hány darab a betű van egy szóban!

def letter_a_counter(word):
    counter = 0
    for c in word:
        if c == "a":
            counter = counter + 1
    return counter

print(letter_a_counter("almakutya"))

## Írj egy olyan függvényt, amely paraméterül kap
## egy szót, és megszámolja, hogy hány magánhangzó van benne

def sonant_counter(word):
    counter = 0
    for c in word:
        if c in "aeiou":
            counter = counter + 1  # vagy counter += 1
    return counter

print(sonant_counter("almakalitka"))

## Írj egy függvényt, mely kap egy szót, és visszaadja
## a benne szereplő betűket *-gal elválasztva egy stringben!
## Az utolsó karakter után ne legyen *
## xyz -> x*y*z

def concat_letter_with_star(word):
    result = ""
    for c in word:
        result += c + "*"
    return result[:-1]

print(concat_letter_with_star("alma"))

## Írj egy függvényt, ami a paraméterként átadott szóból
## kiveszi a space-eket, és azt adja vissza.

def is_reverse_equal(word: str):
    return word == word[::-1]


print(is_reverse_equal("anna"))
print(is_reverse_equal("indul a görög aludni"))
print(is_reverse_equal("indulagörögaludni"))

# Írj egy függvényt, ami a paraméterként átadott szóból
## kiveszi a space-ket, és azt adja vissza

def kill_spaces(word):
    result = ""
    for c in word:
        if c != " ":
            result += c
        return result


print(kill_spaces("alma korte barack"))
print("Üres Kód")
# üres kódot add ki!!!

name = "John Doe"
print(name.index("Doe"))
print(name.index("J"))
# print(name.index("x"))

print ("x" in name)

print("alma korte barack".split())


fruits = "alma korte barack"
fruits_list = fruits.split()
print(fruits_list)

for n in fruits_list:
    print(n)

names = "john doe jack doe jane doe"
print(names.upper()[4:15].split())

ip = "192.168.0.1"
print(ip.split("."))
for number in ip.split("."):
    print(int(number))