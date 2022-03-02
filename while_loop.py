are_you_a_boy = True
print(are_you_a_boy)

is_17_lower_than_15 = False
print(is_17_lower_than_15)

print(type(are_you_a_boy))

result = 10 < 20
print(result)

result = 10 > 20
print(result)

result = 10 >= 20
print(result)

result = 10 == 20
print(result)

result = 10 == 10
print(result) #stringek esetén is hasonlóan működik

while False:
    print("Hello ciklus")

# while True:
#     print("Hello vegtelen")

# count = 0
# while count < 10:
#     print("Hello " + str(count))
#     count = count + 1
# print("End")

number = int(input("Írj be egy számot"))
while number > 0:
    print(number * 2)
