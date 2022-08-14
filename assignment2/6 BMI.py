
x=float(input("vazn(kg) ra vared konid : "))
y=float(input("qad(metr) ra vared konid : "))
BMI= (x/(y*y))
if(14<BMI<40):
    if(BMI<16):
        sug=("shoma laghari mofrat  drid lotfan b pezeshk morajeeh konid")
    elif(16<=BMI<18.5):
        sug=("shoma laghar hastid ba rezhim v taghzieh mnaseb mitavanid b tanasob andam brsid")
    elif(18.5<BMI<24.9):
        sug=("shoma dar vazn standard hastid ba rezhim v taghzieh mnaseb khod edameh dahid")
    elif(25<BMI<29.9):
        sug=("shoma ezafeh vazn darid ba rezhim v taghzieh mnaseb dar kenar varzesh mitvanid be vazn standard brsid ")
    elif(30<BMI<34.9):
        sug=("shoma chagh hastid dar sorat adam raayat rezhim  v taghzieh emkan ebtela b bimari haye ghalbi vjod dard")
    elif(BMI>35):
        sug=("shoma chaghi mofrat  drid lotfan b pezeshk morajeeh konid")
    print("shakhes tudeh badani shoma=",BMI)
    print("pishnahad:",sug)
else:
    print("vazn ya qad vared shodeh eshtebah ast!!!!!")
