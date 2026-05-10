def num(a):
  num = int(a)
  if (num < 10):
    return (num + num)
  elif (num <100):
    return (num + num //10 + num % 10)
  elif (num <1000):
    return (num + num //100 + ( (num //10) % 10) + num % 10)
  else:
    return (num + num //1000 + ((num //100) % 10) + ((num //10) % 10) + num %10)

count = list(range(10000))

for i in range (10000):
  temp = num(i)
  if (temp >= 10000):
    continue
  else:
    count[temp] = -1

for i in range (10000):
  if (count[i] != -1):
    print (i)

