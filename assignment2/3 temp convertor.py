

#tempretur convertion





while True:
 
      X=input("meghyas 1 ra vared konid : ")
      Y=input("meghyas 2 ra vared konid : ")
      t=float(input("dama ra  bar hasb meghyas 1 vared konid : "))

      if((X=="K" or X=="F" or X=="C")and(Y=="C" or Y=="F" or Y=="K")):

         if(X=="F"and Y=="C"):
           res=((t-32) * 5/9 )

         elif(X=="F" and Y=="K"):
           res=((t-32) * 5/9 )+ 273.15
  
         elif(X=="K" and Y=="C"):
           res=(t-273.15 )
  
         elif(X=='K' and Y=="F"):
            res=((t -273.15) * 9/5) + 32 
  
         elif(X=="C" and Y=="K"):
            res=(t+273.15 )

         elif(X=="C" and Y=='F'):
             res=(t*9/5) + 32 
  
         print(t,"darajeh",X,"=",res,"darajeh",Y)
 
      else:
        print("meghyas vared shode sahih nist")
 


