'''Peça ao usuário uma frase e:

Conte quantas palavras existem.

Crie um dicionário com as letras únicas e quantas vezes cada uma aparece (sem acentos e espaços).'''

frase = input("Digite uma frase:").strip().upper()

palavra = frase.split()
print(f"A frase {frase} possui", len(palavra), "palavras")

unique = []
dict_letras = {}

'''for i in frase:
    if i.isalpha():
        if frase.count(i) == 1:
            unique.append(i)
        else:
            dict_letras[i] = dict_letras.get(i, 0) + 1'''  # Desconsidera no dict_letras as letras unicas

for i in frase:
    if i.isalpha():
        # Esse zero é um valor padrão, caso não tenha no dict
        dict_letras[i] = dict_letras.get(i, 0) + 1
        # Adiciona a letra = 0 e depois + 1
        # Precisa começar com zero senao o python vai somar none com 1
        # Daria erro

letras_unicas = [letra for letra, qtd in dict_letras.items() if qtd == 1]

print("Letras únicas:", letras_unicas)
print("Dicionário de letras:", dict_letras)
