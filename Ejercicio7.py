def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

base = float(input("Ingresa el area del triangulo: "))
altura = float(input("Ingresa la altura del triangulo: "))
area = area_triangulo(base, altura)
print("El area del triangulo es: ", area)