import math

  def ler_numero(msg):
    return float(input(msg).replace(",", "."))

  for x in range(4):
     print("\n CALCULADORA GEOMÉTRICA")
     print("1 - Quadrado")
     print("2 - Circulo")
     print("3 - Triangulo")

    op = input("Escolha uma opçao")

   match op:

      case 1:
           lado = ler_numero("Lado:")
           area = lado * lado
           perimetro = 4 * lado
           volume = lado ** 3

           print("Área:", area)
           print("Perímetro:", perimetro)
           print("Volume:", volume)
