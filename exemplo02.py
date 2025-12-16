
lst_vendas = []
resposta = 's'
venda = 1
tentativa = 1

while resposta != 'n':      # 'não'
    try:
        Valor = float(input(f'\nInforme a {venda}ª venda: '))
    except ValueError:
        print('\nInforme apenas números')
    except KeyboardInterrupt:
        print('\nUsuário encerrou')
        break
    else:
        lst_vendas.append(Valor)
        resposta = input('\nQuer continuar [s/n]? ')[0].lower()               #[0] pega somente a primeira letra e minusculo, caso usuário digite maiúsculo
        venda += 1
    finally:
        print(f'\nTentativa {tentativa}')
        tentativa += 1

print(f'Vendas registradas {lst_vendas}')