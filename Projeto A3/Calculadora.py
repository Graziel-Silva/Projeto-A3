import tkinter as tk
from tkinter import font as tkfont
import math

#  CORES
C = {
    "bg":      "#0a0f1e",
    "sidebar": "#0d1526",
    "card":    "#111d35",
    "card2":   "#0f1a30",
    "border":  "#1e3a5f",
    "blue":    "#38bdf8",
    "purple":  "#8b5cf6",
    "green":   "#22c55e",
    "cyan":    "#06b6d4",
    "text":    "#e2e8f0",
    "muted":   "#64748b",
    "dim":     "#94a3b8",
    "white":   "#ffffff",
    "error":   "#ef4444",
    "warning": "#f59e0b",
}

FIGURAS_2D = [
    ("Quadrado",       ["Lado"],                               "Quatro lados iguais e ângulos retos.",        "2D"),
    ("Retângulo",      ["Base", "Altura"],                    "Lados opostos iguais, ângulos de 90°.",       "2D"),
    ("Triângulo",      ["Base", "Altura"],                    "Polígono de três lados e três vértices.",      "2D"),
    ("Círculo",        ["Raio"],                               "Todos os pontos equidistantes do centro.",     "2D"),
    ("Losango",        ["Diagonal Maior", "Diagonal Menor"],   "Quadrilátero com quatro lados iguais.",        "2D"),
    ("Trapézio",       ["Base Maior", "Base Menor", "Altura"], "Um par de lados paralelos (bases).",          "2D"),
    ("Pentágono",      ["Lado"],                               "Polígono regular de cinco lados iguais.",      "2D"),
    ("Hexágono",       ["Lado"],                               "Polígono regular de seis lados iguais.",       "2D"),
    ("Heptágono",      ["Lado"],                               "Polígono regular de sete lados iguais.",       "2D"),
    ("Octógono",       ["Lado"],                               "Polígono regular de oito lados iguais.",       "2D"),
]

FIGURAS_3D = [
    ("Cubo",           ["Lado"],                               "Sólido com seis faces quadradas iguais.",      "3D"),
    ("Esfera",         ["Raio"],                               "Superfície equidistante do centro em 3D.",     "3D"),
    ("Cilindro",       ["Raio", "Altura"],                    "Sólido com duas bases circulares paralelas.",  "3D"),
    ("Cone",           ["Raio", "Altura"],                    "Base circular com vértice oposto apontado.",   "3D"),
    ("Pirâmide",       ["Base", "Altura"],                    "Base quadrada com faces triangulares.",         "3D"),
    ("Prisma",         ["Base", "Altura", "Apótema"],         "Prisma triangular com bases congruentes.",     "3D"),
    ("Paralelepípedo", ["Comprimento", "Largura", "Altura"],  "Sólido com seis faces retangulares.",          "3D"),
]

ICONES = {
    "Quadrado":"□","Retângulo":"▬","Triângulo":"△","Círculo":"○",
    "Losango":"◇","Trapézio":"⌂","Pentágono":"⬠","Hexágono":"⬡",
    "Heptágono":"⬡","Octógono":"⬡","Cubo":"⬛","Esfera":"●",
    "Cilindro":"⊙","Cone":"▽","Pirâmide":"△","Prisma":"◨",
    "Paralelepípedo":"▦",
}

FORMULAS = {
    "Quadrado":       "A = L²   |   P = 4L",
    "Retângulo":      "A = b×h   |   P = 2(b+h)",
    "Triângulo":      "A = (b×h) / 2",
    "Círculo":        "A = πr²   |   C = 2πr",
    "Losango":        "A = (D×d) / 2",
    "Trapézio":       "A = (B+b)×h / 2",
    "Pentágono":      "A = L²√(25+10√5) / 4",
    "Hexágono":       "A = 3√3/2 × L²",
    "Heptágono":      "A = 7L² / (4·tan(π/7))",
    "Octógono":       "A = 2(1+√2) × L²",
    "Cubo":           "V = L³   |   A = 6L²",
    "Esfera":         "V = 4πr³/3   |   A = 4πr²",
    "Cilindro":       "V = πr²h   |   A = 2πr(r+h)",
    "Cone":           "V = πr²h/3   |   A = πr(r+g)",
    "Pirâmide":       "V = B²h / 3",
    "Prisma":         "V = A_base × h",
    "Paralelepípedo": "V = c × l × h",
}

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora Geométrica")
        self.root.geometry("1050x680")
        self.root.configure(bg=C["bg"])
        self.root.resizable(True, True)
        self.root.minsize(880, 580)

        self.figura_atual = None
        self.entradas     = []
        self.botoes_sb    = {}
        self._cvs_sb      = None  

        self._fontes()
        self._build()
        self._selecionar(FIGURAS_2D[0])

    def _fontes(self):
        self.fT  = tkfont.Font(family="Segoe UI", size=16, weight="bold")
        self.fS  = tkfont.Font(family="Segoe UI", size=11, weight="bold")
        self.fB  = tkfont.Font(family="Segoe UI", size=10)
        self.fBb = tkfont.Font(family="Segoe UI", size=10, weight="bold")
        self.fSm = tkfont.Font(family="Segoe UI", size=9)
        self.fCt = tkfont.Font(family="Segoe UI", size=8,  weight="bold")
        self.fM  = tkfont.Font(family="Consolas",  size=11, weight="bold")
        self.fR  = tkfont.Font(family="Consolas",  size=15, weight="bold")
        self.fCk = tkfont.Font(family="Consolas",  size=12, weight="bold")
        self.fIc = tkfont.Font(family="Segoe UI",  size=17)

    def _build(self):
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        self._sidebar()
        self._main()
        
    def _sidebar(self):
        sb = tk.Frame(self.root, bg=C["sidebar"], width=215)
        sb.grid(row=0, column=0, sticky="nsew")
        sb.grid_propagate(False)
        sb.columnconfigure(0, weight=1)
        sb.rowconfigure(1, weight=1)

        # --- Logo ---
        lf = tk.Frame(sb, bg=C["sidebar"])
        lf.grid(row=0, column=0, pady=(14,0), padx=12, sticky="w")
        tk.Label(lf, text="◈ Formas:", font=self.fS, bg=C["sidebar"], fg=C["blue"]).pack(side="left")
        tk.Frame(sb, bg=C["border"], height=1).grid(row=0, column=0, sticky="sew", padx=8, pady=(42,0))

        # --- Área scrollável ---
        scroll_area = tk.Frame(sb, bg=C["sidebar"])
        scroll_area.grid(row=1, column=0, sticky="nsew")
        scroll_area.rowconfigure(0, weight=1)
        scroll_area.columnconfigure(0, weight=1)

        self._cvs_sb = tk.Canvas(
            scroll_area, bg=C["sidebar"], bd=0,
            highlightthickness=0, width=213
        )
        vsb = tk.Scrollbar(scroll_area, orient="vertical", command=self._cvs_sb.yview)
        self._cvs_sb.configure(yscrollcommand=vsb.set)

        self._cvs_sb.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")

        self.scroll_f = tk.Frame(self._cvs_sb, bg=C["sidebar"])
        self._win_id  = self._cvs_sb.create_window((0, 0), window=self.scroll_f, anchor="nw")

        self.scroll_f.bind("<Configure>", self._on_scroll_frame_configure)
        self._cvs_sb.bind("<Configure>",  self._on_canvas_configure)

        self.root.bind_all("<MouseWheel>", self._on_mousewheel)

        # --- Preencher lista ---
        self._cat(self.scroll_f, "▸  FIGURAS 2D", C["blue"])
        for f in FIGURAS_2D:
            self._btn_sb(f, C["blue"], "#1e3a5f")

        tk.Frame(self.scroll_f, bg=C["border"], height=1).pack(fill="x", padx=10, pady=5)

        self._cat(self.scroll_f, "▸  FIGURAS 3D", C["purple"])
        for f in FIGURAS_3D:
            self._btn_sb(f, C["purple"], "#2d1b69")


    def _on_scroll_frame_configure(self, event):
        self._cvs_sb.configure(scrollregion=self._cvs_sb.bbox("all"))

    def _on_canvas_configure(self, event):
        self._cvs_sb.itemconfig(self._win_id, width=event.width)

    def _on_mousewheel(self, event):
        try:
            widget = event.widget
            w = widget
            while w is not None:
                if w is self._cvs_sb or w is self.scroll_f:
                    self._cvs_sb.yview_scroll(-1 * (event.delta // 120), "units")
                    return
                try:
                    w = w.master
                except Exception:
                    break
        except Exception:
            pass

    def _cat(self, parent, text, color):
        tk.Label(parent, text=text, font=self.fCt, bg=C["sidebar"],
                 fg=color, anchor="w", padx=12).pack(fill="x", pady=(7, 2))

    def _btn_sb(self, fig, cor, hover):
        nome = fig[0]
        fr = tk.Frame(self.scroll_f, bg=C["sidebar"], cursor="hand2")
        fr.pack(fill="x", padx=6, pady=1)

        barra = tk.Frame(fr, bg=C["sidebar"], width=3)
        barra.pack(side="left", fill="y")

        inner = tk.Frame(fr, bg=C["sidebar"])
        inner.pack(side="left", fill="x", expand=True, padx=4, pady=3)

        ic = tk.Label(inner, text=ICONES.get(nome, "◆"), font=self.fIc,
                      bg=C["sidebar"], fg=cor, width=3)
        ic.pack(side="left")

        tf = tk.Frame(inner, bg=C["sidebar"])
        tf.pack(side="left", padx=4)

        nl = tk.Label(tf, text=nome,   font=self.fBb, bg=C["sidebar"], fg=C["text"], anchor="w")
        nl.pack(anchor="w")
        tl = tk.Label(tf, text=fig[3], font=self.fCt,  bg=C["sidebar"], fg=cor,      anchor="w")
        tl.pack(anchor="w")

        all_w = [fr, inner, ic, tf, nl, tl]

        def enter(e):
            if self.figura_atual and self.figura_atual[0] != nome:
                for w in all_w:
                    w.config(bg=hover)
        def leave(e):
            if self.figura_atual and self.figura_atual[0] != nome:
                for w in all_w:
                    w.config(bg=C["sidebar"])
        def click(e, f=fig):
            self._selecionar(f)

        for w in [fr] + all_w:
            w.bind("<Enter>",    enter)
            w.bind("<Leave>",    leave)
            w.bind("<Button-1>", click)
            w.bind("<MouseWheel>", self._on_mousewheel)

        self.botoes_sb[nome] = {
            "all": all_w, "barra": barra,
            "cor": cor, "hover": hover
        }

    def _sbtn(self, parent, text, color, cmd):
        b = tk.Label(parent, text=text, font=self.fSm, bg=C["sidebar"],
                     fg=color, anchor="w", padx=10, pady=4, cursor="hand2")
        b.bind("<Button-1>", lambda e: cmd())
        b.bind("<Enter>",    lambda e: b.config(bg=C["border"]))
        b.bind("<Leave>",    lambda e: b.config(bg=C["sidebar"]))
        return b

    # ─── Inicio ───────────────────────────────
    def _main(self):
        main = tk.Frame(self.root, bg=C["bg"])
        main.grid(row=0, column=1, sticky="nsew")
        main.columnconfigure(0, weight=1)
        main.rowconfigure(1, weight=1)

        self._header(main)
        self._content(main)
        self._statusbar(main)

    def _header(self, p):
        h = tk.Frame(p, bg=C["sidebar"], height=54)
        h.grid(row=0, column=0, sticky="ew")
        h.grid_propagate(False)
        h.columnconfigure(1, weight=1)

        left = tk.Frame(h, bg=C["sidebar"])
        left.grid(row=0, column=0, padx=18, pady=8, sticky="w")

        self.h_ic = tk.Label(left, text="○", font=self.fIc, bg=C["sidebar"], fg=C["blue"])
        self.h_ic.pack(side="left", padx=(0, 8))
        self.h_nm = tk.Label(left, text="Selecione uma figura", font=self.fT,
                             bg=C["sidebar"], fg=C["white"])
        self.h_nm.pack(side="left")
        self.h_tg = tk.Label(left, text="", font=self.fCt,
                             bg=C["blue"], fg=C["white"], padx=6, pady=2)
        self.h_tg.pack(side="left", padx=8)

        right = tk.Frame(h, bg=C["sidebar"])
        right.grid(row=0, column=2, padx=14, pady=8, sticky="e")
        self.ck = tk.Label(right, text="00:00:00", font=self.fCk,
                           bg=C["sidebar"], fg=C["muted"])
        self.ck.pack(side="right", padx=6)


        self.h_line = tk.Frame(p, bg=C["blue"], height=2)
        self.h_line.grid(row=0, column=0, sticky="sew")

    def _content(self, p):
        c = tk.Frame(p, bg=C["bg"])
        c.grid(row=1, column=0, sticky="nsew")
        c.columnconfigure(0, weight=2)
        c.columnconfigure(1, weight=3)
        c.rowconfigure(0, weight=1)


        left = tk.Frame(c, bg=C["bg"])
        left.grid(row=0, column=0, sticky="nsew", padx=(16, 8), pady=14)
        left.columnconfigure(0, weight=1)
        left.rowconfigure(1, weight=1)


        pc = tk.Frame(left, bg=C["card"])
        pc.grid(row=0, column=0, sticky="ew")

        self.neon_top = tk.Frame(pc, height=3, bg=C["blue"])
        self.neon_top.pack(fill="x")

        self.cvs = tk.Canvas(pc, width=240, height=165,
                             bg=C["card"], bd=0, highlightthickness=0)
        self.cvs.pack(padx=14, pady=10)

        self.desc_l = tk.Label(pc, text="Selecione uma figura.",
                               font=self.fB, bg=C["card"], fg=C["dim"],
                               wraplength=220, justify="center")
        self.desc_l.pack(pady=(0, 4))

        self.form_l = tk.Label(pc, text="", font=self.fM,
                               bg=C["card2"], fg=C["cyan"], padx=10, pady=5)
        self.form_l.pack(fill="x", padx=12, pady=(2, 12))


        rc = tk.Frame(left, bg=C["card"])
        rc.grid(row=1, column=0, sticky="nsew", pady=(10, 0))
        rc.columnconfigure(0, weight=1)

        tk.Frame(rc, height=3, bg=C["green"]).pack(fill="x")
        tk.Label(rc, text="Resultados", font=self.fS,
                 bg=C["card"], fg=C["white"]).pack(anchor="w", padx=14, pady=(10, 6))

        self.res_frame = tk.Frame(rc, bg=C["card"])
        self.res_frame.pack(fill="both", expand=True, padx=12, pady=(0, 12))

        self._limpar_res()


        right = tk.Frame(c, bg=C["bg"])
        right.grid(row=0, column=1, sticky="nsew", padx=(8, 16), pady=14)
        right.columnconfigure(0, weight=1)

        ic = tk.Frame(right, bg=C["card"])
        ic.grid(row=0, column=0, sticky="ew")
        ic.columnconfigure(0, weight=1)

        self.neon_inp = tk.Frame(ic, height=3, bg=C["purple"])
        self.neon_inp.pack(fill="x")

        tk.Label(ic, text="Parâmetros de Entrada", font=self.fS,
                 bg=C["card"], fg=C["white"]).pack(anchor="w", padx=16, pady=(12, 4))

        self.inp_frame = tk.Frame(ic, bg=C["card"])
        self.inp_frame.pack(fill="x", padx=14, pady=(4, 14))
        self.inp_frame.columnconfigure(1, weight=1)

        bf = tk.Frame(ic, bg=C["card"])
        bf.pack(fill="x", padx=14, pady=(0, 16))
        bf.columnconfigure(0, weight=1)
        bf.columnconfigure(1, weight=1)

        self._gbtn(bf, "⚡  CALCULAR", C["blue"],  "#0ea5e9", self._calcular
                   ).grid(row=0, column=0, padx=(0, 5), sticky="ew")
        self._gbtn(bf, "✕  LIMPAR",   C["card2"], C["border"], self._limpar,
                   fg=C["dim"]).grid(row=0, column=1, padx=(5, 0), sticky="ew")

    def _gbtn(self, parent, text, bg, hover, cmd, fg=None):
        if fg is None:
            fg = C["white"]
        b = tk.Label(parent, text=text, font=self.fBb, bg=bg, fg=fg,
                     pady=10, cursor="hand2", anchor="center")
        b.bind("<Button-1>", lambda e: cmd())
        b.bind("<Enter>",    lambda e: b.config(bg=hover))
        b.bind("<Leave>",    lambda e: b.config(bg=bg))
        return b

    def _statusbar(self, p):
        sb = tk.Frame(p, bg=C["sidebar"], height=26)
        sb.grid(row=2, column=0, sticky="ew")
        sb.grid_propagate(False)
        sb.columnconfigure(1, weight=1)
        tk.Label(sb, text=" ◈ GeoCalc Pro  |  Projeto Universitário",
                 font=self.fSm, bg=C["sidebar"], fg=C["muted"]
                 ).grid(row=0, column=0, sticky="w", padx=8)
        self.status_lbl = tk.Label(sb, text="Pronto", font=self.fSm,
                                   bg=C["sidebar"], fg=C["green"])
        self.status_lbl.grid(row=0, column=2, sticky="e", padx=8)

    def _selecionar(self, fig):
        nome, campos, desc, tipo = fig
        self.figura_atual = fig

        cor = C["blue"] if tipo == "2D" else C["purple"]

        for n, info in self.botoes_sb.items():
            ativo = (n == nome)
            bg = info["hover"] if ativo else C["sidebar"]
            for w in info["all"]:
                w.config(bg=bg)
            info["barra"].config(bg=info["cor"] if ativo else C["sidebar"])

        self.h_ic.config(text=ICONES.get(nome, "◆"), fg=cor)
        self.h_nm.config(text=nome)
        self.h_tg.config(text=tipo, bg=cor)
        self.neon_top.config(bg=cor)
        self.neon_inp.config(bg=cor)
        self.h_line.config(bg=cor)
        self.desc_l.config(text=desc)
        self.form_l.config(text=FORMULAS.get(nome, ""), fg=cor)

        self._desenhar(nome, cor)
        self._montar_inputs(campos, cor)
        self._limpar_res()
        self._status(f"Selecionado: {nome}")


    def _montar_inputs(self, campos, cor):
        for w in self.inp_frame.winfo_children():
            w.destroy()
        self.entradas = []

        for i, campo in enumerate(campos):
            tk.Label(self.inp_frame, text=campo, font=self.fBb,
                     bg=C["card"], fg=C["dim"], anchor="w"
                     ).grid(row=i, column=0, sticky="w", pady=6, padx=(0, 10))

            ef = tk.Frame(self.inp_frame, bg=C["border"], padx=1, pady=1)
            ef.grid(row=i, column=1, sticky="ew", pady=6)
            ef.columnconfigure(0, weight=1)

            ent = tk.Entry(ef, font=self.fM, bg=C["card2"], fg=C["muted"],
                           bd=0, insertbackground=cor, relief="flat")
            ent.grid(row=0, column=0, sticky="ew", padx=8, pady=5)
            ent.insert(0, "0")

            def fi(e, en=ent, c=cor, ef=ef):
                if en.get() == "0":
                    en.delete(0, "end")
                en.config(fg=C["white"])
                ef.config(bg=c)

            def fo(e, en=ent, ef=ef):
                if en.get() == "":
                    en.insert(0, "0")
                    en.config(fg=C["muted"])
                ef.config(bg=C["border"])

            ent.bind("<FocusIn>",  fi)
            ent.bind("<FocusOut>", fo)
            ent.bind("<Return>",   lambda e: self._calcular())
            self.entradas.append(ent)
