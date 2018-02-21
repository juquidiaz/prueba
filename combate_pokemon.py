
pokemon_elegido = input("¿Contra qué pokemon quieres combatir? (Squirtle / Charmander / Bulbasaur: ").upper()

vida_pikachu = 100
vida_enemigo = 0

if pokemon_elegido == "SQUIRTLE":
    vida_enemigo = 90
    nombre_pokemon = "Squirtle"
elif pokemon_elegido == "CHARMANDER":
    vida_enemigo = 80
    nombre_pokemon = "Charmander"
elif pokemon_elegido == "BULBASAUR":
    vida_enemigo = 100
    nombre_pokemon = "Bulbasaur"


while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿Que ataque vamos a usar? (Chispazo / Bola voltio)").upper()

    if ataque_elegido == "CHISPAZO":
        vida_enemigo -= 10
    elif ataque_elegido == "BOLA VOLTIO":
        vida_enemigo -= 12

    print("La vida de {} es de {}".format(nombre_pokemon, vida_enemigo))

    if pokemon_elegido == "SQUIRTLE":
        print("Squirtle te hace un ataque de 8 de daño")
        vida_pikachu -= 8

    elif pokemon_elegido == "CHARMANDER":
        print("Charmander te hace un ataque de 7 de daño")
        vida_pikachu -= 7

    elif pokemon_elegido == "BULBASAUR":
        print("Bulbasaur te hace un ataque de 10 de daño")
        vida_pikachu -= 10

    print("La vida de Pikachu es de {}".format(vida_pikachu))

if vida_enemigo <=0:
    print("¡Has ganado!")

if vida_pikachu <=0:
    print("¡Has perdido!")

print("El combate ha terminado")