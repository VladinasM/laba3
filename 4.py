n = int(input("Введите число n >= 2: "))
while n < 2:
   print('Введите  число большее или  равное двум')
   n = int(input("Введите число n >= 2: "))

a = list()
for i in range(n + 1):
   a.append(i)

for i in range(2, n + 1):
   if a[i] != 0:
      p = i
      for j in range(2*p, n + 1, p):
            a[j] = 0

print("Кратные 7 на промежутке от 1 до n: ")
for i in range(7, n + 1, 7):
   print(i, end = " ")
print()
print("Простые на промежутке от 2 до n: ")
for i in range(2, n + 1):
   if a[i] != 0:
      print(a[i], end = ' ')
     
