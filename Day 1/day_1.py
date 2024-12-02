#import 

file = open("input.txt", "r")

file_lines = file.readlines()
location_ID1, loacation_ID2 = [],[]
for line in file_lines:
    location = line.split()
    location_ID1.append(location[0])
    loacation_ID2.append(location[1])


location_ID1.sort()
loacation_ID2.sort()
#print (location_ID1)

LID3 = []
x=0

while x <= 999:
    #print(location_ID1[x], loacation_ID2[x])
    LID3.insert(x, abs(int(location_ID1[x])-int(loacation_ID2[x])))
    x+=1

#print(LID3)

total = 0
for x in LID3:
    total += x

#print(total)
compares = 0

for x in location_ID1:
    count = 0
    for y in loacation_ID2:
        if x == y:
            count+=1
        else:
            pass
    compares += int(x)*count

print(compares)





