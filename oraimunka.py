"""#1, legkisebb érték

def feladat1():
    tomb =[]

    for i in range(3):
        tomb.append(int(input("Kérek egy számot: ")))

    print(f"A legkisebb elem:{min(tomb)}")

feladat1()

#2, legnagyobb érték

def feladat2():
    tomb =[]

    for i in range(3):
        tomb.append(int(input("Kérek egy számot: ")))

    print(f"A legnagyobb elem:{max(tomb)}")
feladat2()

#3, érdemjegy

def ertekeles(pontSzam):
    if (pontSzam<50):
        return 1
    if (50<=pontSzam<60):
        return 2
    if (60<=pontSzam<70):
        return 3
    if (70<=pontSzam<85):
        return 4
    return 5

for i in range(1):
    erdemjegy=ertekeles(int(input("Kérem a pontszámot: ")))
print(f"Az érdemjegy: {erdemjegy}")
"""

#4, osztható-e
def feladat4():
    oszthato=False
    szam=(int(input("Kérek egy számot: ")))

    if szam%3==0 or szam%5==0:
        oszthato=True
    
    if oszthato==True:
        print("Igen")
    else:
        print("Nem")

feladat4()

#5, kettő összege


#6, páros szám

#7, abc sorrend

#8, kisebb

#9, zárt intervallum

#10, start