"""
Dado un numero entero n, genera una lista de n elementos en 1 y regresa una lista de strings,
donde los elementos son:

FizzBuzz si el numero es divisible de 3 y 5
Fizz si el numero es divisible de 3
Buzz si el numero es divisible de 5
El numero si no es multiplo de 3 ni de 5

"""

def fizz_buzz_list(n):
    return [fizz_buzz(i) for i in range(1, n+1)]

def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

number_ = int(input("Enter a number: "))
print(fizz_buzz_list(number_))