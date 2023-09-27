import math
chislo = 0
while chislo <11:
    print("что вы хотите сделать")
    print("1 сложение")
    print("2 вычитание")
    print("3 умножение")
    print("4 деление")
    print("5 возведение в степень")
    print("6 квадратный корень")
    print("7 факториал")
    print("8 синус")
    print("9 косинус")
    print("10 тангенс")
    print("11 выйти из программы")
    chislo = int(input())
    if chislo == 1:
        print("Впишите певое число")
        a = int(input())
        print("Впишите второе число")
        b = int(input())
        c = a+b
        print(c)
    if chislo == 2:
        print("Впишите певое число")
        a = int(input())
        print("Впишите второе число")
        b = int(input())
        c = a-b
        print(c)
    if chislo == 3:
        print("Впишите певое число")
        a = int(input())
        print("Впишите второе число")
        b = int(input())
        if b==0:
            print("На ноль делить нельзя")
        else:
            c = a*b
            print(c)
    if chislo == 4:
        print("Впишите певое число")
        a = int(input())
        print("Впишите второе число")
        b = int(input())
        c = a/b
        print(c)
    if chislo == 5:
        print("Впишите число")
        a = int(input())
        print("Впишите степень")
        b = int(input())
        c = a **b
        print(c)
    if chislo == 6:
        print("Впишите число")
        a = int(input())
        c= a ** (1/2)
        print(c)
    if chislo == 7:
        print("Впишите число")
        a = int(input())
        c = a
        for i in range(1,a):
            c = c * i
        print(c)
    if chislo == 8:
        print("Впишите число")
        a = int(input())
        c= math.sin(a)
        print(c)
    if chislo == 9:
        print("Впишите число")
        a = int(input())
        c= math.cos(a)
        print(c)
    if chislo == 10:
        print("Впишите число")
        a = int(input())
        c= math.tan(a)
        print(c)
print("калькулятор закончил работу")
