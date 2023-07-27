text=input("Введите тескт:")
first_sym=input("Введите первую букву:")
second_sym=input("Введите вторую букву:")
firstSymCount=0
secondSymCount=0

for symbol in text:
  if symbol==first_sym:
    firstSymCount+=1
  if symbol==second_sym:
    secondSymCount+=1

print("Кол-во букв",first_sym,"=",firstSymCount)
print("Кол-во букв",second_sym,"=",secondSymCount)

