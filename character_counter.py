"""
Escribe una función que tome un caracter, y una string, y devuelva el número de veces que 
el caracter aparece en la string.
"""

def character_counter(character, string):

    if type(character) != str or type(string) != str:
        return "Invalid input"
    
    count = 0
    string = string.lower()
    character = character.lower()
    
    for char in string:
        if char == character:
            count += 1
    return count

input_character = input("Enter a character: ")
input_string = input("Enter a string: ")
print(character_counter(input_character, input_string))