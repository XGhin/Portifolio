def main():
    def somar(A, B):
        C = A + B
        return C
    def subtrair(A, B):
        C = A - B
        return C
    
    def dividir(A, B):
        C = A / B
        return C

    def multiplicar(A, B):
        C = A * B
        return C
        
    def potencia(A, B):
        C = A ** B
        return C
        
        
    def raiz(A, B):
        C = A ** (1/B)
        return C
    
    
    def apresentacao():    
        print("\n\n")
        print("Escolha uma das operações abaixo:")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Dividir")
        print("4 - Multiplicar")
        print("5 - Potencia")
        print("6 - Raiz")
        operacao = int(input("Qual operação você deseja fazer?"))
        
        A = int(input("Digite o primeiro valor: "))
        B = int(input("Digite o segundo valor: "))
        
        if operacao == 1:
            C = somar(A, B)
            return C

        if operacao == 2:
            C = subtrair(A, B)
            return C
        
        if operacao == 3:
            C = dividir(A, B)
            return C
            
        if operacao == 4:
            C = multiplicar(A, B)
            return C
            
        if operacao == 5:
            C = potencia(A, B)
            return C
            
        if operacao == 6:
            C = raiz(A, B)  
            return C
            
        else:
            print("\nOperação inválida")
            apresentacao()
            
        continuacao(C)
    
    
    def continuacao(C):
        print("\n")
        print("O resultado atual foi: {}" .format(C))
        print("Escolha uma das operações abaixo:")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Dividir")
        print("4 - Multiplicar")
        print("5 - Potencia")
        print("6 - Raiz")
        print("0 - Finalizar Calculo")
        operacao = int(input("Qual operação você deseja fazer?"))
        
        B = int(input("Digite o segundo valor: "))
        
        if operacao == 1:
            somar(C, B)

        if operacao == 2:
            subtrair(C, B)
        
        if operacao == 3:
            dividir(C, B)
            
        if operacao == 4:
            multiplicar(C, B)
            
        if operacao == 5:
            potencia(C, B)
            
        if operacao == 6:
            raiz(C, B)  
            
        if operacao == 0:
            print("\nObrigado por usar a minha calculadora")
            return 0
               
        else:
            print("\nOperação inválida")
            continuacao()
            
            
    apresentacao()
    
    print("Obrigado por usar a minha calculadora")

print("Bem vindo a minha calculadora em Python")


main()