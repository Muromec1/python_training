# ismetles = "Az év egyik hónapja"
# for i range ["február." , "január."]:
#     print(ismetles + i)
count = 0
for month in ["január", "február", "március"]:
    print("Az év " + str(count) + ". hónapja" + month + ".")
    # count = count + 1
    count += 1

#egyéb megoldások:
i=1
for month in ["january","february","march"]:
    print("Az év",i,". hónapja: ",month)
    i=i+1
print("end")

#
i=1
for month in ["Januar", "Februar", "Marcius"]:
    print("Az év",i, ". honapja", month)
    i=i+1