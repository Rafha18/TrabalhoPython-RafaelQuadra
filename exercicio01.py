def exercicio01():
    print("=============================================")
    print("Exercicio 01, Lista Inovação, Tendências e Desafios em T.I.")
    print("=============================================")

    lista = []
    lista = input("Informe uma Lista de 10 Números Sem Espaços ou Caracteres Especiais:")
    lista_usuario = lista

    print("=============================================")
    print(f"A lista informada é: {lista_usuario}")
    print("=============================================")
    print(f"O Primeiro Número da Lista Informada é: {lista_usuario[0]}")
    print("=============================================")
    print(f"O Ultimo Número da Lista Informada é: {lista_usuario[9]}")
    print("=============================================")


if (__name__ == '__main__'):
    exercicio01()
