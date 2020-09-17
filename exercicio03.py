def exercicio03():

    print("=============================================")
    print("Exercicio 03, Lista Inovação, Tendências e Desafios em T.I.")
    print("=============================================")
    print("Informe Abaixo 3 Números Inteiros (Um Numero Por Linha!)")

    numeros = []
    for i in range(3):
        numeros.append(int(input(">>>: ")))

    print("=============================================")
    print(f"A lista informada é: {numeros}")
    print("=============================================")

    soma = numeros[0] + numeros[1] + numeros[2]
    pot = numeros[0] ** 3

    if numeros[0] == numeros[1] == numeros[2]:
        print(f"Voce Informou 3 Números Iguais, o Número {numeros[0]} Foi Elevado a Potência 3, com o resultado de: {pot}")
    else:
        print(f"O Resultado da SOMA dos Números Informados São: {soma}")


if (__name__ == '__main__'):
    exercicio03()





















