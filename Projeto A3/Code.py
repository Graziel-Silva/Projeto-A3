import math

def ler_numero(msg):
    return float(input(msg).replace(",", "."))

  for x in range(10):
     print("\n CALCULADORA GEOMÉTRICA")
     print("1 - Quadrado")
     print("2 - Circulo")
     print("3 - Triangulo")
     print("4 - Pirâmide")
     print("5 - Pentágono")
     print("6- Retângulo")
     print("7 - Cubo")
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
           area = math.pi * raio**2
           perimetro = 2 * math.pi * raio
           volume = (4/3) * math.pi * raio**3  # esfera

           print("Área: {area:.2f}")
           print("Perímetro (circunferência): {perimetro:.2f}")
           print("Volume (esfera): {volume:.2f}") 
          
      case 3:
            base = ler_numero("Base: ")
            altura = ler_numero("Altura: ")
            lado1 = ler_numero("Lado 1: ")
            lado2 = ler_numero("Lado 2: ")
            lado3 = ler_numero("Lado 3: ")

            area = (base * altura) / 2
            perimetro = lado1 + lado2 + lado3

            print("Área:", area)
            print("Perímetro:", perimetro)
            print("Volume: Não possui")

    
      case 4 :
           lado = ler_numero("Digite o lado da base: ")
           altura = ler_numero("Digite a altura da pirâmide: ")
           apotema = ler_numero("Digite o apótema: ")

           area_base = lado ** 2
           area_lateral = 2 * lado * apotema
           area_total = area_base + area_lateral
           volume = (1/3) * area_base * altura

           print("Área da base: {area_base:.2f}")
           print("Área lateral: {area_lateral:.2f}")
           print("Área total: {area_total:.2f}")
           print("Volume: {volume:.2f}")
          
      case 5: 
            lado = ler_numero("Lado: ")
            perimetro = 5 * lado

            print("Perímetro:", perimetro)
            print("Área: (fórmula mais complexa)")
            print("Volume: Não possui")

      case 6:
           base = ler_numero("Digite a base: ")
           altura = ler_numero("Digite a altura: ")

           area = base * altura
           perimetro = 2 * (base + altura)

           print("Área: {area:.2f}")
           print("Perímetro: {perimetro:.2f}")

      case 7:
           lado = ler_numero("Digite o lado do cubo: ")

           volume = lado ** 3
           area_total = 6 * (lado ** 2)
           perimetro = 12 * lado

           print("Volume: {volume:.2f}")
           print("Área total: {area_total:.2f}")
           print("Perímetro (arestas): {perimetro:.2f}")

      case 9:
          raio = ler_numero("Digite o raio: ")
          altura = ler_numero("Digite a altura: ")

          volume = (1/3) * math.pi * raio**2 * altura
          area_lateral = math.pi * raio * geratriz
          area_total = math.pi * raio * (raio + geratriz)

          print("Volume: {volume:.2f}")
          print("Área lateral: {area_lateral:.2f}")
          print("Área total: {area_total:.2f}")

      case _:
            print("Opção inválida!")

        
