# print("Gondolj egy számra 1 és 100 között, én kitalálom.")
# interval_start = 1
# interval_end = 100
# bigger_or_lower = "a"
# while bigger_or_lower != "E":
#     guess = int((interval_start+interval_end) / 2)
#     bigger_or_lower = input("A szám amire gondoltál Nagyobb [N] / Kisebb [K] / Egyenlő [E] mint " + str(guess) + " ? - ")
#     if bigger_or_lower == "K":
#         interval_end = guess-1
#     if bigger_or_lower == "N":
#         interval_start = guess+1
# print("A gondolt szám a " + str(guess))
# a jó, működő kód fent

# Én kódom:
# print("Gondolj egy számra 1 és 10 között!")
# minimum = 1
# maximum = 10
# answer = "x"
# while answer != "e":
#     guess = int((maximum+minimum) / 2)
#     answer = input("A szám amire gondoltál Nagyobb [N] / Kisebb [K] / Egyenlő [E] mint " + str(guess) + " ?")
#     if answer == "K":
#         maximum#


# Tanár:
print("Gondolj egy számra 1 és 10 között!")
min = 1
max = 10
answer = "x"
while answer != "e":
    guess = (min + max) // 2
    print("A tippem", guess)
    answer = input("k/e/n")
    if answer == "k":
        max = guess - 1
    elif answer == "n":
        min = guess + 1
print("A gondolt szám", guess)