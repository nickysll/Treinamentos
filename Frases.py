# Contar uma letra especifica

# Retira os espaços com strip e deixa em maiusculo
frase = input("Digite uma frase:").strip().upper()
letra = input("Escolha uma letra para contar:").upper()

contagem_letra = 0

for i in frase:
    if i == letra:
        contagem_letra += 1

# Para cada letra (i) na frase, se a letra for igual a letra(variavel) escolhida pelo usuario
# então incrementa +1 na contagem

print(f"A frase possui {contagem_letra} vezes a letra {letra}")

# Contar a quantidade de palavras na frase

palavras = frase.split()  # Pega apenas as palavras da frase
contagem = len(palavras)  # Conta a quantidade de palavras
print(contagem)

# Contar as letras sem o espaço
contador_letra = 0

for palavra in palavras:
    for i in palavra:
        contador_letra += 1

print(contador_letra)

# Para cada palavra em palavras, para cada letra na palavra então adicione +1 no contador

# Contar quantas vezes cada letra aparece

dicionario_letras = {}

for letra in frase:
    if letra == ' ':
        pass
    else:
        contagem = frase.count(letra)
        dicionario_letras[letra] = contagem

print(dicionario_letras)

# Primeiro cria o dict vazio, depois para cada letra na frase, se a letra for igual a vazio (Pois espaço é considerado str)
# Se vazio então passe, senão então conte na frase a quantidade da letra e adicione chave(letra):valor(contagem)

# Outra opção
dicionario_letras = {}

for letra in frase:
    if letra != ' ' and letra not in dicionario_letras:
        dicionario_letras[letra] = frase.count(letra)

print(dicionario_letras)

# Pois se o A ja estiver no dict, vai percorrer varias vezes o loop
