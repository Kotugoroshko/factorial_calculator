def factorial(n):
    suma = 1
    while n>1:
        suma*=n 
        n-=1
    return suma

number = int(input("Введіть факторіал числа"))
result = factorial(number)
print(f"Факторіал числа {number} дорівнює {result}")