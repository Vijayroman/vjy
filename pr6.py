ram=int(input())
sam=list(map(int,input().split()))
cnc=0
for i in range(len(sam)-2):
    for x in range(i+1,len(sam)-1):
         for j in range(x+1,len(sam)):
            if sam[i]<sam[x]<sam[j] and i<x<j:
                cnc+=1
print(cnc)    
