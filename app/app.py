import os

restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}
]


def exibir_nome_do_programa():
    """Exibe o nome do programa no terminal."""
    print("=== SABOR EXPRESS ===\n")


def exibir_opcoes():
    """Mostra as opções disponíveis no menu principal do sistema."""
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')


def finalizar_app():
    """Finaliza a execução do aplicativo exibindo uma mensagem final."""
    exibir_subtitulo('Finalizar app')


def voltar_ao_menu_principal():
    """Aguarda o usuário e retorna ao menu principal."""
    input('\nDigite uma tecla para voltar ao menu ')
    main()


def opcao_invalida():
    """Exibe mensagem de erro para uma opção inválida."""
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    """Limpa o terminal e exibe um subtítulo formatado.

    Args:
        texto (str): Texto que será exibido como título da seção.

    Returns:
        None
    """
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    """Solicita dados do usuário e cadastra um novo restaurante.

    Returns:
        None
    """
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurante = {
        'nome': nome_do_restaurante,
        'categoria': categoria,
        'ativo': False
    }

    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()


def listar_restaurantes():
    """Exibe todos os restaurantes cadastrados com categoria e status.

    Returns:
        None
    """
    exibir_subtitulo('Listando restaurantes')

    print(f'{"Nome do restaurante".ljust(23)} | {"Categoria".ljust(20)} | Status')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = "Ativado" if restaurante['ativo'] else "Desativado"

        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    """Ativa ou desativa um restaurante com base no nome informado.

    Returns:
        None
    """
    exibir_subtitulo('Alterando estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']

            mensagem = (
                f'O restaurante {nome_restaurante} foi ativado com sucesso'
                if restaurante['ativo']
                else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            )

            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')

    voltar_ao_menu_principal()


def escolher_opcao():
    """Lê a opção escolhida pelo usuário e executa a ação correspondente.

    Returns:
        None
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except:
        opcao_invalida()


def main():
    """Inicializa o sistema e exibe o menu principal.

    Returns:
        None
    """
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()