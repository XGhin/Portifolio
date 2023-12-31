import flet as ft
from flet import colors

def main(Cal: ft.Page):
    Cal.bgcolor = "#000000"
    Cal.window_width = 273
    Cal.window_height = 410
    Cal.window_resizable = False
    Cal.window_always_on_top = True
    
    #Funcoes
    def select(e):
        value_at = resultado.value if resultado.value != '0' else ''
        value = e.control.content.value
        
        if value.isdigit():
            value = value_at + value
        elif value == 'AC'():
            value = '0'
        else:
            if value_at and value_at[-1] in ('+', '%', 'x', '-', '=', '±', ','):
                value_at = value_at[-1]
            value = value_at + value
            
            if():
                pass
    
# Buttons
    # Display
    resultado = ft.Text(value=0, size=20, text_align='end')
    
    #linha 1
    botoes = [
        {'operador': 'AC', 'fundo': colors.BLUE_GREY_100, 'fonte': colors.BLACK},
        {'operador': '±', 'fundo': colors.BLUE_GREY_100,  'fonte': colors.BLACK},
        {'operador': '%', 'fundo': colors.BLUE_GREY_100,  'fonte': colors.BLACK},
        {'operador': '÷', 'fundo': colors.ORANGE , 'fonte': colors.WHITE}, 
        {'operador': '7', 'fundo': colors.WHITE24, 'fonte': colors.WHITE}, 
        {'operador': '8', 'fundo': colors.WHITE24, 'fonte': colors.WHITE}, 
        {'operador': '9', 'fundo': colors.WHITE24, 'fonte': colors.WHITE}, 
        {'operador': 'x', 'fundo': colors.ORANGE , 'fonte': colors.WHITE}, 
        {'operador': '4', 'fundo': colors.WHITE24, 'fonte': colors.WHITE}, 
        {'operador': '5', 'fundo': colors.WHITE24, 'fonte': colors.WHITE}, 
        {'operador': '6', 'fundo': colors.WHITE24, 'fonte': colors.WHITE}, 
        {'operador': '-', 'fundo': colors.ORANGE , 'fonte': colors.WHITE}, 
        {'operador': '1', 'fundo': colors.WHITE24, 'fonte': colors.WHITE}, 
        {'operador': '2', 'fundo': colors.WHITE24, 'fonte': colors.WHITE}, 
        {'operador': '3', 'fundo': colors.WHITE24, 'fonte': colors.WHITE}, 
        {'operador': '+', 'fundo': colors.ORANGE , 'fonte': colors.WHITE}, 
        {'operador': '0', 'fundo': colors.WHITE24, 'fonte': colors.WHITE}, 
        {'operador': ',', 'fundo': colors.WHITE24, 'fonte': colors.WHITE}, 
        {'operador': '=', 'fundo': colors.ORANGE , 'fonte': colors.WHITE}, 
    ]

    btn = [ft.Container(
        content = ft.Text(value=btn['operador'], color=btn['fonte']),
        width=50,
        height=50,
        bgcolor=btn['fundo'],
        border_radius=100,
        alignment=ft.alignment.center,
        on_click=select,
    )for btn in botoes]

# Linhas
    display = ft.Row(
        width=250,
        height=50,
        controls=[resultado],
        alignment= "end"
    )
    
    Keyboard = ft.Row(
        width=250, 
        wrap=True,
        controls=btn,
        alignment='end',
    )
    
    Cal.add(display, Keyboard)
    
ft.app(target=main)