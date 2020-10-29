import random
list1 = list()
n = int(input("Введите длину списка: "))
for i in range(n):
   list1.append(random.randint(-60, 60))
print(list1)

minElem = min(list1)
maxElem = max(list1)
print('Минимальное число: ', minElem)
ln = len(list1)
for i in range(len(list1)):
   a = int(list1[i])
   if list1.index(minElem) < list1.index(a) and a > 0 and list1.index(a)%2==0:
      list1.remove(a)
      list1.insert(i, ' ')
while ' ' in list1:
   list1.remove(' ')

print(list1)
