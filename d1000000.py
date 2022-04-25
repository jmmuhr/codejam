def straight_dice(T,N,array):
    straight=0
    count=1
    for num in sorted(array):
        if num >= count:
            count+=1
            straight+=1
    print("Case #{}: {}".format(T,straight))

T=int(input())
N=[]
array=[]
for i in range(0,T):
    N.append(int(input()))
    array.append(int(item) for item in input().split())
for i in range(0,T):
    straight_dice(i+1,N[i],array[i])
