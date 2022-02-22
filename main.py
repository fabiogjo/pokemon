from seed.pokemon import seed as SeedPokemon, pokemon_string
import os
from os import system, name
from time import sleep


def clear():
    if name == 'nt':
        _ = system('cls')


    else:
        _ = system('clear')


def definindo_pokemon():
    resposta = 0
    while(resposta != 1):
        print("\n" * 100)
        print("Escolha seu pokemon")
        escolha = (int(input(pokemon_string)) - 1)

        if escolha > len(pokemon_string):
            print("Digite um valor válido!")
        else:
            print("\n" * 100)
            pokemon_selecionado = SeedPokemon[escolha]
            print("Voce selecionou {}, level {}\nHabilidades\n{}".format(pokemon_selecionado.name, pokemon_selecionado.level, pokemon_selecionado.habilidades))

        print("Confirmar escolha?")
        resposta = int(input("(1) Sim (2) Não"))


definindo_pokemon()
print('fim')











