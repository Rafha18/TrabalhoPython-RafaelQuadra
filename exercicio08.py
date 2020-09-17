def exercicio08():

    print("=============================================")
    print("Exercicio 08, Lista Inovação, Tendências e Desafios em T.I.")
    print("=============================================")
    print("Informe Abaixo Quantos Números Deseja Lançar:")
    totaldenumeros = int(input(">>>: "))

    print("Informe os Numeros a Serem Lançados (UM NUMERO POR LINHA!): ")

    numeros = []
    for i in range(totaldenumeros):
        numeros.append(int(input(">>>: ")))

    print("=============================================")
    print(f"A lista informada é: {numeros}")

    soma = sum(numeros)
    media = soma / totaldenumeros

    print("=============================================")
    print(f"A SOMA dos Números Informados é: {soma}")
    print("=============================================")
    print(f"A MÉDIA dos Números Informados é: {media}")
    print("=============================================")


if (__name__ == '__main__'):
    exercicio08()