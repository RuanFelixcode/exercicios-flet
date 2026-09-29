import flet as ft




def main(page: ft.Page):
    page.title = 'PizzaDev'


    titulo = ft.Text(
        'PizzaDev',
        size=30,
        weight=ft.FontWeight.BOLD
    )


    subtitulo = ft.Text(
        'monte seu pedido com segurança',
        size=25
    )


    nome = ft.Text(
        'Nome:',
        size=20,
        weight=ft.FontWeight.BOLD
    )


    slogan = ft.Text(
        'Slogan',
        size=20
    )


    intrucao = ft.Text(
        'Compre nosso produto',
        size=20
    )


    # Texto que vai mostrar a mensagem
    mensagem = ft.Text(
        'Configure sua pizza Calabresa',
        size=22,
        weight=ft.FontWeight.BOLD
    )


    # Campo para digitar a quantidade
    quantidade = ft.TextField(
        label="Quantidade"
    )


    # Escolha do tamanho
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
        value="M"
    )


    # Função para calcular
    def calcular(e):


        if not quantidade.value.isdigit():
            mensagem.value = "Digite uma quantidade inteira."
            page.update()
            return


        qtd = int(quantidade.value)


        if qtd < 1 or qtd > 10:
            mensagem.value = "Quantidade deve ficar entre 1 e 10."
            page.update()
            return


        if tamanho.value == "M":
            preco = 32
        else:
            preco = 42


        total = qtd * preco


        mensagem.value = f"Parcial: R$ {total:.2f}"


        page.update()




    # Botão calcular
    botao_calcular = ft.Button(
        "Calcular",
        on_click=calcular
    )


        # Dados das pizzas
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


    # Função que recebe uma pizza e cria o card
    def criar_card(pizza):


        def escolher(e):
            mensagem.value = (
                f'Selecionada: {pizza["nome"]} - '
                f'M: R$ {pizza["m"]}'
            )
            page.update()


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


    # Cria os cards usando o for
    coluna_esquerda = []
    coluna_direita = []


    for i, pizza in enumerate(PIZZAS):


        card = criar_card(pizza)


        if i % 2 == 0:
            coluna_esquerda.append(card)
        else:
            coluna_direita.append(card)


    autor = ft.Text(
        'Autor: Ruan',
        size=20,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.RED
    )


    # Cabeçalho
    page.add(titulo)
    page.add(subtitulo)
    page.add(nome)
    page.add(slogan)
    page.add(intrucao)


    # Mensagem + configuração da pizza
    page.add(
        ft.Column([
            mensagem,
            quantidade,
            tamanho,
            botao_calcular
        ])
    )


    # Pizzas em 2 colunas
    page.add(
        ft.Row(
            [
                ft.Column(coluna_esquerda),
                ft.Column(coluna_direita)
            ],
            scroll=ft.ScrollMode.AUTO
        )
    )


    page.add(autor)




ft.run(main)

