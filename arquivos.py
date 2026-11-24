def gerar_proxima_matricula(banco):
    maior_matricula = 1000  # Começa em 1000 para a primeira ser 1001
    try:
        a = open(banco, 'rt', encoding='utf-8')
    except FileNotFoundError:
        return 1001
    else:
        for linha in a:
            dado = linha.strip().split(';')
            if len(dado) >= 1 and dado[0].isdigit():
                mat = int(dado[0])
                if mat > maior_matricula:
                    maior_matricula = mat
        a.close()
    return maior_matricula + 1



def salvar(banco,dados):
    try:
        a = open(banco, 'at', encoding='utf-8')
    except:
        print('\033[31mErro ao abrir o arquivo para salvar!\033[m')
    else:
        try:
            a.write(f"{dados['matricula']};{dados['nome']};{dados['idade']};{dados['cargo']};{dados['cpf']};{dados['salario']}\n")
        except:
            print('\033[31mErro ao escrever os dados no arquivo!\033[m')
        finally:
            a.close()





def cadastro(lista_funcionarios,matricula_atual,doc):
    dados={}
    # Busca diretamente no arquivo qual é a próxima matrícula livre!
    matricula_livre = gerar_proxima_matricula(doc)
    dados['matricula'] = matricula_livre
    dados['nome']=str(input("seu nome: ")).replace(';', '')
    dados['cargo']=str(input("digite o seu cargo: ")).replace(';', '')


    #tratamente de erros 
    try:
        dados['idade']=int(input("sua idade: "))

        cpf = str(input('Digite o CPF: ')).replace('.', '').replace('-', '').strip()
        if len(cpf) != 11 or not cpf.isdigit():
            print('\033[31mCPF inalido\033[m')
            return matricula_atual
        dados['cpf'] = cpf
        dados['salario'] = float(input('Digite o salário: '))
    except (ValueError, TypeError):
        print('\033[31mEvite colocar letras ou caracteres!\033[m')
        return matricula_atual
    else:
        lista_funcionarios.append(dados.copy())
        print('\033[32mSALVO COM SUCESSO!\033[m')
        print(f'Sua matrícula é: \033[32m{dados["matricula"]}\033[m')
        salvar(doc,dados)
        return matricula_atual + 1

def listar_arquivo(banco):
    print('---|\033[33mANALISAR LISTA DE CADASTRO\033[m|---')
    try:
        a = open(banco, 'rt', encoding='utf-8')
    except:
        print('\033[31mErro ao ler o arquivo!\033[m')
    else:
        linhas = a.readlines()
        if not linhas:
            print('\033[31mNenhum funcionário cadastrado no arquivo!\033[m')
        else:
            for indice, linha in enumerate(linhas, start=1):
                dado = linha.strip().split(';')
                if len(dado) == 6:
                    print(f"{indice} - {dado[1]} | Idade: {dado[2]} | Cargo: {dado[3]} | Matrícula: \033[36m{dado[0]}\033[m")
    finally:
        try:
            a.close()
        except:
            pass


def consultar_arquivo(banco):
    print('---|\033[33mCONSULTAR FUNCIONÁRIO\033[m|---')
    busca = str(input('Digite a Matrícula, CPF ou Nome para buscar: ')).replace('.', '').replace('-', '').strip().lower()
    
    if not busca:
        print('\033[31mDigite algo para pesquisar!\033[m')
        return

    try:
        a = open(banco, 'rt', encoding='utf-8')
    except FileNotFoundError:
        print('\033[31mArquivo de cadastro não encontrado!\033[m')
        return

    encontrados = 0
    for linha in a:
        dado = linha.strip().split(';')
        if len(dado) == 6:
            matricula = dado[0]
            nome = dado[1]
            idade = dado[2]
            cargo = dado[3]
            cpf = dado[4]
            salario = float(dado[5])

            # Verifica se a busca bate com matrícula, CPF ou parte do nome
            if busca == matricula or busca == cpf or busca in nome.lower():
                encontrados += 1
                print('-' * 40)
                print(f'Matrícula: \033[36m{matricula}\033[m')
                print(f'Nome:      {nome}')
                print(f'Idade:     {idade} anos')
                print(f'Cargo:     {cargo}')
                print(f'CPF:       {cpf}')
                print(f'Salário:   \033[32mR$ {salario:.2f}\033[m')

    a.close()

    if encontrados == 0:
        print('\033[31mNenhum funcionário encontrado com esses dados.\033[m')
    else:
        print('-' * 40)

def atualizar_arquivo(banco):
    print('---|\033[33mATUALIZAR DADOS DO FUNCIONÁRIO\033[m|---')
    mat_busca = str(input('Digite a Matrícula do funcionário que deseja editar: ')).strip()

    try:
        a = open(banco, 'rt', encoding='utf-8')
        linhas = a.readlines()
        a.close()
    except FileNotFoundError:
        print('\033[31mArquivo de cadastro não encontrado!\033[m')
        return

    encontrado = False
    novas_linhas = []

    for linha in linhas:
        dado = linha.strip().split(';')
        if len(dado) == 6 and dado[0] == mat_busca:
            encontrado = True
            print(f'\nFuncionário encontrado: \033[36m{dado[1]}\033[m (Cargo atual: {dado[3]} | Salário atual: R$ {float(dado[5]):.2f})')
            print('\033[33mDica: Aperte ENTER para manter o valor atual.\033[m\n')

            novo_nome = str(input(f'Novo nome [{dado[1]}]: ')).replace(';', '').strip() or dado[1]
            novo_cargo = str(input(f'Novo cargo [{dado[3]}]: ')).replace(';', '').strip() or dado[3]

            try:
                nova_idade_str = input(f'Nova idade [{dado[2]}]: ').strip()
                nova_idade = int(nova_idade_str) if nova_idade_str else int(dado[2])

                novo_salario_str = input(f'Novo salário [{dado[5]}]: ').strip()
                novo_salario = float(novo_salario_str) if novo_salario_str else float(dado[5])
            except ValueError:
                print('\033[31mValor inválido! Atualização cancelada.\033[m')
                return

            # Monta a linha atualizada mantendo a matrícula (dado[0]) e o CPF (dado[4])
            linha_atualizada = f"{dado[0]};{novo_nome};{nova_idade};{novo_cargo};{dado[4]};{novo_salario}\n"
            novas_linhas.append(linha_atualizada)
        else:
            novas_linhas.append(linha)

    if not encontrado:
        print('\033[31mMatrícula não encontrada!\033[m')
        return

    # Reescreve o arquivo com a lista atualizada
    try:
        a = open(banco, 'wt', encoding='utf-8')
        a.writelines(novas_linhas)
        a.close()
        print('\033[32mDADOS ATUALIZADOS COM SUCESSO!\033[m')
    except:
        print('\033[31mErro ao salvar as alterações no arquivo!\033[m')


def excluir_arquivo(banco):
    print('---|\033[33mEXCLUIR FUNCIONÁRIO\033[m|---')
    mat_busca = str(input('Digite a Matrícula do funcionário que deseja excluir: ')).strip()

    try:
        a = open(banco, 'rt', encoding='utf-8')
        linhas = a.readlines()
        a.close()
    except FileNotFoundError:
        print('\033[31mArquivo de cadastro não encontrado!\033[m')
        return

    encontrado = False
    novas_linhas = []

    for linha in linhas:
        dado = linha.strip().split(';')
        if len(dado) == 6 and dado[0] == mat_busca:
            encontrado = True
            print(f'\nFuncionário encontrado: \033[36m{dado[1]}\033[m | Cargo: {dado[3]} | CPF: {dado[4]}')
            confirmar = str(input('\033[31mTem certeza que deseja excluir este cadastro? [S/N]: \033[m')).strip().upper()

            if confirmar == 'S':
                # Não adiciona essa linha em novas_linhas (isso apaga o registro)
                continue
            else:
                print('\033[33mExclusão cancelada pelo usuário.\033[m')
                return
        else:
            novas_linhas.append(linha)

    if not encontrado:
        print('\033[31mMatrícula não encontrada!\033[m')
        return

    try:
        a = open(banco, 'wt', encoding='utf-8')
        a.writelines(novas_linhas)
        a.close()
        print('\033[32mFUNCIONÁRIO EXCLUÍDO COM SUCESSO!\033[m')
    except:
        print('\033[31mErro ao atualizar o arquivo após exclusão!\033[m')