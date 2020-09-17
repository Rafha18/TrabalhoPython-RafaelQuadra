def exercicio05():

    print("=============================================")
    print("Exercicio 05, Lista Inovação, Tendências e Desafios em T.I.")
    print("=============================================")

    numpalavras = int(input("Informe o Número de Palavras que Deseja Armazenar:"))


    palavras = []
    for i in range(numpalavras):
        palavras.append(input(">>>: "))

    print("=============================================")
    print(f"A lista informada é: {palavras}")
    print("=============================================")
    maxpalavras = list(map(str, palavras))
    print("A Maior Palavra Informada é:")
    print(max(maxpalavras))

if (__name__ == '__main__'):
    exercicio05()