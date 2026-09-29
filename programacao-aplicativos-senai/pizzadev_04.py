import flet as ft




def main(page: ft.Page):
    page.title = 'PizzaDev'


    # =========================
    # ESTADO DO PEDIDO
    # =========================
    estado = {
        "pizza": None,
        "tamanho": "M",
        "quantidade": 1
    }


    # =========================
    # DADOS DAS PIZZAS
    # =========================
    PIZZAS = [
        {
            "id": "P01",
            "nome": "Calabresa",
            "ingredientes": "calabresa, cebola e muçarela",
            "m": 32,
            "g": 42
        },
        {
            "id": "P02",
            "nome": "Queijo",
            "ingredientes": "ralado, presunto",
            "m": 35,
            "g": 46
        },
        {
            "id": "P03",
            "nome": "Doce",
            "ingredientes": "morango, abacaxi",
            "m": 35,
            "g": 46
        },
        {
            "id": "P04",
            "nome": "Havaiana",
            "ingredientes": "baunilha, sorvete",
            "m": 50,
            "g": 10
        }
    ]


    # =========================
    # ÁREA CENTRAL
    # =========================
    area = ft.Container(
        expand=True
    )


    # =========================
    # TELA INÍCIO
    # =========================
    def mostrar_inicio():


        area.content = ft.Column([
            ft.Text(
                "PizzaDev",
                size=30,
                weight=ft.FontWeight.BOLD
            ),


            ft.Text(
                "monte seu pedido com segurança",
                size=25
            ),


            ft.Text(
                "Bem-vindo ao PizzaDev!",
                size=22
            ),


            ft.Button(
                "Abrir cardápio",
                on_click=lambda e: mostrar_cardapio()
            )
        ])


        area.update()


    # =========================
    # TELA CARDÁPIO
    # =========================
    def mostrar_cardapio():


        coluna_esquerda = []
        coluna_direita = []


        # FOR PARA CRIAR OS CARDS
        for i, pizza in enumerate(PIZZAS):


            card = criar_card(pizza)


            if i % 2 == 0:
                coluna_esquerda.append(card)
            else:
                coluna_direita.append(card)


        area.content = ft.Column([


            ft.Text(
                "Cardápio",
                size=30,
                weight=ft.FontWeight.BOLD
            ),


            ft.Text(
                f"Pedido em edição: "
                f"{estado['pizza'] if estado['pizza'] else 'Nenhuma pizza'}"
            ),


            ft.Row([
                ft.Column(coluna_esquerda),
                ft.Column(coluna_direita)
            ]),


            ft.Button(
                "Voltar",
                on_click=lambda e: mostrar_inicio()
            )
        ])


        area.update()


    # =========================
    # FUNÇÃO PARA CRIAR CARD
    # =========================
    def criar_card(pizza):


        def escolher(e):


            # Guarda a pizza no estado
            estado["pizza"] = pizza["nome"]


            # Vai para a tela de seleção
            mostrar_selecao()


        return ft.Container(
            padding=15,
            border_radius=12,
            content=ft.Column([


                ft.Text(
                    pizza["nome"],
                    size=30,
                    weight=ft.FontWeight.BOLD
                ),


                ft.Text(
                    pizza["ingredientes"],
                    size=25
                ),


                ft.Row([
                    ft.Text(
                        f'M: R$ {pizza["m"]}',
                        size=25
                    ),


                    ft.Text(
                        f'G: R$ {pizza["g"]}',
                        size=25
                    )
                ]),


                ft.Button(
                    f'Escolher {pizza["nome"]}',
                    on_click=escolher
                )
            ])
        )


    # =========================
    # TELA DE SELEÇÃO
    # =========================
    def mostrar_selecao():


        pizza_escolhida = None


        for pizza in PIZZAS:
            if pizza["nome"] == estado["pizza"]:
                pizza_escolhida = pizza


        # Campo de quantidade
        quantidade = ft.TextField(
            label="Quantidade",
            value=str(estado["quantidade"])
        )


        # Tamanho
        tamanho = ft.RadioGroup(
            content=ft.Row([
                ft.Radio(
                    value="M",
                    label="M"
                ),
                ft.Radio(
                    value="G",
                    label="G"
                )
            ]),
            value=estado["tamanho"]
        )


        mensagem = ft.Text(
            f"Pizza selecionada: {estado['pizza']}",
            size=22,
            weight=ft.FontWeight.BOLD
        )


        # Função calcular
        def calcular(e):


            if not quantidade.value.isdigit():
                mensagem.value = "Digite uma quantidade inteira."
                area.update()
                return


            qtd = int(quantidade.value)


            if qtd < 1 or qtd > 10:
                mensagem.value = "Quantidade deve ficar entre 1 e 10."
                area.update()
                return


            # Guarda quantidade e tamanho no estado
            estado["quantidade"] = qtd
            estado["tamanho"] = tamanho.value


            if tamanho.value == "M":
                preco = pizza_escolhida["m"]
            else:
                preco = pizza_escolhida["g"]


            total = qtd * preco


            mensagem.value = f"Parcial: R$ {total:.2f}"


            area.update()


        area.content = ft.Column([


            ft.Text(
                "Seleção",
                size=30,
                weight=ft.FontWeight.BOLD
            ),


            ft.Text(
                f"Pedido em edição: {estado['pizza']}"
            ),


            ft.Text(
                f"Pizza: {pizza_escolhida['nome']}",
                size=25
            ),


            ft.Text(
                pizza_escolhida["ingredientes"],
                size=20
            ),


            quantidade,


            tamanho,


            ft.Button(
                "Calcular",
                on_click=calcular
            ),


            mensagem,


            ft.Row([
                ft.Button(
                    "Voltar",
                    on_click=lambda e: mostrar_cardapio()
                ),


                ft.Button(
                    "Carrinho",
                    on_click=lambda e: mostrar_carrinho()
                )
            ])
        ])


        area.update()


    # =========================
    # TELA CARRINHO
    # =========================
    def mostrar_carrinho():


        area.content = ft.Column([


            ft.Text(
                "Carrinho",
                size=30,
                weight=ft.FontWeight.BOLD
            ),


            ft.Text(
                "Carrinho vazio",
                size=22
            ),


            ft.Text(
                f"Pizza guardada: {estado['pizza']}"
            ),


            ft.Button(
                "Voltar",
                on_click=lambda e: mostrar_selecao()
            )
        ])


        area.update()


    # =========================
    # AUTOR
    # =========================
    autor = ft.Text(
        'Autor: Ruan',
        size=20,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.RED
    )


    # =========================
    # COLOCA A ÁREA NA PÁGINA
    # =========================
    page.add(
        area,
        autor
    )


    # Começa na tela inicial
    mostrar_inicio()




ft.run(main)

