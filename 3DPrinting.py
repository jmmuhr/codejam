T=int(input())
array=[]
for i in range(0,3*T):
    x = input().split(' ')
    x = list(map(int,x))
    array.append(x)

for k in range(T):
    l1=array[3*k]
    l2=array[3*k+1]
    l3=array[3*k+2]
    minimos=[]
    for i in range(0,4):
        minimos.append(min(l1[i],l2[i],l3[i]))
    suma=0
    for num in minimos:
        suma+=num
    if suma < 1000000:
        minimos=[]
    elif suma == 1000000:
        minimos=minimos
    else:
        residuo=suma-1000000
        while residuo>0:
            if minimos[0]<residuo:
                residuo=residuo-minimos[0]
                minimos[0]=0
            else:
                minimos[0]=minimos[0]-residuo
                residuo=0
            if minimos[1]<residuo:
                residuo=residuo-minimos[1]
                minimos[1]=0
            else:
                minimos[1]=minimos[1]-residuo
                residuo=0
            if minimos[2]<residuo:
                residuo=residuo-minimos[2]
                minimos[2]=0
            else:
                minimos[2]=minimos[2]-residuo
                residuo=0
            if minimos[3]<residuo:
                minimos[3]=0
                residuo=residuo-minimos[3]
            else:
                minimos[3]=minimos[3]-residuo
                residuo=0
    if minimos==[]:
        print("Case #{}: {}".format(k+1,'IMPOSSIBLE'))
    else:
        print("Case #{}: {} {} {} {}".format(k+1,minimos[0],minimos[1],minimos[2],minimos[3]))
