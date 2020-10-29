import random
a = list()
for i in range(16):
   a.append(random.randint(-60, 60))
print(a)
x = 0
y = 0
xmax = 0
ymax = 0
for i, Aind in enumerate(a):
   if Aind < 0:
      ymax += 1
      if i > 0 and a[i - 1] >= 0:
         y = i
      
      if ymax > xmax:
         x = y
         xmax = ymax
   else:
      ymax = 0
a = a[:x] + a[x + xmax:] + a[x:x+xmax]
print(a)
