def exercicio04():

    print("=============================================")
    print("Exercicio 04, Lista Inovação, Tendências e Desafios em T.I.")
    print("=============================================")

    arquivo1 = open("nomes.txt")
    arquivo2 = open("nomes2.txt")

    list01 = list(set(arquivo1))
    list02 = list(set(arquivo2))

    print(f"A Lista 01 contem os seguintes nomes: {list01}")
    print("=============================================")
    print(f"A lista 02 contem os seguintes nomes: {list02}")
    print("=============================================")

    lista_final = list(set(list01) - set(list02))

    print(f"A diferença é: {lista_final}")


if (__name__ == '__main__'):
    exercicio04()
