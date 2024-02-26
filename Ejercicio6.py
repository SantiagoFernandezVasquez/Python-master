def par_o_impar(num):
    if num % 2 == 0:
        return "par"
    else:
        return "impar"
    
numero = int(input("Ingresa el numero: "))
resultado = par_o_impar(numero)
print("El numero", numero, "es", resultado)