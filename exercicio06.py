def exercicio06():

    print("=============================================")
    print("Exercicio 06, Lista Inovação, Tendências e Desafios em T.I.")
    print("=============================================")

    numero_interacoes = int(input("Quantos Termos Deseja Visualizar da Sequencia de FIBONACCI? (INFORME UM NUMERO INTEIRO POSITIVO):"))

    numero1, numero2 = 0, 1
    soma = 0

    if numero_interacoes <= 0:
        print("=============================================")
        print("POR FAVOR, INFORME UM NÚMERO POSITIVO!")
    elif numero_interacoes == 1:
        print("=============================================")
        print(f"Sequencia FIBONACCI Com {numero_interacoes} Termo:")
        print(numero1)
    else:
        print("=============================================")
        print(f"Sequencia FIBONACCI Com {numero_interacoes} Termos:")

        while soma < numero_interacoes:
            print(numero1)
            resultado = numero1 + numero2
            numero1 = numero2
            numero2 = resultado
            soma += 1
        print("=============================================")
if (__name__ == '__main__'):
    exercicio06()