import arquivos as df
#função para criar um arquivo

def criarArquivo(nome):
    try:
        aq= open(nome,'wt+')
        aq.close()
    except:
        print('houve um erro ao criar um arquivo')
    else:
        print(f'arquivo {nome} criado com sucesso')


def arquivo(nome):
    try:
        a= open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True



funcionarios=[]
proxima_matricula=1001
arq='historico.txt'

if not  arquivo(arq):
    criarArquivo(arq)



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
    print("4-atualizar cadstro")
    print("5-deletar dados do duncionario")
    try:
     op=int(input("escolha uma opção:"))
    except (ValueError,TypeError):
        print("\033[31mdigite apenas numeros \033[m")
    else:
    
        #condições
        if op == 1:
            linha('---|CADASTRAR|---')
            proxima_matricula=df.cadastro(funcionarios,proxima_matricula,arq)

            
        elif op == 2:
            df.listar_arquivo(arq)
        elif op == 3:
                 df.consultar_arquivo(arq)
        elif op == 4:
            df.atualizar_arquivo(arq)
        elif op == 5:
            df.excluir_arquivo(arq)
                    
                    

        elif op == 0:
            print('---|SAIR|---')
            break
        else:
             print('opção invalida')