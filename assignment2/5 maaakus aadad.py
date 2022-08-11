




while True:
  
  res=0
  y=x=int(input("adad ra vraed konid :    "))
  if(x>0):
   while ((x%10)!=0):

     n=(x%10)
     res=(res*10)+n
     x=(x//10)
   print(y)
   print(res)
   if(res==y):
        print("adad ba maakus khudash barabar ast ")
   else:
            print("adad ba maakus khudash barabar nist ")
  else:
    print("adad vared shode mnfi ast")


 