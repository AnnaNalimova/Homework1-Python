6.# Написать программу для определения счастливости билета
# Сумма первых трех цифр должна равняться сумме последних трех цифр
b=input("Введите шестизначное число:")

if int(b[0]) + int(b[1]) + int(b[2]) == int(b[3]) + int(b[4]) + int(b[5]):
    print("Билетик счастливый")
else:
    print("Вам не повезло")