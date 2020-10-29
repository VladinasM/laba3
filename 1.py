#1a
phrase = input("Введите фразу и поставьте точку: ")
if phrase[-1:] != "." :
   print('Введите точку в конце')
   phrase = input('Введите фразу и поставьте точку: ')
else:
   print('Длина строки: ', len(phrase))

#1b
list1 = [phrase]
for i in list1:
   print("Кол-во слов в строке: ", len(i.split()))

#1в
L = phrase.split()
print(len(min(L, key=len)), "and", len(max(L, key=len)))
   
#1д
ph2 = phrase.replace("*", "")
doubleph2 = ""
for i in range(len(ph2)):
   doubleph2 += ph2[i] * 2
print("Удвоенные буквы без *", doubleph2)
