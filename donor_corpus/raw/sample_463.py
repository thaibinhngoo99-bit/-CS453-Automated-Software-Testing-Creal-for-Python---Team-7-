sys.stdout = open("6-num.txt", "w")
data = "1234567890"
for a in data:
	for b in data:
		for c in data:
			for d in data:
				for e in data:
					for f in data:
 						print(a+b+c+d+e+f)
sys.stdout.close()
