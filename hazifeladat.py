
#0. Írj egy Python programot, amely bekér egy 20-nál nem nagyobb pozitív egész számot a felhasználótól és kiírja a képernyőre a START szót úgy, hogy előtte annyi szóköz legyen amennyi a megadott szám értéke! 
def feladat0():
    szam=int(input("Kérek egy 20-nál nem nagyobb számot: "))
    szokoz=" "

    print(f"{szokoz*szam} START")
feladat0()

#1. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a képernyőre azt a számot, amely az ennél a számnál nem nagyobb pozitív egész számok összege!
def feladat1():
    egeszSzam=int(input("Kérek egy pozitív egész számot: "))
    osszeg=0

    while(egeszSzam>=0):
        osszeg=osszeg+egeszSzam
        egeszSzam=egeszSzam-1
    print(osszeg)
feladat1()

#2. Írj egy Python programot, amely bekér egy szót (sztringet) a felhasználótól és kiírja a képernyőre a szó betűit, úgy, hogy minden betű egy új sorba kerüljön! 
def feladat2():
    szo=input("Kérek egy szót: ")
    for i in str(szo):
        print(i)
feladat2()

#3. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a képernyőre felváltva a 0 és 1 számjegyeket úgy, hogy a számjegyek együttes darabszáma pontosan a megadott szám legyen!
def feladat3():
    Szam=int(input("Kérek egy pozitív egész számot: "))
    for i in range(Szam):
        if i%2==0:
            print("0")
        else:
            print("1")
feladat3()

#4. Írj egy Python programot, amely először bekér egy kisebb majd egy nagyobb pozitív valós számot a felhasználótól és kiírja a képernyőre azokat az egész számokat, amelyek a megadott értékek között helyezkednek el! 

#5. Írj egy Python eljárást, amely paraméterként kap 2 egész számot (N és M) és kiír a képernyőre a csillag (*) karaktereket M darab sorban és N darab oszlopban (tehát NxM darab karaktert egy téglalap alakú képernyőrészre)! A programodban hívd is meg ezt az alprogramot!