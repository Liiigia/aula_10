# Atividade 01
# VsCode -  Github
# receba 3 pares de números e faça a soma de cada par, mostrando o resultado.  
# Requisitos: funções, laços de repetição e Tratamento de Exceções
 
# 1 - Solicitar dois valores ao usuário. 
# 2 - Somar os valores. 
# 3 - Repetir a operação 3 vezes. 
# 4 - Tratar possíveis erros de entrada com try/except... 
# 5 - Exibir o resultado da soma quando não houver erro. 



def soma(v1 , v2):
    t = v1 + v2
    return t


for i in range(1, 4):
    try:
        valor1 = float(input('Digite um valor1: '))
        valor2 = float(input('Digite um valor1: '))
        total = soma(valor1, valor2)
    print(total)

    except ValueError:
        print('\Erro, digite apenas números')
    else:
        print('\Tudo ok')
    finally:
        print('Processo finalizado')

    
    


    


        



