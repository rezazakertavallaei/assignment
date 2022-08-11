# soccor tabale 


from tracemalloc import start
from turtle import goto


m=0
A=R=S=K=F=0
Wf=Df=Lf=0
Wk=Dk=Lk=0
Ws=Ds=Ls=0
Wa=Da=La=0
Wr=Dr=Lr=0
ga=gr=gs=gk=gf=0

while m<10:
  
  m+=1
  print("team haye sherkat konndeh: rezvan' azad' sajjad' khavaran' ferdowsi ")

  x=(input("nam team aval ra vared konid:  "))
  y=(input("nam team dovom ra vared konid;  "))

  g1=int(input("tedad gol zadeh aval   "))
  g2=int(input("tedad gol zadeh dovom  "))
  if(g1>=0 and g2>=0):
    if(x=="azad" ):   

      if(x=="azad" and y=="rezvan"):
          if(g1>g2):
            A+=3 ; Wa+=1 ; Lr+=1
          elif(g1==g2):
            A+=1 ; R+=1  ; Da+=1 ; Dr+=1
          else:
            R+=3 ; Wr+=1 ; La+=1
        
          ga+=1  ; gr+=1
      elif(x=="azad" and y=="sajjad"):
          if(g1>g2):
            A+=3 ; Wa+=1 ; Ls+=1
          elif(g1==g2):
            A+=1 ; S+=1 ; Da+=1 ; Ds+=1
          else:

            S+=3 ; Ws+=1 ; La+=1

          ga+=1 ; gs+=1
      elif(x=="azad" and y=="khavaran"):
        if(g1>g2):
            A+=3 ; Wa+=1 ; Lk+=1
        elif(g1==g2):
            A+=1 ; K+=1  ; Da+=1 ; Dk+=1
        else:
            K+=3 ; Wk+=1 ; La+=1

        ga+=1 ; gk+=1
      elif(x=="azad" and y=="ferdowsi"):
        if(g1>g2):
            A+=3 ; Wa+=1 ; Lf+=1
        elif(g1==g2):
            A+=1 ; F+=1  ; Da+=1 ; Df+=1
        else:
            F+=3 ; Wf+=1 ; La+=1

        ga+=1 ; gf+=1
    elif(x=="rezvan"):
      if(x=="rezvan" and y=="azad"):
          if(g1>g2):
            R+=3 ; Wr+=1 ; La+=1
          elif(g1==g2):
            R+=1 ; A+=1  ; Dr+=1 ; Da+=1
          else:
            A+=3 ; Wa+=1 ; Lr+=1

          ga+=1 ; gr+=1
      elif(x=="rezvan" and y=="sajjad"):
          if(g1>g2):
            R+=3 ; Wr+=1 ; Ls+=1
          elif(g1==g2):
            R+=1 ; S+=1 ; Dr+=1 ; Ds+=1
          else:
            S+=3 ; Ws+=1 ; Lr+=1

          gr+=1 ; gs+=1
      elif(x=="rezvan" and y=="khavaran"):
        if(g1>g2):
            R+=3 ; Wr+=1 ; Lk+=1
        elif(g1==g2):
            R+=1 ; K+=1  ; Dr+=1 ; Dk+=1
        else:
            K+=3 ; Wk+=1 ; Lr+=1

        gr+=1 ; gk+=1
      elif(x=="rezvan" and y=="ferdowsi"):
        if(g1>g2):
            R+=3 ; Wr+=1 ; Lf+=1
        elif(g1==g2):
            A+=1 ; F+=1  ; Dr+=1 ; Df+=1
        else:
            F+=3 ; Wf+=1 ; Lr+=1
        gr+=1 ; gf+=1  
    elif(x=="sajjad"):
      if(x=="sajjad" and y=="azad"):
          if(g1>g2):
            S+=3 ; Ws+=1 ; La+=1
          elif(g1==g2):
            S+=1 ; A+=1  ; Ds+=1 ; Da+=1
          else:
            A+=3 ; Wa+=1 ; Ls+=1
          gs+=1 ; ga+=1
      elif(x=="sajjad" and y=="rezvan"):
          if(g1>g2):
            S+=3 ; Ws+=1 ; Lr+=1
          elif(g1==g2):
            R+=1 ; S+=1 ; Dr+=1 ; Ds+=1
          else:
            R+=3 ; Wr+=1 ; Ls+=1

          gs+=1 ; gr+=1
      elif(x=="sajjad" and y=="khavaran"):
        if(g1>g2):
            S+=3 ; Ws+=1 ; Lk+=1
        elif(g1==g2):
            S+=1 ; K+=1  ; Ds+=1 ; Dk+=1
        else:
            K+=3 ; Wk+=1 ; Ls+=1

        gs+=1 ; gk+=1
      elif(x=="sajjad" and y=="ferdowsi"):
        if(g1>g2):
            S+=3 ; Ws+=1 ; Lf+=1
        elif(g1==g2):
            S+=1 ; F+=1  ; Ds+=1 ; Df+=1
        else:
            F+=3 ; Wf+=1 ; Ls+=1

        gs+=1 ; gf+=1
    elif(x=="khavaran"):
      if(x=="khavaran" and y=="azad"):
          if(g1>g2):
            K+=3 ; Wk+=1 ; La+=1
          elif(g1==g2):
              K+=1 ; A+=1  ; Dk+=1 ; Da+=1
          else:
            A+=3 ; Wa+=1 ; Lk+=1

          gk+=1 ; ga+=1
      elif(x=="khavaran" and y=="rezvan"):
          if(g1>g2):
            K+=3 ; Wk+=1 ; Lr+=1
          elif(g1==g2):
            K+=1 ; R+=1 ; Dr+=1 ; Dk+=1
          else:
            R+=3 ; Wr+=1 ; Lk+=1

          gk+=1; gr+=1
      elif(x=="khavaran" and y=="sajjad"):
        if(g1>g2):
            K+=3 ; Wk+=1 ; Ls+=1
        elif(g1==g2):
            S+=1 ; K+=1  ; Ds+=1 ; Dk+=1
        else:
            S+=3 ; Ws+=1 ; Lk+=1

        gk+=1 ;gs+=1
      elif(x=="khavaran" and y=="ferdowsi"):
        if(g1>g2):
            K+=3 ; Wk+=1 ; Lf+=1
        elif(g1==g2):
            K+=1 ; F+=1  ; Dk+=1 ; Df+=1
        else:
            F+=3 ; Wf+=1 ; Lk+=1

        gk+=1 ; gf+=1
    elif(x=="ferdowsi"):
      if(x=="ferdowsi" and y=="azad"):
          if(g1>g2):
            F+=3 ; Wf+=1 ; La+=1
          elif(g1==g2):
            F+=1 ; A+=1  ; Df+=1 ; Da+=1
          else:
            A+=3 ; Wa+=1 ; Lf+=1
             
          gf+=1 ; ga+=1
      elif(x=="ferdowsi" and y=="rezvan"):
          if(g1>g2):
            F+=3 ; Wf+=1 ; Lr+=1
          elif(g1==g2):
            F+=1 ; R+=1 ; Dr+=1 ; Df+=1
          else:
            R+=3 ; Wr+=1 ; Lf+=1

          gf+=1 ; gr+=1
      elif(x=="ferdowsi" and y=="sajjad"):
          if(g1>g2):
              F+=3 ; Wf+=1 ; Ls+=1
          elif(g1==g2):
              S+=1 ; F+=1  ; Ds+=1 ; Df+=1
          else:
              S+=3 ; Ws+=1 ; Lf+=1

          gf+=1 ; gs+=1
      elif(x=="ferdowsi" and y=="khavaran"):
        if(g1>g2):
            F+=3 ; Wf+=1 ; Lk+=1
        elif(g1==g2):
            K+=1 ; F+=1  ; Dk+=1 ; Df+=1
        else:
            K+=3 ; Wk+=1 ; Lf+=1 

        gf+=1 ; gk+=1
    else:
      m-=1
      print("team vared shode sahih nemibashad") 
  else:
    print("adad gol eshtebah ast")  
    m-=1
print("team  ","emteyaz ","bord ",'bakht ',"mosavi ","tedad-bazi")
print("rezvan ",    R    ,   Wr  ,    Lr  ,   Dr      ,     gr   )
print("ferdowsi ",    F    ,   Wf  ,    Lf  ,   Df    ,      gf  )
print("khavaran  ",    K    ,   Wk  ,    Lk  ,   Dk   ,     gk   )
print("sajjad ",    S    ,   Ws  ,     Ls  ,    Ds    ,     gs   )
print("azad ",    A     ,    Wa   ,     La  ,   Da     ,    ga   )

