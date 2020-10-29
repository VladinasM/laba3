import random
n = int(input("Введите n: ")) # stroki
m = int(input("Введите m: ")) # stolbiki


a = [[0] * m for i in range(n)]
x = 0
y = 0
Max = a[0][0]
for i in range(n):
      for j in range(m):
            a[i][j] = random.randint(-30, 30)
            print(a[i][j], end=" ")
            if (i + j)%2!=0 and a[i][j] > Max:
                  Max = a[i][j] 
                  x = i
                  y = j  
      print()      
print("Максимальный элемент: ", Max)
print(x, y)
