
import csv 

rows=[]
with open("reindeer.csv", newline='') as fill:
    lines = csv.reader(fill, quoting=csv.QUOTE_NONNUMERIC)
    for row in lines:
        y = []
        for x in row:
            y.append((x))
        rows.append(y)

#print(rows)

"""
file_lines = file.readlines()
redFactory = []
for line in file_lines:
    linez=[]
    lines = line.rstrip('n')
    for int in eval(lines):
        
    redFactory.append((eval(lines)))
"""
#print(len(rows))
safe_1, safe_2 = [],[]
#print (redFactory)

for x in rows:
    checkFactory = []
    for y in x:
        if y != '':
            checkFactory.append(y)
        else:
            pass
    #print(len(checkFactory))
    #print(checkFactory)
    a = sorted(checkFactory)
    b = list(reversed(a))
    #print(checkFactory,x)
    c = (len(checkFactory)-1)
    track = 0
    for t in range(c):
        if t == 0:
            track += 1
            pass
        if (1 <= (checkFactory[t] - checkFactory[(t-1)]) <= 3) or (1<= (checkFactory[(t-1)] - checkFactory[t]) <= 3):
            track += 1
        else:
            pass
    print (a,b,checkFactory)

    if checkFactory == a or checkFactory == b:
        safe_1.append('Green')
        if track == c:
            safe_2.append('Green')
        else:
            safe_2.append('Red')
    else:
        safe_1.append('Red')
        if track == c:
            safe_2.append('Green')
        else:
            safe_2.append('Red')

print(len(safe_1))
print(len(safe_2))
total = 0

for x in range(len(safe_1)):
    if safe_1[x] == safe_2[x] == 'Green':
        total += 1
    else:
        pass
print (total)



