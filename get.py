'''Contar todas as letras de uma frase, ignorando espaços, e separar em dois dicionários — um para vogais e outro para consoantes.
Regras:

O programa deve pedir uma frase.

Ignorar letras com acento, pontuação ou espaços.

Tudo deve ser contado em maiúsculas.

Utilize .get() para preencher os dicionários.'''

frase = input("Digite uma frase:").strip().upper()

vogais = ["A", "E", "I", "O", "U"]
dict_vogal = {}
dict_conso = {}

for i in frase:
    if not i.isalpha():  # Ignora acentos, pontuações e espaços
        continue
    if i in vogais:
        dict_vogal[i] = dict_vogal.get(i, 0) + 1
    else:
        dict_conso[i] = dict_conso.get(i, 0) + 1

print(f"Vogais: {dict_vogal} \n Consoantes: {dict_conso}")
