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


    # Texto que vai mostrar a pizza selecionada
    mensagem = ft.Text(
        'Nenhuma pizza selecionada',
        size=22,
        weight=ft.FontWeight.BOLD
    )


    # Funções dos botões
    def escolher_calabresa(e):
        mensagem.value = 'Selecionada: Calabresa - M: R$ 32'
        page.update()


    def escolher_queijo(e):
        mensagem.value = 'Selecionada: Queijo - M: R$ 35'
        page.update()


    def escolher_doce(e):
        mensagem.value = 'Selecionada: Doce - M: R$ 35'
        page.update()


    def escolher_havaiana(e):
        mensagem.value = 'Selecionada: Havaiana - M: R$ 50'
        page.update()


    calabresa = ft.Container(
        padding=15,
        border_radius=12,
        content=ft.Column([
            ft.Text(
                "Calabresa",
                size=30,
                weight=ft.FontWeight.BOLD
            ),
            ft.Text(
                "calabresa, cebola e muçarela",
                size=25
            ),
            ft.Row([
                ft.Text("M: R$ 32", size=25),
                ft.Text("G: R$ 42", size=25)
            ]),
            ft.Button(
                "Escolher Calabresa",
                on_click=escolher_calabresa
            )
        ])
    )


    queijo = ft.Container(
        padding=15,
        border_radius=12,
        content=ft.Column([
            ft.Text(
                "Queijo",
                size=30,
                weight=ft.FontWeight.BOLD
            ),
            ft.Text(
                "ralado, presunto",
                size=25
            ),
            ft.Row([
                ft.Text("M: R$ 35", size=25),
                ft.Text("G: R$ 46", size=25)
            ]),
            ft.Button(
                "Escolher Queijo",
                on_click=escolher_queijo
            )
        ])
    )


    doce = ft.Container(
        padding=15,
        border_radius=12,
        content=ft.Column([
            ft.Text(
                "Doce",
                size=30,
                weight=ft.FontWeight.BOLD
            ),
            ft.Text(
                "morango, abacaxi",
                size=25
            ),
            ft.Row([
                ft.Text("M: R$ 35", size=25),
                ft.Text("G: R$ 46", size=25)
            ]),
            ft.Button(
                "Escolher Doce",
                on_click=escolher_doce
            )
        ])
    )


    havaiana = ft.Container(
        padding=15,
        border_radius=12,
        content=ft.Column([
            ft.Text(
                "Havaiana",
                size=30,
                weight=ft.FontWeight.BOLD
            ),
            ft.Text(
                "baunilha, sorvete",
                size=25
            ),
            ft.Row([
                ft.Text("M: R$ 50", size=25),
                ft.Text("G: R$ 10", size=25)
            ]),
            ft.Button(
                "Escolher Havaiana",
                on_click=escolher_havaiana
            )
        ])
    )


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


    # Mensagem de seleção
    page.add(mensagem)


    # Pizzas em 2 colunas
    page.add(
        ft.Row(
            [
                ft.Column([
                    calabresa,
                    doce
                ]),
                ft.Column([
                    queijo,
                    havaiana
                ])
            ],
            scroll=ft.ScrollMode.AUTO
        )
    )


    page.add(autor)




ft.run(main)

