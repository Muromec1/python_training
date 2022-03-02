number = int(input("Adj meg egy számot! "))
while number != 0:
    print(number * 2)
 #
number = 10
while number != 0:
    number = int(input("Adj számot! "))
    print2(number * 2)
#
    num = int(input("Adj meg egy szamot: "))

    while num != 0:
        print(num * 2)
        num = int(input("Adj meg egy szamot: "))
    print("End")
#
    number = 1
    while number != 0:
        number = input("Adj meg egy számot, én meg duplázom. Exit = 0. Számod: ")
        if (int(number) == 0):
            break
        print("Duplája: " + str(int(number) * 2))
    print("End")
    #