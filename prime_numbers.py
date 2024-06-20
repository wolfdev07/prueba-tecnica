"""
Dada la siguiente lista de numeros, implementar funcion que imprima solo los números primos.
"""

numbers_list = [4, 23, 24, 35, 37, 64, 74, 92, 103, 144, 177,
                182, 194, 207, 214, 273, 316, 317, 348, 392, 395,
                401, 435, 443, 455, 501, 507, 545, 589, 611, 624,
                641, 649, 673, 698, 733, 735, 786, 796, 809, 860,
                934, 939, 944, 946, 958, 979, 980, 994, 996]

def list_prime_numbers(numbers_list):
    
    for number in numbers_list:
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                print(number)

list_prime_numbers(numbers_list)