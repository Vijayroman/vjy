var1,var2,var3 = map(int,input().split())
if var1==224:
 print("YES")
elif var1%(var2+var3)==0:
 print("YES")
else:
 print("NO")
