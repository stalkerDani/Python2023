Lottók=["ötös lottó", "Hatos lottó", "Skandináv lottó" , "totó"]

for i,elem in enumerate(Lottók):
    print("\t"+str(i+1)+":",elem)

print("\t0: Kilépés")

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
print("Forrás")

for i,elem in enumerate(egysegek[típusId]):
    print("\t"+str(i+1)+":",elem)
print("\t0: Vissza")
egysegId="alma"
while egysegId=="alma" or egysegId not in range(len(egysegek[típusId])+1):
    try:
        egysegId=int(input("Válassz "))
        if egysegId not in range(len(egysegek[típusId])+1):
           raise 
    except:
        print("válassz a listából")
print("Cél")
for i,elem in enumerate(egysegek[típusId]):
    print("\t"+str(i+1)+":",elem)
print("\t0: Vissza")
