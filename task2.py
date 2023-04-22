# 1.Найдите сумму цифр трехзначного числа
number = int(input("ВВедите трехзначное число :"))
smm = 0
number2 = str(number)
if (number < 100) and (number > 999):
    print("Число не трехзначное")
elif (number >= 100) and (number <= 999):
    while number > 0:
        smm += number%10
        number = number//10
    print(f'{number2}->{smm}({number2[0]}+{number2[1]}+{number2[2]})')