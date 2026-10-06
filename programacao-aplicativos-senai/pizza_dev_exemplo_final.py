import flet as ft


def main(page: ft.Page):
    page.title = "PizzaDev"

    # =========================
    # ESTADO DO PEDIDO
    # =========================
    estado = {
        "pizza": None,
        "tamanho": "M",
        "quantidade": 1,
        "nome": "",
        "telefone": "",
        "recebimento": "retirada",
        "rua": "",
        "numero": "",
        "bairro": "",
        "complemento": "",
        "taxa_entrega": 0,
        "pagamento": "pix",
        "valor_recebido": 0,
        "troco": 0,
        "observacao": ""
    }

    # =========================
    # CARRINHO
    # =========================
    carrinho = []

    lista_visual = ft.ListView(
        spacing=8,
        expand=True
    )

    subtotal_texto = ft.Text(
        "Subtotal: R$ 0.00",
        size=22,
        weight=ft.FontWeight.BOLD
    )

    total_texto = ft.Text(
        "Total: R$ 0.00",
        size=24,
        weight=ft.FontWeight.BOLD
    )

    # O botão é criado na tela do carrinho.
    # A variável começa como None para podermos atualizá-la depois.
    botao_avancar = None

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
    # FUNÇÕES DE VALOR
    # =========================
    def calcular_subtotal():
        subtotal = 0
        for item in carrinho:
            subtotal += item["preco"] * item["qtd"]
        return subtotal

    def calcular_total():
        return calcular_subtotal() + estado["taxa_entrega"]

    # =========================
    # AVISAR COM SNACKBAR
    # =========================
    def avisar(texto):
        page.show_dialog(
            ft.SnackBar(
                ft.Text(texto)
            )
        )

    # =========================
    # DIMINUIR QUANTIDADE
    # =========================
    def diminuir_quantidade(indice):
        item = carrinho[indice]

        if item["qtd"] > 1:
            item["qtd"] -= 1
            atualizar_carrinho()
        else:
            avisar("A quantidade mínima é 1.")

    # =========================
    # AUMENTAR QUANTIDADE
    # =========================
    def aumentar_quantidade(indice):
        item = carrinho[indice]

        if item["qtd"] < 10:
            item["qtd"] += 1
            atualizar_carrinho()
        else:
            avisar("A quantidade máxima é 10.")

    # =========================
    # REMOVER ITEM
    # =========================
    def remover_item(indice):
        item = carrinho[indice]
        nome = item["nome"]

        carrinho.pop(indice)
        atualizar_carrinho()
        avisar(f"{nome} removida do carrinho.")

    # =========================
    # LIMPAR CARRINHO
    # =========================
    def limpar_carrinho():
        carrinho.clear()
        estado["taxa_entrega"] = 0
        atualizar_carrinho()
        avisar("Carrinho limpo.")
        mostrar_carrinho()

    def confirmar_limpeza(e):
        dialogo = ft.AlertDialog(
            title=ft.Text("Limpar carrinho?"),
            content=ft.Text("Todos os itens serão removidos."),
            actions=[
                ft.TextButton(
                    "Cancelar",
                    on_click=lambda e: page.pop_dialog()
                ),
                ft.TextButton(
                    "Confirmar",
                    on_click=lambda e: (
                        page.pop_dialog(),
                        limpar_carrinho()
                    )
                )
            ]
        )
        page.show_dialog(dialogo)

    # =========================
    # ATUALIZAR CARRINHO
    # =========================
    def atualizar_carrinho():
        nonlocal botao_avancar

        lista_visual.controls.clear()
        subtotal = 0

        for indice, item in enumerate(carrinho):
            parcial = item["preco"] * item["qtd"]
            subtotal += parcial

            botao_menos = ft.Button(
                "-",
                on_click=lambda e, i=indice: diminuir_quantidade(i)
            )

            botao_mais = ft.Button(
                "+",
                on_click=lambda e, i=indice: aumentar_quantidade(i)
            )

            botao_remover = ft.Button(
                "Remover",
                on_click=lambda e, i=indice: remover_item(i)
            )

            linha = ft.Row([
                ft.Text(
                    f'{item["nome"]} - '
                    f'{item["tamanho"]} - '
                    f'x{item["qtd"]} - '
                    f'R$ {parcial:.2f}',
                    size=20
                ),
                botao_menos,
                botao_mais,
                botao_remover
            ])

            lista_visual.controls.append(linha)

        subtotal_texto.value = f"Subtotal: R$ {subtotal:.2f}"
        total_texto.value = f"Total: R$ {calcular_total():.2f}"

        # Atividade 8: só permite avançar se houver item no carrinho.
        if botao_avancar is not None:
            botao_avancar.disabled = len(carrinho) == 0

        page.update()

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
            estado["pizza"] = pizza["nome"]
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

        quantidade = ft.TextField(
            label="Quantidade",
            value=str(estado["quantidade"])
        )

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

        # =========================
        # CALCULAR
        # =========================
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

            estado["quantidade"] = qtd
            estado["tamanho"] = tamanho.value

            if tamanho.value == "M":
                preco = pizza_escolhida["m"]
            else:
                preco = pizza_escolhida["g"]

            total = qtd * preco
            mensagem.value = f"Parcial: R$ {total:.2f}"
            area.update()

        # =========================
        # ADICIONAR AO CARRINHO
        # =========================
        def adicionar_carrinho(e):
            if not quantidade.value.isdigit():
                mensagem.value = "Digite uma quantidade inteira."
                area.update()
                return

            qtd = int(quantidade.value)

            if qtd < 1 or qtd > 10:
                mensagem.value = "Quantidade deve ficar entre 1 e 10."
                area.update()
                return

            estado["quantidade"] = qtd
            estado["tamanho"] = tamanho.value

            if tamanho.value == "M":
                preco = pizza_escolhida["m"]
            else:
                preco = pizza_escolhida["g"]

            item = {
                "nome": pizza_escolhida["nome"],
                "tamanho": tamanho.value,
                "qtd": qtd,
                "preco": preco
            }

            carrinho.append(item)
            atualizar_carrinho()
            mostrar_carrinho()

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
                    "Adicionar ao carrinho",
                    on_click=adicionar_carrinho
                )
            ])
        ])

        area.update()

    # =========================
    # TELA CARRINHO - AULA 8
    # =========================
    def mostrar_carrinho():
        nonlocal botao_avancar

        botao_avancar = ft.Button(
            "Avançar",
            on_click=lambda e: mostrar_cliente(),
            disabled=len(carrinho) == 0
        )

        atualizar_carrinho()

        area.content = ft.Column([
            ft.Text(
                "Carrinho",
                size=30,
                weight=ft.FontWeight.BOLD
            ),
            lista_visual,
            subtotal_texto,
            total_texto,
            ft.Row([
                ft.Button(
                    "Continuar comprando",
                    on_click=lambda e: mostrar_cardapio()
                ),
                ft.Button(
                    "Limpar carrinho",
                    on_click=confirmar_limpeza
                ),
                botao_avancar,
                ft.Button(
                    "Voltar",
                    on_click=lambda e: mostrar_selecao()
                )
            ])
        ])

        area.update()

    # =========================
    # AULA 9 - DADOS DO CLIENTE
    # =========================
    def mostrar_cliente():
        nome = ft.TextField(
            label="Nome",
            value=estado["nome"]
        )

        telefone = ft.TextField(
            label="Telefone",
            value=estado["telefone"]
        )

        recebimento = ft.RadioGroup(
            content=ft.Row([
                ft.Radio(value="retirada", label="Retirada"),
                ft.Radio(value="entrega", label="Entrega")
            ]),
            value=estado["recebimento"]
        )

        rua = ft.TextField(
            label="Rua",
            value=estado["rua"]
        )

        numero = ft.TextField(
            label="Número",
            value=estado["numero"]
        )

        bairro = ft.TextField(
            label="Bairro",
            value=estado["bairro"]
        )

        complemento = ft.TextField(
            label="Complemento",
            value=estado["complemento"]
        )

        endereco = ft.Column([
            ft.Text(
                "Endereço de entrega",
                size=22,
                weight=ft.FontWeight.BOLD
            ),
            rua,
            numero,
            bairro,
            complemento
        ], visible=estado["recebimento"] == "entrega")

        mensagem = ft.Text(size=18)

        def recebimento_mudou(e):
            endereco.visible = recebimento.value == "entrega"

            if recebimento.value == "retirada":
                estado["taxa_entrega"] = 0
            else:
                estado["taxa_entrega"] = 6

            total_cliente.value = f"Total: R$ {calcular_total():.2f}"
            page.update()

        recebimento.on_change = recebimento_mudou

        total_cliente = ft.Text(
            f"Total: R$ {calcular_total():.2f}",
            size=24,
            weight=ft.FontWeight.BOLD
        )

        def validar_cliente(e):
            nome.error_text = None
            telefone.error_text = None
            rua.error_text = None
            numero.error_text = None
            bairro.error_text = None

            nome_valor = nome.value.strip()
            digitos = "".join(c for c in telefone.value if c.isdigit())

            valido = True

            if not nome_valor:
                nome.error_text = "Informe o nome."
                valido = False

            if len(digitos) not in (10, 11):
                telefone.error_text = "Use DDD + número (10 ou 11 dígitos)."
                valido = False

            if recebimento.value == "entrega":
                if not rua.value.strip():
                    rua.error_text = "Informe a rua."
                    valido = False

                if not numero.value.strip():
                    numero.error_text = "Informe o número."
                    valido = False

                if not bairro.value.strip():
                    bairro.error_text = "Informe o bairro."
                    valido = False

            if not valido:
                page.update()
                return

            estado["nome"] = nome_valor
            estado["telefone"] = digitos
            estado["recebimento"] = recebimento.value
            estado["rua"] = rua.value.strip()
            estado["numero"] = numero.value.strip()
            estado["bairro"] = bairro.value.strip()
            estado["complemento"] = complemento.value.strip()

            if recebimento.value == "entrega":
                estado["taxa_entrega"] = 6
            else:
                estado["taxa_entrega"] = 0

            mensagem.value = "Dados válidos!"
            page.update()
            mostrar_pagamento()

        area.content = ft.Column([
            ft.Text(
                "Dados do cliente e recebimento",
                size=30,
                weight=ft.FontWeight.BOLD
            ),
            nome,
            telefone,
            ft.Text(
                "Como deseja receber?",
                size=20,
                weight=ft.FontWeight.BOLD
            ),
            recebimento,
            endereco,
            total_cliente,
            mensagem,
            ft.Row([
                ft.Button(
                    "Voltar",
                    on_click=lambda e: mostrar_carrinho()
                ),
                ft.Button(
                    "Continuar para pagamento",
                    on_click=validar_cliente
                )
            ])
        ])

        area.update()

    # =========================
    # AULA 10 - PAGAMENTO
    # =========================
    def mostrar_pagamento():
        pagamento = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="dinheiro", label="Dinheiro"),
                ft.Radio(value="pix", label="Pix"),
                ft.Radio(value="cartao", label="Cartão")
            ]),
            value=estado["pagamento"]
        )

        valor_recebido = ft.TextField(
            label="Valor recebido",
            visible=estado["pagamento"] == "dinheiro"
        )

        troco_texto = ft.Text(
            "",
            size=20,
            weight=ft.FontWeight.BOLD
        )

        observacao = ft.TextField(
            label="Observação",
            multiline=True,
            max_length=120,
            value=estado["observacao"]
        )

        total_pagamento = ft.Text(
            f"Total do pedido: R$ {calcular_total():.2f}",
            size=25,
            weight=ft.FontWeight.BOLD
        )

        def pagamento_mudou(e):
            valor_recebido.visible = pagamento.value == "dinheiro"
            valor_recebido.error_text = None
            troco_texto.value = ""
            page.update()

        pagamento.on_change = pagamento_mudou

        def validar_pagamento(e):
            total = calcular_total()
            estado["pagamento"] = pagamento.value
            estado["observacao"] = observacao.value

            valor_recebido.error_text = None

            if pagamento.value == "dinheiro":
                texto_valor = valor_recebido.value.strip().replace(",", ".")

                try:
                    valor = float(texto_valor)
                except ValueError:
                    valor_recebido.error_text = "Informe um valor válido."
                    troco_texto.value = ""
                    page.update()
                    return

                if valor < total:
                    valor_recebido.error_text = (
                        f"Valor insuficiente. O total é R$ {total:.2f}."
                    )
                    troco_texto.value = ""
                    page.update()
                    return

                troco = valor - total
                estado["valor_recebido"] = valor
                estado["troco"] = troco
                troco_texto.value = f"Troco: R$ {troco:.2f}"

            else:
                estado["valor_recebido"] = 0
                estado["troco"] = 0
                troco_texto.value = ""

            page.update()

        def finalizar_pedido(e):
            validar_pagamento(e)

            if pagamento.value == "dinheiro" and valor_recebido.error_text:
                return

            estado["pagamento"] = pagamento.value
            estado["observacao"] = observacao.value

            avisar("Pedido finalizado com sucesso!")

        area.content = ft.Column([
            ft.Text(
                "Pagamento",
                size=30,
                weight=ft.FontWeight.BOLD
            ),
            total_pagamento,
            ft.Text(
                "Forma de pagamento:",
                size=20,
                weight=ft.FontWeight.BOLD
            ),
            pagamento,
            valor_recebido,
            troco_texto,
            observacao,
            ft.Row([
                ft.Button(
                    "Voltar",
                    on_click=lambda e: mostrar_cliente()
                ),
                ft.Button(
                    "Calcular pagamento",
                    on_click=validar_pagamento
                ),
                ft.Button(
                    "Finalizar pedido",
                    on_click=finalizar_pedido
                )
            ])
        ])

        area.update()

    # =========================
    # AUTOR
    # =========================
    autor = ft.Text(
        "Autor: Ruan",
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
