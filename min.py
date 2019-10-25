n=int(input())
x=[int(x) for x in input().split()]
if n==len(x):
    for i in range(n):
        j=i+1
        for j in range(n):
            if x[i]<x[j]:
                temp=x[i]
                x[i]=x[j]
                x[j]=temp
    print(x[0])
