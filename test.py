# Hozzatok létre egy változót, hogy órák száma, hours - értéke 3
# Hozzatok létre még1 változót, hogy minutes, tartalmazza, hogy - előző változó szorzása 60-nal
# 3 óra az 180 perc - számok helyén használjátok az hours és minutes változókat

hours = 3
minutes = hours * 60
print(str(hours) + " óra az " + str(minutes) + " perc.")

#########
# Hozzatok létre egy word nevű változót és adjátok neki értékül egy nagyon hosszú szót:
# számoljátok ki a hosszát
# A "csúnya hosszú" szó pontosan 13 karakter (szavakkal)

word = "hosszuszogyakorlasra"
print(len(word))
print("A " + word + "szó pontosan " + str(len(word)) + " karakter hosszú.")

#########
# number = input("Random szám pls ")
# print(int(number) * 3)

###########
# Írj egy programot, ami bekérdezi először a nevedet
# Majd bekérdezi, hogy hányszor írja ki
# Írja ki ennyiszer a nevedet!
# Szorgalmi feladat: írd ki a név elé, hogy éppen hanyadjára kerül kiírásra

name = input("Neved: ")
count = int(input("Hányszor írja ki?"))

for i in range (1,count+1):
    print(str(i) + " " + name)