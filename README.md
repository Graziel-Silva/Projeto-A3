# Calculadora Geométrica - Projeto A3

Este projeto consiste no desenvolvimento de uma **Calculadora Geométrica** robusta, criada como parte da unidade curricular **Projeto A3** no âmbito acadêmico. O objetivo principal é fornecer uma ferramenta capaz de realizar cálculos precisos de área, perímetro e volume para diversas figuras geométricas planas (2D) e espaciais (3D).

## Visão Geral do Projeto

O software está sendo desenvolvido com foco na **Programação Orientada a Objetos (POO)**, garantindo que o código seja modular, escalável e de fácil manutenção. Embora a versão inicial foque na lógica matemática e estruturação das classes, o projeto final contará com uma interface gráfica amigável utilizando a biblioteca **Tkinter**, atendendo às especificações e requisitos solicitados pelo docente.

### Funcionalidades Atuais

A calculadora abrange uma ampla gama de formas geométricas, divididas em duas categorias principais conforme detalhado na tabela abaixo:

| Categoria | Figuras Suportadas | Cálculos Realizados |
| :--- | :--- | :--- |
| **Figuras 2D** | Quadrado, Círculo, Triângulo, Pentágono, Retângulo, Losango, Trapézio, Hexágono, Heptágono, Octógono | Área e Perímetro |
| **Figuras 3D** | Cubo, Pirâmide, Cilindro, Esfera, Cone, Paralelepípedo | Volume e Área Total |

## Tecnologias Utilizadas

A escolha das tecnologias reflete o compromisso com as melhores práticas de desenvolvimento de software ensinadas em sala de aula.

*   **Linguagem:** [Python](https://www.python.org/) (Versão 3.10 ou superior para suporte ao `match-case`).
*   **Paradigma:** Programação Orientada a Objetos (POO).
*   **Interface Gráfica:** [Tkinter](https://docs.python.org/3/library/tkinter.html) (Em fase de implementação).
*   **Bibliotecas Internas:** `math` para cálculos trigonométricos e constantes precisas como o Pi.

## Estrutura de Desenvolvimento

Atualmente, o código está organizado para priorizar a precisão dos cálculos matemáticos. A transição para a interface gráfica está planejada para ocorrer logo após a consolidação de toda a lógica de classes.

> "A escolha de separar a lógica de negócio (cálculos) da interface (Tkinter) permite que o projeto siga o padrão de design MVC (Model-View-Controller), facilitando a implementação da GUI sem comprometer a integridade dos cálculos geométricos."

## Como Executar (Versão CLI)

Para testar a lógica atual da calculadora via terminal, siga os passos abaixo:

1.  Certifique-se de ter o Python instalado em sua máquina.
2.  Clone o repositório:
    ```bash
    git clone https://github.com/Graziel-Silva/Projeto-A3.git
    ```
3.  Navegue até a pasta do projeto e execute o arquivo principal:
    ```bash
    python "Projeto A3/Code.py"
    ```

---
**Desenvolvido por:**
*   [Graziel Silva](https://github.com/Graziel-Silva)
*   [Wesley Oliveira](https://github.com/PRESIDIARIO01)
*   [Pedro Baleeiro](https://github.com/pedrobaleeiro)