from model.pokemon import Pokemon
from seed.habilidade import habilidade_bulbasauro, habilidade_charmander, habilidade_chicorita, habilidade_pikachu


seed = [

    Pokemon("Bulbasauro",
            60, habilidade_bulbasauro),

    Pokemon("Charmander",
            70,
            habilidade_charmander),

    Pokemon("Chicorita",
            70,
            habilidade_chicorita),

    Pokemon("Pikachu",
            70,
            habilidade_pikachu)


]

pokemon_string = ''
for indice, monstro in enumerate(seed):
    pokemon_string += "({}) {} ".format(indice + 1, monstro.name)