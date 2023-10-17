import flet as ft


def main(Calc_Sal: ft.Page):
    Calc_Sal.title = "Calculadora de Salario"
    Calc_Sal.window_resizable = False
    Calc_Sal.window_width = 390
    Calc_Sal.window_height = 360
    Calc_Sal.window_always_on_top = True

    def calcular_salario(e):
        seu_salario.value = str(((int(horas.value) * 60) + int(minutos.value)) * (float(ganho_hora.value) / 60))
        Calc_Sal.update()

    def zerar_horas(e):
        horas.value = str("")
        Calc_Sal.update()
    
    def zerar_minutos(e):
        minutos.value = str("")
        Calc_Sal.update()
    
    def zerar_ganho_hora(e):
        ganho_hora.value = str("")
        Calc_Sal.update()

    # criar botoes
    calcular = ft.ElevatedButton(text="Calcular salario", on_click=calcular_salario)

    horas = ft.TextField(label="Quantas horas voce trabalhou?", value="0", width="350", text_align=ft.TextAlign.CENTER, on_focus=zerar_horas)

    minutos = ft.TextField(label="Quantos minutos voce trabalhou?", value="0", width="350", text_align=ft.TextAlign.CENTER, on_focus=zerar_minutos)

    ganho_hora = ft.TextField(label="Quanto voce ganha por hora?", value="0", width="350", text_align=ft.TextAlign.CENTER, on_focus=zerar_ganho_hora)

    seu_salario = ft.TextField(label="Seu salario", value='', width="350")

    # criar funcoes

    # criar tela
    Calc_Sal.add(
        ft.Column([horas, minutos, ganho_hora, calcular, seu_salario], alignment=ft.TextAlign.CENTER)
    )


ft.app(target=main)
