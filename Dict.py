# Frequência de Vogais e Consoantes Separadas
'''Objetivo:
Dado um texto (frase) digitado pelo usuário, crie dois dicionários separados:

Um com a contagem de cada vogal.

Um com a contagem de cada consoante.

Regras:

Ignore espaços e pontuação.

Não conte números.

Considere apenas letras do alfabeto (A-Z).

Trate maiúsculas e minúsculas como iguais.'''

frase = input("Digite uma frase:").strip().upper()

vogais = ["A","E","I","O","U"]
dict_vogal = {}
dict_conso = {}

'''for i in frase:
    if i in vogais:
        if i not in dict_vogal:
            cont_vogal = frase.count(i)
            dict_vogal[i] = cont_vogal
        else:
            pass
    else:
        if i not in dict_conso and i != " ":
            cont_conso = frase.count(i)
            dict_conso[i] = cont_conso
    
print(dict_vogal)
print(dict_conso)'''


for i in frase:
    if not i.isalpha():
        continue
    if i in vogais:
        dict_vogal[i] = dict_vogal.get(i, 0) + 1
    else:
        dict_conso[i] = dict_conso.get(i, 0) + 1

print("Vogais:", dict_vogal)
print("Consoantes:", dict_conso)
