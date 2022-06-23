def factorial(numero):
    if numero == 1:
        print("a llegado al caso base")
        return 1
    else:
        print("el numero ahora es", numero)
        return numero*factorial(numero-1)

numFac= int(input("Numero a calcular el factorial: "))
print("Resultado: " +str(factorial(numFac)))