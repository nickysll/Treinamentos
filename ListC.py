# Atribua os valores 100 e 200 às variáveis x e y usando desempacotamento.
x, y = 200, 100

print(f"x = {x}\ny = {y}")

# Dada a lista valores = [3, 7, 9], atribua o primeiro valor a a, o segundo a _ (ignorar), e o terceiro a b
a, _, b = [3, 7, 9]

print(f"a = {a}\nb = {b}")

# Use um for com enumerate() para imprimir o índice e a palavra de uma lista:

palavras = ["ovo", "casa", "radar", "sol"]

for i, palavra in enumerate(palavras):
    print(f"{i} : {palavra}")

# Dada a lista nomes = ["ana", "bia", "carla"], crie uma nova lista com strings no formato:

nomes = ["ana", "bia", "carla"]

lista = [f"{i} - {nome.upper()}" for i, nome in enumerate(nomes)]

print(lista)

# 5. List comprehension com desempacotamento de tuplas

pares = [(1, 2), (3, 4), (5, 6)]
# Crie uma nova lista com a soma de cada par, usando list comprehension e desempacotamento.

list_soma = [a + b for a, b in pares]
print(list_soma)

trios = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

lista_trios = [a + b + c for a, b, c in trios]
print(lista_trios)

multi_trios = [a * b * c for a, b, c in trios]
print(multi_trios)

multi_par = [a + b + c for a, b, c in trios if (a + b + c) % 2 == 0]
print(multi_par)

# Crie uma nova lista contendo apenas os nomes que estão em índices ímpares,
# e coloque-os em letras maiúsculas, com o índice ao lado.

nomes = ["ana", "bia", "carla", "danilo", "elisa"]

lista_nome = [f"{i} - {nome.upper()}" for i,
              nome in enumerate(nomes) if i % 2 != 0]
print(lista_nome)

# Comparar listas de notas
aluno1 = [7, 8.5, 6, 9]
aluno2 = [6.5, 8.5, 7, 5]

'''Crie uma nova lista com mensagens comparando as notas:

Se a nota do aluno1 for maior → "Aluno 1 venceu"

Se a nota do aluno2 for maior → "Aluno 2 venceu"

Se forem iguais → "Empate"'''

lista_notas = []

for nota1, nota2 in zip(aluno1, aluno2):
    if nota1 > nota2:
        lista_notas.append("Aluno 1 venceu")
    elif nota1 < nota2:
        lista_notas.append("Aluno 2 venceu")
    else:
        lista_notas.append("Empate")

print(lista_notas)

teste = ["Aluno 1 Venceu" if nota1 > nota2 else
         "Aluno 2 venceu" if nota2 > nota1
         else "Empate" for nota1, nota2 in zip(aluno1, aluno2)]
print(teste)

# Ranking de alunos

alunos = ["Ana", "Bia", "Carlos", "Danilo"]
notas = [8.5, 9.0, 7.5, 6.0]

'''Crie uma lista com strings no formato:
"1º lugar: Bia - Nota 9.0"
"2º lugar: Ana - Nota 8.5"
(ordem decrescente pela nota)

Depois, transforme essa lista em um dicionário, com o nome do aluno como chave e a nota como valor'''

# Sorted para ordenar, key= especifica com base em que deseja ordenar, Reverse= Ordem crescente
ordena = sorted(zip(alunos, notas), key=lambda x: x[1], reverse=True)

ranking = [f"{i + 1}º lugar: {aluno} - nota {nota}" for i,
           (aluno, nota) in enumerate(ordena)]
print(ranking)
print(ordena)


# Ranking de filmes
'''Junte as duas listas em uma lista de tuplas com zip.

Ordene os filmes por nota, da maior para a menor.'''

filmes = ["Barbie", "Oppenheimer", "Interstellar", "Duna", "Avatar"]
notas = [9.5, 9.7, 9.3, 8.8, 9.0]

ordenacao = sorted(zip(filmes, notas), key=lambda x: x[1], reverse=True)

lista_filmes = [f"{i + 1}º lugar: {filme} - nota: {nota}" for i,
                (filme, nota) in enumerate(ordenacao)]

print(lista_filmes)
