import os

restaurantes = [{'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}, {'nome':'João Filho', 'categoria':'Churrascaria', 'ativo':True}, {'nome':'Cachorro Quente', 'categoria':'Lanchonete', 'ativo':False}]


def main():
    exibir_nome_programa()
    menu()
    escolher_opcao()
    
def exibir_nome_programa():
    print("""
        
        Sabor express

        """)
    
def menu():
    '''Essa função é responsável por mostrar o menu do aplicativo'''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar Estado do restaurante')
    print('4. Sair\n')

def cadastrar_novo_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante'''
    
    '''
    Inputs:
    - Nome do restaurante 
    - Categoria do restaurante

    Outputs:
    - adiciona um novo restaurante a lista de restaurantes
    
    '''

    exibir_subtitulo('Cadastro de novos restaurantes')

    print('\n')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastro com sucesso !')

    print('\n')

    voltar_ao_menu_principal()

def listar_restaurante():
    '''Essa função vai listar todos os restaurantes salvos'''

    exibir_subtitulo('Listar restaurantes')

    print(f'{'Nome do restaurante'.ljust(23) } | {'Categoria'.ljust(20)} | {'Estado'} \n')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}\n') 

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função vai alterar o estado dos restaurantes, ela que irá dizer se os restaurantes
    estão ativos ou não'''

    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    print('\n')
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
        
        
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função irá fazer com que a pessoa possa escolher a opção que ela quiser'''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        print('\n')

        #a função match pode ser usada no lugar da função if, pois tem um sintaxe mais simplificada
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante(), print('\n')
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print('\n')

def voltar_ao_menu_principal():
    '''Faz com que o usuário possa voltar ao menu principal do aplicativo'''

    input ('Digite uma tecla para voltar ao menu principal') 
    os.system('cls')
    main()

def opcao_invalida():
    '''Caso o usuário escolha uma opção que não esteja especificada no menu, o aplicativo irá retornar 
        uma mensagem avisando que aqule opção é inválida'''
    
    os.system('cls')
    print('\n')
    print('Opção inválida!\n')

    voltar_ao_menu_principal()

def finalizar_programa():
    exibir_subtitulo('Encerrando o programa!')

if __name__ == '__main__':
    main()
