import math

def ler_numero(msg):
    return float(input(msg).replace(",", "."))

  for x in range(7):
     print("\n CALCULADORA GEOMÉTRICA")
     print("1 - Quadrado")
     print("2 - Circulo")
     print("3 - Triangulo")
     print("4 - Pirâmide")
     print("5 - Pentágono")
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
           print("Volume: Não possui")
    
      case 4 :
            base = ler_numero("Área da base: ")
            altura = ler_numero("Altura: ")

            volume = (1/3) * base * altura

            print("Volume da pirâmide:", volume)

      case "5": 
            lado = ler_numero("Lado: ")
            perimetro = 5 * lado

            print("Perímetro:", perimetro)
            print("Área: (fórmula mais complexa)")
            print("Volume: Não possui")

      case _:
            print("Opção inválida!")

        
