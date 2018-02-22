
texto_usuario = input("Dime una frase: ")

espacio = " "

n_espacios = 0

for letra in texto_usuario:
    if letra in espacio:
        n_espacios += 1

print("Los espacios son {}".format(n_espacios))
