


while True:
    zog=0
    fard=0
    x=int(input("adad mored nazar ra vared konid:    "))

    while (x%10)!=0 :
        n =(x%10)
        if ((n%2)==0)or (n==0):
          zog+=1
        else:
          fard+=1
        
        x=x//10
    
    print( "tedad adad fard: ", fard ,'tedad adad zog :',zog )

    if(fard>zog):
      print("tedad adadfard bishtar ast")
    else:
      print("tedad adad zohg bishtar ast")