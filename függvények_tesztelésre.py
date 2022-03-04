# Írj egy olyan is_ascending függvényt, mely paraméterül kap
# három egész számot. A függvény True-t ad vissza,
# ha a számok szigorúan növekvő sorrendben vannak.
# Ellenkező esetben visszaad egy False értéket.
# 1, 3, 6 -> True
# 1, 10, 20 -> True
# 1, 1, 1 -> False
# 20, 10, 1 -> False
# 20, 10, 20 -> False

def is_ascending(a: int, b: int, c: int):
    if a < b < c:
        return True
    else:
        return False

# egyszerűbb megoldás:
# def is_ascending(a: int, b: int, c: int):
#     return a < b < c


# print(is_ascending(1, 5, 7))





# Írj egy word_concat függvényt, mely két szót kap
# paraméterként, és visszaadja őket összefűzve úgy,
# hogy a rövidebb legyen elől
# "alma", "korte" -> "almakorte"
# "cseresznye", "meggy" -> "meggycseresznye

def word_concat(word1, word2):
    if len(word1) < len(word2):
        return word1 + word2
    elif len(word1) == len(word2):
        return word1 + word2
    else:
        return word2 + word1

# az if-nél a <= megoldással kilőhetsz egy elif sort

# print(word_concat("alma", "körte"))
# print(word_concat("cseresznye", "meggy"))
# print(word_concat("körte", "meggy"))
