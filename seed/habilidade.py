from model.habilidade import Habilidade

Bulbasauro = [

    Habilidade("Ataque Básico", 10),

    Habilidade("Chuva de folhas", 10),

    Habilidade("Chicote de Raiz", 10),

    Habilidade("Pedrada", 10)


]

Charmander = [

    Habilidade("Ataque Básico", 10),

    Habilidade("Bola de Fogo", 10),

    Habilidade("Lava", 10),

    Habilidade("Chuva de fogo", 10)


]

Chicorita = [

    Habilidade("Ataque Básico", 10),

    Habilidade("Esmagamento", 10),

    Habilidade("Investida", 10),

    Habilidade("Pele de pedra", 10)


]

Pikachu = [

    Habilidade("Ataque Básico", 10),

    Habilidade("Choque", 10),

    Habilidade("Choque do Trovao", 10),

    Habilidade("Curto Circuito", 10)


]



habilidade_bulbasauro = ''
for indice, habilidade in enumerate(Bulbasauro):
    habilidade_bulbasauro += "({}) {} ".format(indice + 1, habilidade.name)

habilidade_charmander = ''
for indice, habilidade in enumerate(Charmander):
    habilidade_charmander += "({}) {} ".format(indice + 1, habilidade.name)

habilidade_chicorita = ''
for indice, habilidade in enumerate(Chicorita):
    habilidade_chicorita += "({}) {} ".format(indice + 1, habilidade.name)

habilidade_pikachu = ''
for indice, habilidade in enumerate(Pikachu):
    habilidade_pikachu += "({}) {} ".format(indice + 1, habilidade.name)