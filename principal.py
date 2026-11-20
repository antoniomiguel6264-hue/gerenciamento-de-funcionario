funcionarios=[]
proxima_matricula=1001

def linha(msg):
    print('='*len(msg))
    print(msg)
    print('='*len(msg))    


while True:
    dados={}
    linha('GERENCIAMENTO DE FUNCIONARIO ')

    print("0-sair")
    print("1-cadastra")
    print("2-listar")
    print("3-informações dos funcionarios")
    try:
     op=int(input("escolha uma opção:"))
    except (ValueError,TypeError):
        print("\033[31mdigite apenas numeros \033[m")
    else:
    
        #condições
        if op == 1:
            linha('---|CADASTRAR|---')
            dados['matricula']=proxima_matricula

            dados['nome']=str(input('digite o nome :'))
            dados['cargo']=str(input('digite o cargo:'))
            
            try:
                
                cpf=str(input('digite o cpf: ')).replace('.', '').replace('-', '')

                
                if len(cpf) != 11 or not cpf.isdigit():
                    print('\033[31mCPF inválido!\033[m')
                    continue

                dados['cpf'] = cpf
                
                
                dados['salario']=float(input('digite o salario:'))
            except(ValueError,TypeError):
                print("evite colocar letras ou caracteres")
            else:
                print('SALVO COM SUCESSO!')
                print(f'sua matricula é :\033[32m{dados["matricula"]}\033[m ')
                #ADICIONAR OS DADOS NA LISTA
                funcionarios.append(dados.copy())
                proxima_matricula+=1

            
        elif op == 2:
            print('---|\033[33mANALISAR LISTA DE CADASTRO\033[m---')
            if not funcionarios:
                  print('Nenhum funcionário cadastrado!')

            else:
                 for indice, pessoa in enumerate(funcionarios, start=1):
                  print(f'{indice} - {pessoa["nome"]}')
        elif op == 3:
                  while True:
                      consuta=str(input("deseja consultar algum funcionario (s/n): "))
                      if consuta in 'Ss':
                         busca = str(input('Qual funcionário deseja consultar? matricula ou cpf '))
                         encontrou=False


                         for pessoa in funcionarios:
                            if busca == str(pessoa['matricula']) or busca == pessoa['cpf'] or busca.lower() in pessoa['nome'].lower():
                

                                print(f'Nome: {pessoa["nome"]}')
                                print(f'Cargo: {pessoa["cargo"]}')
                                print(f'matricula:\033[36m{pessoa["matricula"]}\033[m')
                                print(f'CPF:\033[36m{pessoa["cpf"]}\033[m')
                                print(f'Salário: R$ {pessoa["salario"]:.2f}')
                                encontrou=True
                                

                         if not encontrou:
                             print("funcionario não encontrado")
                      elif consuta in 'Nn':
                          break

                      else:
                           print('Funcionário não encontrado!')

        elif op == 0:
            print('---|SAIR|---')
            break
        else:
             print('opção invalida')