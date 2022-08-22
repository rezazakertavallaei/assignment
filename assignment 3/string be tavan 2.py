

import random 

adad_random=0

aadad = []
adad_tavan2=[]
while True:
    adad_random = random.randint(1 , 100)
    aadad.append(adad_random)

    if len(aadad) == 20:
        break

print("aadad pish farz: " , aadad)

for i in aadad:
    adad_tavan2.append(i**2)
print("aadad tavan 2 : ", adad_tavan2)