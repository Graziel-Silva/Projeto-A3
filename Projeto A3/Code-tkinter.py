import tkinter as tk
from tkinter import messagebox
import math

# ==========================
# CORES, TENHO QUE VER SE TODOS IRÂO GOSTAR DAS CORES, MAS VOU DEIXAR ESSAS AQUI POR ENQUANTO, DEPOIS VEJO SE MUDO OU NÃO
# ==========================
FUNDO = "#1e1e2f"
TEXTO = "#ffffff"
BOTAO_2D = "#3498db"
BOTAO_3D = "#9b59b6"
VERDE = "#00c853"

# ==========================
# 15 FIGURAS EM 2D E 3D
# ==========================
FIGURAS_2D = [
    ("Quadrado",   ["Lado"]),
    ("Retângulo",  ["Base", "Altura"]),
    ("Triângulo",  ["Base", "Altura"]),
    ("Círculo",    ["Raio"]),
    ("Losango",    ["Diagonal Maior", "Diagonal Menor"]),
    ("Trapézio",   ["Base Maior", "Base Menor", "Altura"]),
    ("Pentágono",  ["Lado"]),
    ("Hexágono",   ["Lado"]),
    ("Heptágono",  ["Lado"]),
    ("Octógono",   ["Lado"]),
]

FIGURAS_3D = [
    ("Cubo",           ["Lado"]),
    ("Esfera",         ["Raio"]),
    ("Cilindro",       ["Raio", "Altura"]),
    ("Cone",           ["Raio", "Altura"]),
    ("Pirâmide",       ["Base", "Altura"]),
    ("Prisma",         ["Base", "Altura", "Apótema"]),
    ("Paralelepípedo", ["Comprimento", "Largura", "Altura"]),
]

# ==========================
# JANELA DE DEPURAÇÃO
# ==========================
janela = tk.Tk()
janela.title("Calculadora Geométrica A3")
janela.geometry("800x850")
janela.configure(bg=FUNDO)
janela.resizable(False, False)

# ==========================
# VARIÁVEIS GLOBAIS 
# ==========================
figura_atual = ""
campos = []
entradas = []
labels = []

# ==========================
# TÍTULO, VAI TER QUE SER ESSE AQUI, MAS VOU DEIXAR ESSE COMENTÁRIO PARA ME LEMBRAR DE DEIXAR O TÍTULO AQUI NO MEIO DO CÓDIGO, PORQUE SE EU COLOCAR ANTES DOS BOTÕES FICA MUITO FEIO, ENTÃO VOU DEIXAR ESSE COMENTÁRIO PARA ME LEMBRAR DE COLOCAR O TÍTULO AQUI NO MEIO DO CÓDIGO
# ==========================
titulo = tk.Label(
    janela,
    text="Calculadora Geométrica A3",
    bg=FUNDO,
    fg=TEXTO,
    font=("Arial", 22, "bold")
)
titulo.pack(pady=15)

# ==========================
# FRAME DOS BOTÕES (com scroll)
# ==========================
frame_externo = tk.Frame(janela, bg=FUNDO)
frame_externo.pack()

frame_botoes = tk.Frame(frame_externo, bg=FUNDO)
frame_botoes.pack()

# ==========================
# FUNÇÃO CONFIGURAR
# ==========================
def configurar(figura, lista_campos):

    global figura_atual, campos

    figura_atual = figura
    campos = lista_campos

    for i in range(5):

        entradas[i].delete(0, tk.END)

        if i < len(lista_campos):

            labels[i].config(text=lista_campos[i] + ":")

            entradas[i].config(state="normal")

        else:

            labels[i].config(text="")

            entradas[i].config(state="disabled")

    resultado.config(text="")

# ==========================
# ESSE AQUI SÂO OS BOTÕES EM 2D PARTE DE WESLEY
# ==========================
frame_2d = tk.Frame(frame_botoes, bg=FUNDO)
frame_2d.grid(row=0, column=0, padx=20, sticky="n")

tk.Label(
    frame_2d,
    text="Figuras 2D",
    bg=FUNDO,
    fg=BOTAO_2D,
    font=("Arial", 14, "bold")
).pack(pady=5)

for nome, lista in FIGURAS_2D:

    tk.Button(
        frame_2d,
        text=nome,
        width=18,
        bg=BOTAO_2D,
        fg="white",
        relief="flat",
        cursor="hand2",
        command=lambda n=nome, l=lista: configurar(n, l)
    ).pack(pady=3)

# ==========================
# ESSA PARTE AQUI IREI FAZER OS BOTÕES EM 3D, MAS AINDA NÃO FIZ, ENTÃO VOU DEIXAR ESSE COMENTÁRIO PARA ME LEMBRAR DE FAZER DEPOIS
# ==========================
frame_3d = tk.Frame(frame_botoes, bg=FUNDO)
frame_3d.grid(row=0, column=1, padx=20, sticky="n")

tk.Label(
    frame_3d,
    text="Figuras 3D",
    bg=FUNDO,
    fg=BOTAO_3D,
    font=("Arial", 14, "bold")
).pack(pady=5)

for nome, lista in FIGURAS_3D:

    tk.Button(
        frame_3d,
        text=nome,
        width=18,
        bg=BOTAO_3D,
        fg="white",
        relief="flat",
        cursor="hand2",
        command=lambda n=nome, l=lista: configurar(n, l)
    ).pack(pady=3)

# ==========================
# VISU DO CAMPOS
# ==========================
frame_campos = tk.Frame(janela, bg=FUNDO)
frame_campos.pack(pady=20)

for i in range(5):

    lbl = tk.Label(
        frame_campos,
        text="",
        bg=FUNDO,
        fg=TEXTO,
        font=("Arial", 11),
        width=20,
        anchor="e"
    )

    lbl.grid(row=i, column=0, pady=5, padx=5)

    ent = tk.Entry(
        frame_campos,
        width=20,
        font=("Arial", 11),
        state="disabled"
    )

    ent.grid(row=i, column=1, pady=5)

    labels.append(lbl)
    entradas.append(ent)

# ==========================
# FUNÇÃO CALCULAR, COM DEFEITO NO CALCULO, MAS CREIO QUE CONSEGUI RESOLVER, ENTÃO VOU DEIXAR ESSE COMENTÁRIO PARA ME LEMBRAR DE VER SE O CALCULO ESTÁ CERTO DEPOIS, PORQUE EU FIZ MUITAS FIGURAS E MUITAS FÓRMULAS, ENTÃO PODE SER QUE TENHA ALGUM ERRO EM ALGUMA FÓRMULA, ENTÃO VOU DEIXAR ESSE COMENTÁRIO PARA ME LEMBRAR DE VER SE O CALCULO ESTÁ CERTO DEPOIS
# ==========================
def calcular():

    if figura_atual == "":

        messagebox.showwarning(
            "Aviso",
            "Escolha uma figura."
        )

        return

    valores = []

    try:

        for i in range(len(campos)):

            valor = entradas[i].get().replace(",", ".")

            valores.append(float(valor))

    except:

        messagebox.showerror(
            "Erro",
            "Digite apenas números válidos."
        )

        return

    # ======================
    # QUADRADO
    # ======================
    if figura_atual == "Quadrado":

        area = valores[0] ** 2
        perimetro = 4 * valores[0]

        texto = (
            f"Área = {area:.2f}\n"
            f"Perímetro = {perimetro:.2f}"
        )

    # ======================
    # CÍRCULO
    # ======================
    elif figura_atual == "Círculo":

        area = math.pi * valores[0] ** 2
        comprimento = 2 * math.pi * valores[0]

        texto = (
            f"Área = {area:.2f}\n"
            f"Comprimento = {comprimento:.2f}"
        )

    # ======================
    # RETÂNGULO
    # ======================
    elif figura_atual == "Retângulo":

        area = valores[0] * valores[1]
        perimetro = 2 * (valores[0] + valores[1])

        texto = (
            f"Área = {area:.2f}\n"
            f"Perímetro = {perimetro:.2f}"
        )

    # ======================
    # TRIÂNGULO
    # ======================
    elif figura_atual == "Triângulo":

        area = (valores[0] * valores[1]) / 2

        texto = f"Área = {area:.2f}"

    # ======================
    # LOSANGO
    # ======================
    elif figura_atual == "Losango":

        # d1 = diagonal maior, d2 = diagonal menor
        d1, d2 = valores[0], valores[1]
        area = (d1 * d2) / 2
        lado = math.sqrt((d1 / 2) ** 2 + (d2 / 2) ** 2)
        perimetro = 4 * lado

        texto = (
            f"Área = {area:.2f}\n"
            f"Perímetro = {perimetro:.2f}"
        )

    # ======================
    # TRAPÉZIO
    # ======================
    elif figura_atual == "Trapézio":

        b_maior, b_menor, h = valores[0], valores[1], valores[2]
        area = ((b_maior + b_menor) * h) / 2

        texto = f"Área = {area:.2f}"

    # ======================
    # PENTÁGONO
    # ======================
    elif figura_atual == "Pentágono":

        l = valores[0]
        area = (l ** 2 * math.sqrt(25 + 10 * math.sqrt(5))) / 4
        perimetro = 5 * l

        texto = (
            f"Área = {area:.2f}\n"
            f"Perímetro = {perimetro:.2f}"
        )

    # ======================
    # HEXÁGONO
    # ======================
    elif figura_atual == "Hexágono":

        l = valores[0]
        area = (3 * math.sqrt(3) / 2) * l ** 2
        perimetro = 6 * l

        texto = (
            f"Área = {area:.2f}\n"
            f"Perímetro = {perimetro:.2f}"
        )

    # ======================
    # HEPTÁGONO
    # ======================
    elif figura_atual == "Heptágono":

        l = valores[0]
        n = 7
        area = (n * l ** 2) / (4 * math.tan(math.pi / n))
        perimetro = n * l

        texto = (
            f"Área = {area:.2f}\n"
            f"Perímetro = {perimetro:.2f}"
        )

    # ======================
    # OCTÓGONO
    # ======================
    elif figura_atual == "Octógono":

        l = valores[0]
        area = 2 * (1 + math.sqrt(2)) * l ** 2
        perimetro = 8 * l

        texto = (
            f"Área = {area:.2f}\n"
            f"Perímetro = {perimetro:.2f}"
        )

    # ======================
    # CUBO
    # ======================
    elif figura_atual == "Cubo":

        volume = valores[0] ** 3
        area = 6 * (valores[0] ** 2)

        texto = (
            f"Volume = {volume:.2f}\n"
            f"Área Total = {area:.2f}"
        )

    # ======================
    # ESFERA
    # ======================
    elif figura_atual == "Esfera":

        volume = (4 / 3) * math.pi * valores[0] ** 3
        area = 4 * math.pi * valores[0] ** 2

        texto = (
            f"Volume = {volume:.2f}\n"
            f"Área Total = {area:.2f}"
        )

    # ======================
    # CILINDRO
    # ======================
    elif figura_atual == "Cilindro":

        r, h = valores[0], valores[1]
        volume = math.pi * r ** 2 * h
        area = 2 * math.pi * r * (r + h)

        texto = (
            f"Volume = {volume:.2f}\n"
            f"Área Total = {area:.2f}"
        )

    # ======================
    # CONE
    # ======================
    elif figura_atual == "Cone":

        r, h = valores[0], valores[1]
        geratriz = math.sqrt(r ** 2 + h ** 2)
        volume = (1 / 3) * math.pi * r ** 2 * h
        area = math.pi * r * (r + geratriz)

        texto = (
            f"Volume = {volume:.2f}\n"
            f"Área Total = {area:.2f}"
        )

    # ======================
    # PIRÂMIDE (base quadrada)
    # ======================
    elif figura_atual == "Pirâmide":

        base, h = valores[0], valores[1]
        volume = (base ** 2 * h) / 3
        apotema_lateral = math.sqrt((base / 2) ** 2 + h ** 2)
        area_base = base ** 2
        area_lateral = 4 * (base * apotema_lateral / 2)
        area_total = area_base + area_lateral

        texto = (
            f"Volume = {volume:.2f}\n"
            f"Área Total = {area_total:.2f}"
        )

    # ======================
    # PRISMA (base triangular equilátera)
    # ======================
    elif figura_atual == "Prisma":

        base, h, apotema = valores[0], valores[1], valores[2]
        area_base = (base * apotema) / 2
        perimetro_base = 3 * base
        volume = area_base * h
        area_total = 2 * area_base + perimetro_base * h

        texto = (
            f"Volume = {volume:.2f}\n"
            f"Área Total = {area_total:.2f}"
        )

    # ======================
    # PARALELEPÍPEDO
    # ======================
    elif figura_atual == "Paralelepípedo":

        c, l, h = valores[0], valores[1], valores[2]
        volume = c * l * h
        area = 2 * (c * l + c * h + l * h)
        diagonal = math.sqrt(c ** 2 + l ** 2 + h ** 2)

        texto = (
            f"Volume = {volume:.2f}\n"
            f"Área Total = {area:.2f}\n"
            f"Diagonal = {diagonal:.2f}"
        )

    else:
        texto = "Figura não reconhecida."

    resultado.config(text=texto)

# ==========================
# BOTÃO CALCULAR
# ==========================
botao_calcular = tk.Button(
    janela,
    text="CALCULAR",
    bg=VERDE,
    fg="white",
    font=("Arial", 13, "bold"),
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2",
    command=calcular
)

botao_calcular.pack(pady=15)

# ==========================
# RESULTADO 
# ==========================
resultado = tk.Label(
    janela,
    text="",
    bg=FUNDO,
    fg="#00ffcc",
    font=("Arial", 14, "bold")
)

resultado.pack(pady=10)

# ==========================
# RODAPÉ
# ==========================
rodape = tk.Label(
    janela,
    text="Projeto Faculdade - Tkinter Python",
    bg=FUNDO,
    fg="#777799",
    font=("Arial", 9)
)

rodape.pack(side="bottom", pady=10)

# ==========================
# LOOP MORY
# ==========================
janela.mainloop()
