adatok=[] 

f=open("autok.txt")
for sor in f:
 
    tempSor=sor.strip().split(" ")
 
    tempSor[0]=int(tempSor[0])
    tempSor[3]=int(tempSor[3])
    tempSor[4]=int(tempSor[4])
    tempSor[5]=int(tempSor[5])

    tempIdő=tempSor[1].split(":")

    tempIdő[0]=int(tempIdő[0])
    tempIdő[1]=int(tempIdő[1])


    adatok.append(tempSor[0])
 
f.close()

print(adatok)