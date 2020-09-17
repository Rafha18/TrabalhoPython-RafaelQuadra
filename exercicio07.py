from datetime import date

def exercicio07():

    print("=============================================")
    print("Exercicio 07, Lista Inovação, Tendências e Desafios em T.I.")
    print("=============================================")

    X = 24
    Y = 5

    ANO = int(input("Informe o ANO que Deseja saber o Dia da PÁSCOA:"))

    A = ANO % 19
    #print(f"{A}")

    B = ANO % 4
    #print(f"{B}")

    C = ANO % 7
    #print(f"{C}")

    D = (19 * A + X) % 30
    #print(f"{D}")

    E = (2 * B + 4 * C + 6 * D + Y) % 7
    #print(f"{E}")

    if ((D + E) > 9):
        DIA = D + E - 9
        print("=============================================")
        print(f"A PÁSCOA Será/Foi Dia {DIA} de ABRIL no Ano de {ANO}")
        print("=============================================")
    else:
        DIA = D + E + 22
        print("=============================================")
        print(f"A PÁSCOA Será/Foi Dia {DIA} de Março no Ano de {ANO}")
        print("=============================================")


if (__name__ == '__main__'):
    exercicio07()