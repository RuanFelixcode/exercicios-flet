import flet as ft


def main(page: ft.Page):
    # variáveis simples e compostas e textos
    emprestimos = []
    resultado = ft.Text('')
    total_unidades = ft.Text('Total de unidades emprestadas: 0', size=20)
    lista_emprestimos = ft.Column(controls=[])
    largura = 350

    # função para calcular o total de unidades
    def calcular_total():
        total = 0

        for emprestimo in emprestimos:
            total += emprestimo["quantidade"]

        total_unidades.value = f'Total de unidades emprestadas: {total}'

    # função dos botões
    def limpar(e):
        usuario.value = ''
        qtd.value = ''
        equipamento.value = None
        resultado.value = ''
        page.update()

    def solicitar(e):
        if not usuario.value.strip():
            resultado.value = 'Informe o nome do responsável.'
            page.update()
            return

        if not qtd.value.isdigit() or int(qtd.value) <= 0:
            resultado.value = 'Digite uma quantidade inteira maior que zero.'
            page.update()
            return

        if equipamento.value is None:
            resultado.value = 'Selecione um equipamento.'
            page.update()
            return

        emprestimo = {
            "responsavel": usuario.value.strip(),
            "equipamento": equipamento.value,
            "quantidade": int(qtd.value)
        }

        emprestimos.append(emprestimo)

        calcular_total()
        texto_emprestimo = (
    f"Responsável: {emprestimo['responsavel']}\n"
    f"Equipamento: {emprestimo['equipamento']}\n"
    f"Quantidade: {emprestimo['quantidade']}"
)

        lista_emprestimos.controls.append(
    ft.Text(texto_emprestimo)
)

        resultado.value = 'Empréstimo registrado com sucesso!'
        page.update()

    # botões
    botao_limpar = ft.Button(
        content='Limpar',
        on_click=limpar
    )

    botao_solicitar = ft.Button(
        content='Solicitar empréstimo',
        on_click=solicitar
    )

    # objetos
    usuario = ft.TextField(
        label='Digite o nome do responsável:',
        width=largura
    )

    qtd = ft.TextField(
        label='Digite a quantidade',
        width=largura
    )

    equipamento = ft.Dropdown(
        label='Escolha o equipamento:',
        options=[
            ft.DropdownOption(key='notebook'),
            ft.DropdownOption(key='projetor'),
            ft.DropdownOption(key='multímetro')
        ],
        width=largura
    )

    # organizar elementos e adicionar na página
    coluna = ft.Column(
        [
            usuario,
            equipamento,
            qtd,
            ft.Row(
                [botao_solicitar, botao_limpar],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            resultado,
            total_unidades,lista_emprestimos
        ],
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        scroll=ft.ScrollMode.AUTO
    )

    page.add(coluna)


ft.run(main)
