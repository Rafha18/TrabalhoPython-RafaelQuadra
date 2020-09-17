def exercicio02():

    print("=============================================")
    print("Exercicio 02, Lista Inovação, Tendências e Desafios em T.I.")
    print("=============================================")

    numero_inteiro = input("Informe um Número Inteiro:")
    par_ou_impar = int(numero_inteiro)
    print("=============================================")
    print(f"O Número Informado é: {par_ou_impar}")

    if (par_ou_impar % 2 == 0):
        print(f"O Numero {par_ou_impar} é PAR!")
    else:
        print(f"O Numero {par_ou_impar} é IMPAR!")

if (__name__ == '__main__'):
    exercicio02()
