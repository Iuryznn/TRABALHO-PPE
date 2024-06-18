cliente = {
    'nome': '',
    'telefone': '',
    'email': '',
    'senha': ''
}

camisas_M = {
    '0': {'GROW COMPANY TRIANGLE VERDE': '129,99'},
    '1': {'BAZON MESCLA': '129,99'},
    '2': {'GROW COMPANY CANYONS MESCLA': '129,99'},
    '3': {'GROW COMPANY SQUARE MESCLA': '129,99'},
    '4': {'HOCKS CINZA ESCURO': '79,99'},
    '5': {'GROW COMPANY LINES MARINHO': '129,99'},
    '6': {'GROW COMPANY LOGO DIAG MARINHO': '129,99'},
    '7': {'GROW COMPANY SQUARE MARINHO': '129,99'},
    '8': {'GROW COMPANY LOGO DIAG BEGE': '129,99'},
    '9': {'GROW COMPANY STICK BEGE': '129,99'},
    '11': {'GROW COMPANYN GREFFITI PRRETO': '129,99'},
    '12': {'BAZON PRETO': '129,99'},
    '13': {'LRG VERMELH0': '79,99'},
    '14': {'GROW COMPANY BOMGROW BRANCO': '129,99'},
    '15': {'BAZON BRANCO': '129,99'},
    '16': {'GROW COMPANY MACBA BRANCO': '129,99'},
    '17': {'GRIZZLY BRANCO': '79,99'}

}

camisas_G = {
    '0': {'ASTON ROSA': '79,99'},
    '1': {'BAZON  MESCLA': '129,99'},
    '2': {'GROW COMPANY AQUARE BEGE': '129,99'},
    '3': {'GROW COMPANY LOGO 3x3 MARINHO': '129,99'},
    '4': {'GROW COMPANY LOGO DIAG MARINHO': '129,99'},
    '5': {'SANTA CRUZ MANGA LONGA MESCLA': '79,99'},
    '6': {'NEW ERA MESCLA': '129,99'},
    '7': {'GROW COMPANY SQUARE MESCLA': '129,99'},
    '8': {'GROW COMPANY LOGO 3x3 MESCLA': '129,99'},
    '10': {'ASTON - CHUMBO': '79,99'},
    '11': {'SURF SCREAM CLASSIC DIVISION PRETO': '89,99'},
    '12': {'GROW COMPANY BORD - G PRETO': '129,99'},
    '13': {'GROW COMPANY GOLDEN GATE PRETA': '129,99'},
    '14': {'GROW COMPANY STICK PRETA': '129,99'},
    '15': {'ADIO  PRETO': '79,99'},
    '16': {'BAZON PRETO': '129,99'},
    '17': {'ASTON PRETO': '79,99'},
    '18': {'GROW COMPANY - LINES PRETO': '129,99'},
    '19': {'BAZON - MANGA COMPRIDA BRANCA': '139,99'},
    '21': {'BAZON - BRANCA': '129,99'},
    '22': {'GROW COMPANY - CANYONS BRANCO': '129,99'},
}

carrinho_compras = {}

nome_completo = input('NOME COMPLETO: ').upper()
telfone = (input('CELULAR: '))
email = input('EMAIL: ').lower()
senha = input('SENHA: ')

cliente['nome'] = nome_completo
cliente['telefone'] = telfone
cliente['email'] = email
cliente['senha'] = senha

print(f'PRAZER EM CONHECER VOCÊ {cliente['nome']}')
acesso_catalogo = input('PARA TER ACESSO AO CATALOGO DIGITE (1): ')

while acesso_catalogo != '1':
    print('ACESSO NEGADO')
    acesso_catalogo = input('PARA TER ACESSO AO CATALOGO DIGITE (1): ')

if acesso_catalogo == '1':
    print('ACESSO PERMITIDO: ')
    print('----CATALOGO----')

    escolha = input('O QUE VOCÊ PROCURA?\n(1) CAMISETAS\n(2) CALÇA\n(3) BERMUDA\n(4) MOLETOM\n(5) BONÉ\n(6) GORRO\n(7) MEIA\n(8) SLIDE\nDIGITE O NÚMERO: ')

    if escolha == '1':
        camisetas = input('ESCOLHA O TAMANHO:\n(1) M\n(2) G\n(3) GG\n(4) XG\nDIGITE O NÚMERO: ')

        if camisetas == '1':

            for produto, preco in camisas_M.items():
                print(produto, preco)
            
            while True:
                escolha_produto = input('DIGITE O NÚMERO DA PEÇA QUE DESEJA OU (X) PARA ENCERRAR: ').upper()


                if escolha_produto == 'X':
                    print('SESSÃO ENCERRADA')

                    break


                elif escolha_produto in camisas_M:
                    produto = list(camisas_M[escolha_produto].keys())[0]
                    preco = list(camisas_M[escolha_produto].values())[0]
                    carrinho_compras[produto] = preco
                    print(f'PRODUTO {produto} ADICIONADO NO CARRINHO')


                else:
                    print('PRODUTO NÃO ENCONTRADO')

        elif camisetas == '2':
            for produto, preco in camisas_G.items():
                print(produto, preco)
            
            while True:
                escolha_produto = input('DIGITE O NÚMERO DA PEÇA QUE DESEJA OU (X) PARA ENCERRAR: ').upper()

                if escolha_produto == 'X':
                    print('SESSÃO ENCERRADA')

                    break

                elif escolha_produto in camisas_G:
                    produto = list(camisas_G[escolha_produto].keys())[0]
                    preco = list(camisas_G[escolha_produto].values())[0]
                    carrinho_compras[produto] = preco
                    print(f'PRODUTO {produto} ADICIONADO NO CARRINHO')

print('\nCARRINHO DE COMPRAS:')


for produto, preco in carrinho_compras.items():
    print(f'PRODUTO: {produto}\nPREÇO: {preco}')
