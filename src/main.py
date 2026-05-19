while True:
    print("1 - Cadastrar aluno")
    print("2 - Media escolar")
    print("3 - Sair")
    escolha = int(input("Digite uma opção: "))

    if escolha == 1:
        nome = input("Digite o nome do aluno: ")
    if escolha == 2:
        nota1= float(input("Insira a primeira nota: "))
        nota2= float(input("Insira a segunda nota: "))
        nota3= float(input("Insira a terceira nota: "))
        nota4= float(input("Insira a quarta nota: "))
        media = (nota1+nota2+nota3+nota4)/4
        if media >= 0 and media <= 10:
                if media >= 7:
                    print(nome)
                    print("Aprovado, sua nota:",media)
                elif media < 7:
                    print(nome)
                    print("Recuperacao, sua nota:",media)
                elif media <4:
                    print(nome)
                    print("Reprovado, sua nota:",media)
        else:
            print("Nota invalida, tente novamente")

          

    elif escolha == 3:
        break
    elif escolha > 4:
        print("Numero invalido, tente novamente")

