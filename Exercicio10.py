def exercicio10():

    print("=============================================")
    print("Exercicio 10, Lista Inovação, Tendências e Desafios em T.I.")
    print("=============================================")

    time = (input("Informe o NOME do TIME: "))
    print("=============================================")

    vitorias = int(input("Informe o Número de VITÓRIAS do TIME: "))
    print("=============================================")
    empates = int(input("Informe o Número de EMPATES do TIME: "))
    print("=============================================")
    derrotas = int(input("Informe o Número de DERROTAS do TIME: "))
    print("=============================================")

    total_pontos_vitorias = vitorias * 3

    totaldepontos = total_pontos_vitorias + empates

    print("=============================================")
    print()
    print()
    print(f"{time} tem um TOTAL de {totaldepontos} PONTOS no CAMPEONATO!")
if (__name__ == '__main__'):
    exercicio10()