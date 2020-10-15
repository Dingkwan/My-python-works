def Fah_to_Cel(Fah):
    return (Fah-32)*5/9

input_Fah=int(input('输入华氏温度：'))
print("对应的摄氏温度是：",Fah_to_Cel(input_Fah))