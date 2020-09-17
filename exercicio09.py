def exercicio09():

    print("=============================================")
    print("Exercicio 09, Lista Inovação, Tendências e Desafios em T.I.")
    print("=============================================")
    print("Informe Abaixo Quantos Números Deseja Lançar:")
    totaldenumeros = int(input(">>>: "))

    print("Informe os Numeros a Serem Lançados (UM NUMERO POR LINHA!): ")

    numeros = []
    for i in range(totaldenumeros):
        numeros.append(int(input(">>>: ")))

    print("=============================================")
    print(f"A lista informada é: {numeros}")

    for i in range(len(numeros)):
        numeros[i] = numeros[i] ** 2

    print("=============================================")
    print(f"A Lista de Todos os Números Informados ao QUADRADO É: {numeros}")
    print("=============================================")

if (__name__ == '__main__'):
    exercicio09()