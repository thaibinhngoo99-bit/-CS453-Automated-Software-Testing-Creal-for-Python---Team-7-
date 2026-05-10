T = float(input("Entre com a temperatura que está agora: "))

if T >= 26.0 and T <= 36.0:
	print("A temperatura está boa")
elif T > 36.0:	
	print("A temperatura está quente\n Tome bastante líquido")
elif T >= 15.0 and T < 26.0:
	print("A temperatura está agradável")
else:
	print("A temperatura esta fria")
