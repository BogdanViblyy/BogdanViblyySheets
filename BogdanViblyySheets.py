from random import *
nimed=["Mati","Meelis","Kati","Mati"]
while True:
    print("********")
    v=input("N-näita andmed\nL-lisada andmeid\nK-andmete kustutamine\nH-andmete haldus\nI-Positsiooni ootsing\n")
    
    
    if v=="N":
        v=input("Kas juhuslik(j) nimi või terve loetelu(t)?")
        if v=="t":
            print(nimed)
        elif v=="j":
            print(choice(nimed))
    elif v=="L":
        v=input("Kas nimekirja lõppu(l) või positsioonile(p)")
        if v=="l":
            nimi=input("Sisesta nimi: ")
            nimed.append(nimi)
        elif v=="p":
            nimi=input("Sisesta nimi: ")
            ind=int(input("Mille kohale: "))
            nimed.insert(ind-1,nimi)
    elif v=="K":
        v=input("Kas nimi järgi(n) või indeksi järgi(i) või kõke(k)")
        if v=="i":
            ind=int(input("Sisesta indeks: "))
            nimed.pop(ind-1)
        elif v=="k":
            nimed.clear()
        elif v=="n":
            nimi=input("Sisesta nimi: ")
            mitu=nimed.count(nimi)
            if mitu>0:
                v=input("Kas tahad kustutada kõik {nimi}\k või mingi konkreetne?\ind")
                if v=="k":
                    while nimed.count(nimi)>0:
                        nimed.remove(nimi)
                elif v=="ind":
                    ind=0
                    indlist=[]
                    sob=0
                    for e in nimed:
                        ind +=1
                        indlist.append(ind - 1)
                    print(indlist)
                    v=int(input("Mis indeks?"))
                    nimed.pop(v)
                else:
                    nimed.remove(nimi)
            
            
            
            
            else:
                print(f"{nimi} ei ole loetelus")
    elif v=="H":
        v=input("Sorteerimine(s), kopeerimine(k) või ümber pööramine(p)")
        if v=="s":
            v=int(input("A-z?(1) või Z-a?(2)")) 
            if v==1:
                nimed.sort()
            elif v==2:
                nimed.sort(reverse=True)
            
            nimed.sort()
        elif v=="k":
            nimed.copy()
        elif v=="p":
            nimed.reverse()
    elif v=="I":
            nimi=input("millest nimest sa tahad teada?")
            x=nimed.count(nimi)
            print("{nimi} on {x} tükki tabelis")
             
