from soma import soma
from subtrair import subtrair
from multiplicar import multiplicar
from divisao import divisao
from raizquadrada import raizquadrada
from potencia import potencia
from cotacao import cotacao_dolar
from calculardolar import calcular_dolar

def calculadora():
    while True:
        print("""
=== Calculadora ===
1 - soma
2 - subtrair
3 - multiplicar
4 - divisão
5 - raiz quadrada
6 - potencia
7 - cotação       
8 - sair       
          """)
        a = int(input("Digite um número: "))
        b = int(input("Digite o segundo número: "))
        escolha = int(input("O que deseja fazer? "))
        match escolha:
            case 1:
                soma()
            case 2:
                subtrair()
            case 3:
                multiplicar()
            case 4:
                divisao()
            case 5:
                raizquadrada()
            case 6:
                potencia()
            case 7:
                valor = cotacao_dolar()
                print("Dólar hoje: R$ {valor}")
                escolha = int(input("Deseja converter o valor para dólar? "))
                print("""
1 - sim
2 - não
""")
                if escolha == 1:
                    calcular_dolar()
                else:
                    return

            case 8:
                break        
