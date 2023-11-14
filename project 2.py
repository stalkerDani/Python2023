def menu(lista):
    for i,szoveg in enumerate(lista):
        print("{}: {}".format(i+1,szoveg))

    valasz=-1
    while (valasz<1 or valasz>len(lista)) and valasz!=999:
        try:
            valasz=int(input("Válasz: "))
        except:
            pass
        
    return valasz-1


    
#lista=["előre", "hátra", "jobbra", "balra"]

#valasztott=menu(lista)
#print(valasztott,lista[valasztott])

#valasztott=menu(lista)
#print(valasztott,lista[valasztott])


tortenet=[
    [
        1,
        "Reggel felkeltél,",
        ["fogmosás", "öltözés", "reggeli"],
        [2,3,4]
    ],
    [
        2,
        "megmostad a fogad,",
        ["öltözés és reggeli","munkába indulás","Vissza alvás"],
        [5,6,7]
    ],
    [
        3,
        "felöltöztél, de nem volt időd fogatmosni",
        ["vissza az elsőre"],
        [1]
    ],
    [
        4,
        "Elkéstél a munkából és kiletél rugva",
        ["vissza az elsőre"],
        [1]
    ],
    [
        5,
        "felöltöztél és lementél reggelizni",
        ["munkába indulás","bolt","kimész a városba"],
        [8,9,10]
    ],
    [
        6,
        "éhesen és ruha nélkül indultál munkába",
        ["Vissza"],
sssss        [2]
    ],
    [
        7,
        "vissza aludtál, emiatt kirúgot a főnököd",
        ["vissza"],
        [2]
    ],
    [
        8,
        "elindultál munkába",
        ["elindultál munkába és élted tovább az unalmas egy hangu életed"],
        [11]
    ],
    [
        9,
        "elmentél boltba és elütött egy autó",
        ["meghaltál"],
        [5]
    ],
    [
        10,
        "kimentél a városba és találtál egy jobb munka lehetőséget",
        ["találtál egy rugalmas munka idejü izgalmasabb munkát és az életed gyökerestül meg változott"],
        [12]
    ],
    [
        11,
        "",
        [],
        []
    ],
    [
        12,
        "",
        [],
        []
    ],    
]
szalId=1
while True:
    templista=[]
    for elem in tortenet:
        templista.append(elem[0])

    keresettIndex=templista.index(szalId)    

    print("\n"+"_"*50)
    print(tortenet[keresettIndex][1])

    if len(tortenet[keresettIndex][2])==0:
        break
    valasztott=menu(tortenet[keresettIndex][2])

    if szalId==999:
        break
    
    szalId=tortenet[keresettIndex][3][valasztott]

print("Vége")


    
