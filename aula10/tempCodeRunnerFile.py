
for num in range(1, 4):
    try:
        venda = float(input('Informe o valor da venda: '))
        meta = float(input('Informe a meta: '))
        resultado = calcula_atingimento(venda, meta)
        # print(f'Resultado: {resultado}')      # retiro o print daqui e jogo no else, tbm é uma opção

    except ValueError:
        print('\nErro!!! Digite apenas números')
    except ZeroDivisionError:
        print('\nErro!!! A meta não pode ser zero')
        exit()
    except KeyboardInterrupt:
        print('\nOperação finalizada pelo usuário')
    else:                                                       # else é quando não tiver nenhum erro, não entrou nos erros sinalizado anteriormente.
        print(f'Resultado: {resultado}%')
    finally:
        print('Operação Finalizada')