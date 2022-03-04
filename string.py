name = "John Doe"

print(name.upper())
print(name.lower())

print(name[0])

name = name.lower()
print(name[0])

for c in name:
    print(c)

print(name[2:6])
print(name[2:])
print(name[:6])
print(name[0:7:2])
print(name[::-1])

word = "arvizturotukorfurogep"
print(word[:-1])

filename = "doom.exe"
print(filename[-3:])
ip = "192.168.0.1"
print(ip[-1:])

print("alma" == "alma")
print("alma" == "körte")

print("alma" > "korte")

print("a" in "alma")

print("gyakorlás")
# Írj egy olyan függvényt, ami megszámolja, hogy
# hány darab á betű van egy szóban!

def letter_a_counter(word):
    counter = 0
    for c in word:
        if c == "a":
            counter += counter + 1
    return counter

print(letter_a_counter("alma"))

