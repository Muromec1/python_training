# Hány számot szeretnél megadni?
# 3
# Kérél be tőle pont annyi számot, mint amit az előbb megadott
# Összegezzük a felhasználó által megadott csak pozitív számokat

# total_number_of_numbers = int(input("Hány számot szeretnél megadni? "))
# if total_number_of_numbers == 3:
#     numbers = int(input("Írj be tetszőleges 3 számot! "))
# sum = 0

# total_number_of_numbers = int(input("Hány számot szeretnél megadni? "))
# for i in range (0, total_number_of_numbers)
#     numbers = int(input("Írj be 3 számot! "))

# Tanár
count = int(input("Hány számot szeretnél megadni? "))
for i in range(count):
    number = int(input("Add meg a " + str(i+1) + ". számot! "))
    print("A megadott szám:", number)
    if number > 0:
        sum += number
        print("Részösszeg:", sum)
print("Végső összeg:", sum)