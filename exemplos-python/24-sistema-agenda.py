import os

# Lista que armazena todos os clientes
lista_de_clientes = [
    {
        "nome": "Ana Souza",
        "idade": 28,
        "email": "ana.souza@example.com",
        "celular": "(11) 91234-5678"
    },
    {
        "nome": "Bruno Almeida",
        "idade": 35,
        "email": "bruno.almeida@example.com",
        "celular": "(21) 99876-5432"
    },
    {
        "nome": "Carla Mendes",
        "idade": 22,
        "email": "carla.mendes@example.com",
        "celular": "(31) 98765-4321"
    },
    {
        "nome": "Diego Ferreira",
        "idade": 40,
        "email": "diego.ferreira@example.com",
        "celular": "(41) 99555-1111"
    },
    {
        "nome": "Eduarda Lima",
        "idade": 30,
        "email": "eduarda.lima@example.com",
        "celular": "(51) 98888-2222"
    }
]


#Função que limpa a tela
def limpar_tela():
    os.system("cls")

#Função que exibi o menu na tela
def exibir_menu():
    print("\n=== MENU PRINCIPAL ===")
    print('[1] - Cadastro de Clientes')
    print('[2] - Listar Clientes Cadastrados')
    print('[3] - Editar Dados de Cliente')
    print('[4] - Excluir um Cliente')
    print('[5] - Sair do Sistema \n')

#Função que volta para o menu principal
def voltar_ao_menu_principal():
    input("\nPressione <Enter> para voltar ao menu inicial...")
    main()

#Função que cadastrar um novo cliente
def cadastrar_novo_cliente():
    try:
        #chamando a função que limpa a tela
        limpar_tela()
        print("=== CADASTRO DE NOVO CLIENTE ===\n")

        #Solicitando os dados do cliente
        nome    = input("Digite o nome do cliente: ")
        idade   = int(input("Digite a idade do cliente: "))
        email   = input("Digite o e-mail do cliente: ")
        celular = input("Digite o celular do cliente: ")  

        
        #Agrupando os dados do cliente
        dados_cliente = {
            'nome': nome,
            'idade': idade,
            'email': email,
            'celular': celular
        }

        #Adicionar o cliente na lista
        lista_de_clientes.append(dados_cliente)

        #Exibindo mensagem de sucesso
        print(f"\nO Cliente {nome} foi cadastrado com sucesso!")
    
    except:
        print("A idade deve ser um número")
       
    
    finally: 
         #Voltar para o menu principal   
        voltar_ao_menu_principal()
   

#Função que Lista todos os clientes cadastrados
def listar_clientes_cadastrados():
    #chamando a função que limpa a tela
    limpar_tela()
    print("=== LISTA DE CLIENTES CADASTRADOS ===\n")

    #Listando os clientes
    for cliente in lista_de_clientes:
        print(f"Nome: {cliente['nome']} | Idade: {cliente['idade']} | E-mail: {cliente['email']} | Celular: {cliente['celular']}")

    #Volta para o menu principal
    voltar_ao_menu_principal()

#Função que exclui um cliente cadastrado
def excluir_cliente():
    #Chamando a função que limpa a tela
    limpar_tela()
    print("=== REMOVER CLIENTE ===\n")

    #indice = 0    
    
    #Listando os clientes cadastrados    
    for indice, cliente in enumerate(lista_de_clientes):
        print(f"Indíce: {indice} | Nome: {cliente['nome']} | Idade: {cliente['idade']} | E-mail: {cliente['email']} | Celular: {cliente['celular']}")
    
    try:
        #Solicitar ao usuario o indice para remover
        indice = int(input("\nDigite o indíce do cliente que deseja remover:  "))

        if indice >= 0 and indice < len(lista_de_clientes):
            #Excluir o cliente escolhido
            cliente_removido = lista_de_clientes.pop(indice)

            print(f"\nCliente {cliente_removido['nome']} removido com sucesso!")
        else:
            print("índice inválido")
    except:
        print("Digite um indice válido")
    
    finally:
        #volta ao menu principal
        voltar_ao_menu_principal()

#Função para editar um usuário
def editar_dados_clientes():
    limpar_tela()
    print("=== EDITAR DADOS DO CLIENTE ===\n")

     #Listando os clientes cadastrados    
    for indice, cliente in enumerate(lista_de_clientes):
        print(f"Indíce: {indice} | Nome: {cliente['nome']} | Idade: {cliente['idade']} | E-mail: {cliente['email']} | Celular: {cliente['celular']}")
    
    try:
        #Solicitar ao usuario o indice para remover
        indice = int(input("\nDigite o indíce do cliente que deseja editar:  "))

        if indice >=0 and indice < len(lista_de_clientes):

            #Capturar os dados do cliente selecionado
            dados_do_cliente = lista_de_clientes[indice]

            #Exibindo os dados do cliente selecionado
            print(f"\nEditando os dados do cliente: {dados_do_cliente['nome']}")

            #Solicitando os novos dados
            novo_nome = input(f"Digite o novo nome (Atual - {dados_do_cliente['nome']}):")
            nova_idade = input(f"Digite a nova idade (Atual - {dados_do_cliente['idade']}):")
            novo_email = input(f"Digite o novo e-mail (Atual -{dados_do_cliente['email']}):")
            novo_celular = input(f"Digite o novo celular (Atual -{dados_do_cliente['celular']}):")

            #Editar 
            dados_do_cliente['nome']    = novo_nome
            dados_do_cliente['idade']   = nova_idade
            dados_do_cliente['email']   = novo_email
            dados_do_cliente['celular'] = novo_celular

            print("\nDados Atualizados com sucesso!")
    except:
            print("Idade ou indice devem ser válidos")

    finally:
        voltar_ao_menu_principal()


#Função Principal do meu programa
def main():
    #chamar a função que limpa a tela
    limpar_tela()
    print("Bem vindo ao Gerenciador de Clientes")

    #Chamar a função que exibi o menu
    exibir_menu()

    #Solicitando uma opção para o usuario
    opcao = int(input('Escolha uma opção: '))

    #Verificando qual foi a opção escolhida
    if opcao == 1:
        #Abrir o cadastro de um novo cliente
        cadastrar_novo_cliente()
    
    elif opcao ==2:
        #Abrir a listagem de clientes cadastrados
        listar_clientes_cadastrados()

    elif opcao ==3:
        #Abrir a edição de clientes
        editar_dados_clientes()    

    elif opcao ==4:
        #Abrir a exclusão de um cliente
        excluir_cliente()
    elif opcao ==5:
        input("Pressione <Enter> para encerrar o programa...")
        exit()
    else:
        print("Opção Inválida!")







#Chamando a função principal
main()