print("Digite uma palavra para que o programa conte as letras")
palavra = str(input("Digite uma palavra: ")).upper()

contador = len(palavra)
print(f"A palavra {palavra} tem {contador} letras.")

vogal = ["A", "E", "I", "O", "U"]

consoantes = 0
vogais = 0

for i in palavra:
    if i not in vogal:
        consoantes += 1
    else:
        vogais += 1
print(f"A Palavra tem {contador} letras, {consoantes} consoantes e {vogais} vogais")