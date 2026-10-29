import flet as ft




def main(page: ft.Page):
    precos = {
        'pequena': 30.00,
        'media': 40.00,
        'grande': 50.00
    }


    pedidos = []
    listar_pedidos = ft.Column(controls=[])
    resultado = ft.Text('', size=20)
    exibir_total = ft.Text('Total a pagar: 0.00', size=20)
    largura = 350
    QuantidadeTotal = ft.Text('Total de pizzas: 0', size=20)




    def mostrar_valor(e):
        if not qtd.value or not sabor.value or not tamanho.value:
            resultado.value = "Preencha sabor, tamanho e quantidade."
            page.update()
            return


        if not qtd.value.isdigit() or int(qtd.value) <= 0:
            resultado.value = "Digite uma quantidade inteira maior que zero."
            page.update()
            return


        quantidade = int(qtd.value)


        pizza = {
            'sabor': sabor.value,
            'quantidade': quantidade,
            'tamanho': tamanho.value,
            'observacao': observacao.value
        }


        pedidos.append(pizza)


        preco_atual = precos[pizza['tamanho']]
        subtotal = preco_atual * pizza['quantidade']


        texto_pizza = (
            f"Pizza {len(pedidos)}\n"
            f"Sabor: {pizza['sabor']}\n"
            f"Tamanho: {pizza['tamanho']}\n"
            f"Quantidade: {pizza['quantidade']}\n"
            f"Observação: {pizza['observacao']}\n"
            f"Subtotal: R$ {subtotal:.2f}"
        )


        listar_pedidos.controls.append(ft.Text(texto_pizza))


        resultado.value = (
            f"{usuario.value} sua pizza foi adicionada ao carrinho."
        )


        sabor.value = None
        qtd.value = ''
        tamanho.value = None
        observacao.value = 'sem observação'


        page.update()


        if not pedidos:
            resultado.value = "Adicione uma pizza antes de calcular."
            page.update()
            return
       
        total = 0
       
        for pedido in pedidos:
            quantidade = pedido['quantidade']
            tamanho_atual = pedido['tamanho']
            preco_unitario = precos[tamanho_atual]
       
            soma = preco_unitario * quantidade
            total += soma
        quantidade_total = 0


        for pedido in pedidos:
            quantidade_total += pedido['quantidade']




        exibir_total.value = f"Total a pagar: R$ {total:.2f}"
        QuantidadeTotal.value = f"QuantidadeTotal: {quantidade_total}"
        page.update()








    def limpar(e):
        usuario.value = ''
        resultado.value = ''
        sabor.value = None
        qtd.value = ''
        tamanho.value = None
        observacao.value = 'sem observação'
        pedidos.clear()
        listar_pedidos.controls.clear()
        exibir_total.value = 'Total a pagar: 0.00'
        QuantidadeTotal.value = 'Total de pizzas: 0'
        page.update()
       


    usuario = ft.TextField(
        label='Digite seu nome:',
        width=largura
    )


    titulo = ft.Text('Pizzaria', size=30)


    qtd = ft.TextField(
        label='Digite a quantidade',
        width=largura
    )


    botao = ft.Button(
        content='Adicionar ao carrinho',
        on_click=mostrar_valor
    )


    botao_limpar = ft.Button(
        content='Limpar',
        on_click=limpar
    )


    sabor = ft.Dropdown(
        label='Escolha o sabor:',
        options=[
            ft.DropdownOption(key='maionese'),
            ft.DropdownOption(key='batata')
        ],
        width=largura
    )


    tamanho = ft.Dropdown(
        label='Escolha o tamanho:',
        options=[
            ft.DropdownOption(key='pequena'),
            ft.DropdownOption(key='media'),
            ft.DropdownOption(key='grande')
        ],
        width=largura
    )


    observacao = ft.TextField(
        label='Observações?',
        width=largura
    )




    coluna = ft.Column(
        [
            titulo,
            usuario,
            sabor,
            tamanho,
            qtd,
            observacao,
            ft.Row(
                [botao, botao_limpar],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            resultado,
            listar_pedidos,
            exibir_total,QuantidadeTotal
        ],
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        scroll=ft.ScrollMode.AUTO
    )


    page.add(coluna)




ft.run(main)



