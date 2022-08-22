

s=0
m=0
h=0

while True:
    x=input("meghyas mored nazar ra vared konid( h ya s) ")
    if x=="s":
        t=int(input("zaman ra bar hasb sanieh vared konid "))
        s=t%60
        h=t//3600
        m=t//60-h*60
        print("time: ",h,"saat",m,"daghigheh",s,"sanieh ")
        continue
    elif x=="h":
        h=int(input("saat ravard konid "))
        m=int(input("min ra vared konid "))
        s=int(input("sanieh ra vared konid "))
        time=(h*60*60)+(m*60)+(s)
        print("zaman  bar hasb sanine :",time)
        continue
