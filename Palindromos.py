'''Remova acentos, pontuação e espaços.

Verifique se é um palíndromo (ou seja, a frase lida de trás pra frente é igual à original).

Conte quantas vezes cada letra apareceu (sem acento e sem contar espaços/pontuações).

Exiba:

Se a frase é ou não um palíndromo.

Um dicionário com a contagem de cada letra.'''

frase = input("Digite uma frase:").strip().upper()
palavras = frase.split()

for palavra in palavras:
    if palavra == palavra[::-1]:
        print(f"A palavra {palavra} é um palíndromo")
    else:
        print(f"A palavra {palavra} não é palíndromo")

dict_letras = {}
unique = []

for i in frase:
    if i.isalpha():
        dict_letras[i] = dict_letras.get(i, 0) + 1

lista_unica = unique.append(
    [palavra for palavra, qtd in dict_letras.items() if qtd == 1])
'''unique.append(lista_unica)'''

print(dict_letras)
print(unique)
# Verificar se o indice de cada letra na palavra invertida é o mesmo que da normal
