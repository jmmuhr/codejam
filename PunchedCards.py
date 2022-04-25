def punched_ASCII(array):
    matriz=[]
    for i in range(1,len(array)):
        print(f"Case #{i}")
        for j in range(0,(2*array[i][0])+1):
            linea=[]
            for k in range(0,(2*array[i][1])+1):
                if ((j in [0,1]) and (k in [0,1])):
                    linea.append(".")
                else:
                    if j%2==0:
                        linea.append("+") if k%2==0 else linea.append("-") 
                    else:
                        linea.append("|") if k%2==0 else linea.append(".")
            matriz.append(linea)
        for j in range(0,(2*array[i][0])+1):
            for k in range(0,(2*array[i][1])+1):
                print(matriz[j][k],end=" ")
            print()

T=int(input("Test Cases: "))
array=[T]
for i in range(0,T):
    aux = list(map(int,input("Enter the numbers : ").strip().split()))[:2]
    array.append(aux)
punched_ASCII(array)
