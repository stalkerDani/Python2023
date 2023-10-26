Lottók=["ötös lottó", "Hatos lottó", "Skandináv lottó" , "totó"]
import random

repeat="igen"
while(repeat=="igen"):

    for i,elem in enumerate(Lottók):
        print("\t"+str(i+1)+":",elem)

    típusId="alma"
    while típusId=="alma" or típusId not in range(len(Lottók)+1):
        try:
            típusId=int(input("Válassz "))
            if típusId not in range(len(típusok)+1):
               raise 
        except:
            print("")


    típusId-=1
    print("típus:" , Lottók[típusId])
    print("")
    print("Nyerő számok")

    for i in range (5):
        print(random.randrange(1, 50))

    repeat=input("újra? (igen/nem):")

    for i,elem in enumerate(Lottók):
        print("\t"+str(i+1)+":",elem)

    típusId="alma"
    while típusId=="alma" or típusId not in range(len(Lottók)+1):
        try:
            típusId=int(input("Válassz "))
            if típusId not in range(len(típusok)+1):
               raise 
        except:
            print("")


    típusId-=1
    print("típus:" , Lottók[típusId])
    print("")
    print("Nyerő számok")

    for i in range (6):
        print(random.randrange(1, 46))

    repeat=input("újra? (igen/nem):")

    for i,elem in enumerate(Lottók):
        print("\t"+str(i+1)+":",elem)

    típusId="alma"
    while típusId=="alma" or típusId not in range(len(Lottók)+1):
        try:
            típusId=int(input("Válassz "))
            if típusId not in range(len(típusok)+1):
               raise 
        except:
            print("")


    típusId-=1
    print("típus:" , Lottók[típusId])
    print("")
    print("Nyerő számok")

    for i in range (7):
        print(random.randrange(1, 36))


    repeat=input("újra? (igen/nem):")

