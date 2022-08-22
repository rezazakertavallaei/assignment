
from itertools import count
import random
c=0
x=100
a=0
x

print("adad mored nazar ra dar bazeh 0-100 b khater bsparid v enter ra bzind")

while True:
     
    adad=random.randint(a,x)
    print("AYA",adad,"adad mored nzr shomast?")
    y=int(input("1: adad bozorgtar ast \n"
    " 2 adad dorost ast \n"
    " 3 adad kuchek tar ast \n"))
    c+=1
    if y==1:
        a= adad
        continue
    elif y==2:
        break
    elif y==3:
        x=adad
        continue
    else:
        print("adad dorost ra az menu entekhab konid")
        a=0
        x=100
        continue
print("hooora adad mored naz shoma :", adad ,"ba",c ,"hads anjam shodeh")
