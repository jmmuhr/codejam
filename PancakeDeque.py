T=int(input())
arrayN=[]
arrayD=[]
for i in range(T):
    N=int(input())
    arrayN.append(N)
    x = input().split(' ')
    x = list(map(int,x))
    arrayD.append(x)
i=0
for array in arrayD:
    i+=1
    arrayAux=array.copy()
    arrayOrd=[]
    while len(arrayAux)>0:
        if arrayAux[0]<=arrayAux[-1]:
            arrayOrd.append(arrayAux[0])
            arrayAux.pop(0)
        else:
            arrayOrd.append(arrayAux[-1])
            arrayAux.pop(-1)
    pivote=arrayOrd[0]
    counter=0
    for k in range(0,len(arrayOrd)):
        if arrayOrd[k]>=pivote:
            counter+=1
            pivote=arrayOrd[k]
    print("Case #{}: {}".format(i,counter))
