print("=================== DESAFIO 8 ===================")

print("================ Conversor de Metros ================")

m = float(input("digite o valor em metros que deseja ser convertido: "))
km = m / 1000
hm = m / 100
dm = m / 10
dc = m * 10
cm = m * 100
mm = m * 1000

print("{}m convertidos para Kilometro é {}km, \nPara Hectometro é {}hm, \nPara Decametro é {}dm,".format(m, km, hm, dm))
print("{}m convertidos para Decimetros são {:.0f}dc, \nPara Centimetros são {:.0f}cm \nE para Milimetros são {:.0f}mm.".format(m, dc, cm, mm))
