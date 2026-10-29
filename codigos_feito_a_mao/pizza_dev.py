import flet as ft


def main(page:ft.Page):


    resultado = ft.Text('',size=20)
    largura = 350
    def mostrar_valor(e):
        if not qtd.value or not sabor.value:
            resultado.value = "prencha todos os campo"
        else:
            resultado.value = f'pedido: {sabor.value}\nquantiade: {qtd.value}'
        page.update()




    def limpar(e):
        resultado.value = ''
        sabor.value = None
        qtd.value = ''
        usuario.value = ''
        tamanho.value = ''
        observacao.value = ''
        page.update()


    def calcular_total(e):
        # 1. Verifica se os campos obrigatórios para o cálculo foram preenchidos
        if not qtd.value or not tamanho.value or not sabor.value:
            resultado.value = "Preencha sabor, tamanho e quantidade para calcular."
            page.update()
            return
       
        # 2. Tabela de preços fictícia baseada no tamanho
        precos = {
            'pequena': 10.00,
            'media': 15.00,
            'grande': 20.00
        }


        try:
            # 3. Converte o texto da quantidade para número inteiro
            quantidade = int(qtd.value)
           
            # 4. Busca o preço na tabela e faz a multiplicação
            preco_unitario = precos[tamanho.value]
            total = preco_unitario * quantidade
           
            # 5. Exibe o resultado formatado com duas casas decimais
            resultado.value = f'Pedido: {quantidade}x {sabor.value} ({tamanho.value})\nTotal a Pagar: R$ {total:.2f}'
           
        except ValueError:
            # Caso o usuário digite letras no campo de quantidade
            resultado.value = "Erro: Digite apenas números na quantidade."
           
        page.update()


    usuario = ft.TextField(label = 'digite seu nome:',width=largura)


    titulo = ft.Text('titulo',size=30)
    qtd = ft.TextField(label = 'digite a quantidade',width=largura)
    botao = ft.Button(content='botão exibir',on_click=mostrar_valor)


    botao_limpar = ft.Button(content='botão_limpar',on_click=limpar)




    sabor = ft.Dropdown(label='ecolha uma opção:',options=[
        ft.DropdownOption(key='maionese'),
        ft.DropdownOption(key='batata'),
    ],width=largura)


    tamanho = ft.Dropdown(label='ecolha o tamanho:',options=[
            ft.DropdownOption(key='pequena'),
            ft.DropdownOption(key='media'),
            ft.DropdownOption(key='grande'),
        ],width=largura)


    observacao = ft.TextField(label = 'observações?',width=largura)
   
    botao_total = ft.Button(content='Calcular Total', bgcolor="black",  
        color="white",on_click=calcular_total
        )




    coluna = ft.Column(
[titulo,
 usuario,
 sabor,
 tamanho,
 qtd,
 observacao,
 ft.Row([botao,botao_limpar]),
 botao_total,
resultado]


    )


    page.add(coluna)




ft.run(main)

