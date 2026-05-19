while True:
    print("1 - Cadastrar aluno")
    print("2 - Media escolar")
    print("3 - Sair")
    escolha = int(input("Digite uma opção"))

    if escolha == 1:
        input("Digite o nome do aluno: ")
        input("Digite a turma do aluno:")
    elif escolha == 2:
       nota1= float(input("Insira a primeira nota"))
       nota2= float(input("Insira a segunda nota"))
       nota3= float(input("Insira a terceira nota"))
       nota4= float(input("Insira a quarta nota"))
       media = (nota1+nota2+nota3+nota4)/4
       print ("Nota final:",media)
    elif escolha == 3:
        break
    else:
        print("Numero invalido, tente novamente")
        

           