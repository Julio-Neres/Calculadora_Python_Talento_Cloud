def calculadora (numero1, numero2, operacao):
    if operacao ==1:
        resultado =numero1 + numero2
    elif operacao ==2:
        resultado =numero1 - numero2
    elif operacao ==3:
        resultado = numero1 * numero2
    elif operacao ==4:
        resultado = numero1 / numero2
    else:
        resultado =0
    return resultado
numero1= float(input("Insira o primeiro número:"))
operacao= int(input("Insira a operação:\n 1-Soma\n 2-subtração\n 3-multiplicação\n 4-divisão \n"))
numero2=float(input("Insira o segundo número:"))
resultado = calculadora(numero1,numero2,operacao)
print("O resultado é:", resultado)
