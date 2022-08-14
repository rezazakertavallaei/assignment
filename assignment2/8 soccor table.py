

n=0
res=0
L=0
D=0
W=0
while n<8:
 
    print("natije bazi" ,n+1, "ra vared konid. " 
    "\nbord : w  bakht : l  mosavi : d ")
    x=input()
    if x=="w":
        res+=3
        W+=1
    elif x=="d":
        res+=1
        D+=1
    elif x=="l":
        res+=0
        L+=1
    else:
        n-=1
        print("dobareh")
    n+=1
print("natije dr 8 bazi anjam shode : ",W,"bord",D,"mosavi", "va", L,"bakht"
   "\nemtiaz nahaii : ",res )

