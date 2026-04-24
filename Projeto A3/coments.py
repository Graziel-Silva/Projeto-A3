import math

def ler_numero(msg):
    return float(input(msg).replace(",", "."))

while True:
    print("\n CALCULADORA GEOMÉTRICA")
    print("1 - Figuras 2D")
    print("2 - Figuras 3D")
    print("0 - Sair")
    op = input("Escolha uma opção: ")

    match op:
        case "0":
            print("Encerrando...")
            break

        case "1":
            print("\n FIGURAS 2D")
            print("1 - Quadrado")
            print("2 - Círculo")
            print("3 - Triângulo")
            print("4 - Pentágono")
            print("5 - Retângulo")
            print("6 - Losango")
            print("7 - Trapézio")
            print("8 - Hexágono")
            print("9 - Heptágono")
            print("10 - Octógono")
            print("0 - Voltar")
            op2 = input("Escolha uma figura: ")

            match op2:
                case "0":
                    continue

                case "1":
                    lado = ler_numero("Lado: ")
                    area = lado ** 2
                    perimetro = 4 * lado
                    print(f"Área: {area:.2f}")
                    print(f"Perímetro: {perimetro:.2f}")
                    print("Volume: Não possui")

                case "2":
                    raio = ler_numero("Raio: ")
                    area = math.pi * raio ** 2
                    perimetro = 2 * math.pi * raio
                    print(f"Área: {area:.2f}")
                    print(f"Perímetro: {perimetro:.2f}")
                    print("Volume: Não possui")

                case "3":
                    base = ler_numero("Base: ")
                    altura = ler_numero("Altura: ")
                    lado1 = ler_numero("Lado 1: ")
                    lado2 = ler_numero("Lado 2: ")
                    lado3 = ler_numero("Lado 3: ")
                    area = (base * altura) / 2
                    perimetro = lado1 + lado2 + lado3
                    print(f"Área: {area:.2f}")
                    print(f"Perímetro: {perimetro:.2f}")
                    print("Volume: Não possui")

                case "4":
                    lado = ler_numero("Lado: ")
                    area = (math.sqrt(25 + 10 * math.sqrt(5)) / 4) * lado ** 2
                    perimetro = 5 * lado
                    print(f"Área: {area:.2f}")
                    print(f"Perímetro: {perimetro:.2f}")
                    print("Volume: Não possui")

                case "5":
                    base = ler_numero("Base: ")
                    altura = ler_numero("Altura: ")
                    area = base * altura
                    perimetro = 2 * (base + altura)
                    print(f"Área: {area:.2f}")
                    print(f"Perímetro: {perimetro:.2f}")
                    print("Volume: Não possui")

                case "6":
                    D = ler_numero("Diagonal maior: ")
                    d = ler_numero("Diagonal menor: ")
                    lado = ler_numero("Lado: ")
                    area = (D * d) / 2
                    perimetro = 4 * lado
                    print(f"Área: {area:.2f}")
                    print(f"Perímetro: {perimetro:.2f}")
                    print("Volume: Não possui")

                case "7":
                    B = ler_numero("Base maior: ")
                    b = ler_numero("Base menor: ")
                    h = ler_numero("Altura: ")
                    area = ((B + b) * h) / 2
                    print(f"Área: {area:.2f}")
                    print("Volume: Não possui")

                case "8":
                    lado = ler_numero("Lado: ")
                    area = (3 * (3 ** 0.5) * lado ** 2) / 2
                    perimetro = 6 * lado
                    print(f"Área: {area:.2f}")
                    print(f"Perímetro: {perimetro:.2f}")
                    print("Volume: Não possui")

                case "9":
                    lado = ler_numero("Lado: ")
                    perimetro = 7 * lado
                    print(f"Perímetro: {perimetro:.2f}")
                    print("Volume: Não possui")

                case "10":
                    lado = ler_numero("Lado: ")
                    area = 2 * (1 + 2 ** 0.5) * lado ** 2
                    perimetro = 8 * lado
                    print(f"Área: {area:.2f}")
                    print(f"Perímetro: {perimetro:.2f}")
                    print("Volume: Não possui")

                case _:
                    print("Opção inválida!")

        case "2":
            print("\n FIGURAS 3D")
            print("1 - Cubo")
            print("2 - Pirâmide")
            print("3 - Cilindro")
            print("4 - Esfera")
            print("5 - Cone")
            print("6 - Paralelepípedo")
            print("0 - Voltar")
            op2 = input("Escolha uma figura: ")

            match op2:
                case "0":
                    continue

                case "1":
                    lado = ler_numero("Lado: ")
                    volume = lado ** 3
                    area_total = 6 * (lado ** 2)
                    perimetro = 12 * lado
                    print(f"Volume: {volume:.2f}")
                    print(f"Área total: {area_total:.2f}")
                    print(f"Perímetro (arestas): {perimetro:.2f}")

                case "2":
                    lado = ler_numero("Lado da base: ")
                    altura = ler_numero("Altura: ")
                    apotema = ler_numero("Apótema: ")
                    area_base = lado ** 2
                    area_lateral = 2 * lado * apotema
                    area_total = area_base + area_lateral
                    volume = (1/3) * area_base * altura
                    print(f"Área da base: {area_base:.2f}")
                    print(f"Área lateral: {area_lateral:.2f}")
                    print(f"Área total: {area_total:.2f}")
                    print(f"Volume: {volume:.2f}")

                case "3":
                    raio = ler_numero("Raio: ")
                    altura = ler_numero("Altura: ")
                    volume = math.pi * raio ** 2 * altura
                    area_total = 2 * math.pi * raio * (raio + altura)
                    print(f"Volume: {volume:.2f}")
                    print(f"Área total: {area_total:.2f}")

                case "4":
                    raio = ler_numero("Raio: ")
                    volume = (4/3) * math.pi * raio ** 3
                    area_total = 4 * math.pi * raio ** 2
                    print(f"Volume: {volume:.2f}")
                    print(f"Área total: {area_total:.2f}")

                case "5":
                    raio = ler_numero("Raio: ")
                    altura = ler_numero("Altura: ")
                    geratriz = (raio ** 2 + altura ** 2) ** 0.5
                    volume = (1/3) * math.pi * raio ** 2 * altura
                    area_total = math.pi * raio * (raio + geratriz)
                    print(f"Volume: {volume:.2f}")
                    print(f"Área total: {area_total:.2f}")

                case "6":
                    a = ler_numero("Comprimento: ")
                    b = ler_numero("Largura: ")
                    c = ler_numero("Altura: ")
                    volume = a * b * c
                    area_total = 2 * (a*b + b*c + a*c)
                    print(f"Volume: {volume:.2f}")
                    print(f"Área total: {area_total:.2f}")

                case _:
                    print("Opção inválida!")

        case _:
            print("Opção inválida!")