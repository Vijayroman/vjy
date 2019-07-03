import math
sham=int(input())
sim=math.log10(sham)/math.log10(2)
if math.ceil(sim)==math.floor(sim):
    print(0)
else:
    sag=(sham-1)//2
    sem=sg*2
    print(sham-sem)
