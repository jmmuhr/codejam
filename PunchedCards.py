def punched_ASCII(array):
    for i in range(1,len(array)):
        matriz=[]
        print("Case #{}:".format(i))
        for j in range(0,(2*array[i][0])+1):
            linea=''
            for k in range(0,(2*array[i][1])+1):
                if ((j in [0,1]) and (k in [0,1])):
                    linea+='.'
                else:
                    if j%2==0:
                        if k%2==0:
                            linea+='+'
                        else:
                            linea+='-' 
                    else:
                        if k%2==0:
                            linea+='|'
                        else:
                            linea+='.'
            matriz.append(linea)
        for k in range(0,(2*array[i][0])+1):
            print(matriz[k],end=" ")
            print()
                    
T=int(input())
array=[T]
for i in range(0,T):
    x = input().split(' ')
    x = list(map(int,x))
    array.append(x)
punched_ASCII(array)
