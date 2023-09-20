import flet as ft


def main(Calc_Sal: ft.Page):
    Calc_Sal.title = "Calculadora de Salario"
    Calc_Sal.window_resizable = False
    Calc_Sal.window_width = 390
    Calc_Sal.window_height = 360

    def calcular_salario(e):
        seuSalario.value = str(((int(horas.value) * 60) + int(minutos.value)) * (float(ganhoHora.value) / 60))
        Calc_Sal.update()

    # criar botoes
    calcular = ft.ElevatedButton(text="Calcular salario", on_click=calcular_salario)

    horas = ft.TextField(label="Quantas horas voce trabalhou?", value="0", width="350", text_align=ft.TextAlign.CENTER)

    minutos = ft.TextField(label="Quantos minutos voce trabalhou?", value="0", width="350",
                           text_align=ft.TextAlign.CENTER)

    ganhoHora = ft.TextField(label="Quanto voce ganha por hora?", value="0", width="350",
                             text_align=ft.TextAlign.CENTER)

    seuSalario = ft.TextField(label="Seu salario", value='', width="350")

    # criar funcoes

    # criar tela
    Calc_Sal.add(
        ft.Column([horas, minutos, ganhoHora, calcular, seuSalario], alignment=ft.TextAlign.CENTER)
    )


ft.app(target=main)
