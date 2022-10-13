import random as rand

cowokdict = {"1":"Male 1",
"2":"Male 2",
"3":"Male 3",
"4":"Male 4",
"5":"Male 5",
"6":"Male 6",
"7":"Male 7",
"8":"Male 8",
"9":"Male 9",
"10":"Male 10",
"11":"Male 11",
"12":"Male 12",
"13":"Male 13",
"14":"Male 14",
"15":"Male 15",}

cewekdict = {"1":"Female 1",
"2":"Female 2",
"3":"Female 3",
"4":"Female 4",
"5":"Female 5",
"6":"Female 6",
"7":"Female 7",
"8":"Female 8",
"9":"Female 9",
"10":"Female 10",
"11":"Female 11",
"12":"Female 12",
"13":"Female 13",
"14":"Female 14",
"15":"Female 15",
"15":"Female 15",
"16":"Female 16",
"17":"Female 17",
"18":"Female 18",}



#reset var 
lanang = []
wedok = []
#end of reset var

#randomizer 15 object
loop = 1
while loop <=15:
    randomizer = int(round(rand.random(), 3)*rand.randint(2,5) / rand.randint(80,90) * 1000)
    if randomizer > 33 or randomizer < 1:
        while randomizer > 15:
            randomizer = int(randomizer/2)
    elif randomizer <= 15:
        if randomizer < 1:
            randomizer = int((randomizer+rand.randint(1,33))/rand.randint(1,4))
        else:
            if randomizer in lanang:
                pass
            else:
                lanang.append(randomizer)
                loop = loop + 1 

# end of randomizer 15 object

#print(lanang) #ngecek value-ne lanang (15 iterable)

#randomizer 18 object
loop = 1
while loop <=18:
    randomizer = int(round(rand.random(), 3)*rand.randint(2,5) / rand.randint(80,90) * 1000)
    if randomizer > 33 or randomizer < 1:
        while randomizer > 18:
            randomizer = int(randomizer/2)
    elif randomizer <= 18:
        if randomizer < 1:
            randomizer = int((randomizer+rand.randint(1,33))/rand.randint(1,4))
        else:
            if randomizer in wedok:
                pass
            else:
                wedok.append(randomizer)
                loop = loop + 1 
#end of randomizer 18 object


#print(wedok) #ngecek value-ne wedok (18 iterable)

item=[]

for x in range(len(lanang)):
    lanang[x] = str(lanang[x])

for x in range(len(wedok)):
    wedok[x] = str(wedok[x])

#print(lanang)
#print(wedok)

for x in range(len(lanang)):
    item.append(list((wedok[x], lanang[x])))


#print(item)

nameitem=[]
for x in range(len(lanang)):
    item[x][0] = cewekdict[item[x][0]]
    item[x][1] = cowokdict[item[x][1]]

item.append(list((cewekdict[wedok[15]], cewekdict[wedok[16]])))
item.append(list((cewekdict[wedok[17]], )))

for x in item:
    print(x)

