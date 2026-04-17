import math

def ler_numero(msg):
    return float(input(msg).replace(",", "."))

  for x in range(4):
     print("\n CALCULADORA GEOMÉTRICA")
     print("1 - Quadrado")
     print("2 - Circulo")
     print("3 - Triangulo")

 op = input("Escolha uma opção")

   match op:

      case 1:
           lado = ler_numero("Lado:")
           area = lado * lado
           perimetro = 4 * lado
           volume = lado ** 3

           print("Área:", area)
           print("Perímetro:", perimetro)
           print("Volume:", volume)
        
      case 2 :
          raio = ler_numero("Raio: ")
          print("Perímetro:", 2 * math.pi * raio)
          print("Volume:", (4/3) * math.pi * raio**3)

      case 3:
           base = ler_numero("Base: ")
           L1 = ler_numero("Lado 1: ")
           L2 = ler_numero("Lado 2: ")

           print("Área:", (base * altura) / 2)
           print("Perímetro:", l1 + l2 + l3)
           rint("Volume: Não possui")

        
