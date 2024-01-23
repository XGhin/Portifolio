import tkinter as tk
import ttkbootstrap as ttk
from Produtos import Produtos

# window
window = tk.Tk()
window.geometry("820x620")

# commands

def teste():
    print("teste")

def Add_New_Product():
    Produtos.

# frames
# esquerda
esquerda = ttk.Frame(window, padding=10)
esquerda.place(relx=0, rely=0, relwidth=0.5, relheight=1)
"""--------------------------------------------------------------------------------------------------"""
linha1_esquerda = ttk.Frame(esquerda, padding=5)
linha1_esquerda.place(relx=0, rely=0, relwidth=1, relheight=0.1)
"""--------------------------------------------------------------------------------------------------"""
linha2_esquerda = ttk.Frame(esquerda, padding=5)
linha2_esquerda.place(relx=0, rely=0.1, relwidth=1, relheight=0.1)
"""--------------------------------------------------------------------------------------------------"""
linha3_esquerda = ttk.Frame(esquerda, padding=5)
linha3_esquerda.place(relx=0, rely=0.2, relwidth=1, relheight=0.1)
"""--------------------------------------------------------------------------------------------------"""
linha4_esquerda = ttk.Frame(esquerda, padding=5)
linha4_esquerda.place(relx=0, rely=0.3, relwidth=1, relheight=0.1)
"""--------------------------------------------------------------------------------------------------"""
linha5_esquerda = ttk.Frame(esquerda, padding=5)
linha5_esquerda.place(relx=0, rely=0.4, relwidth=1, relheight=0.1)
"""--------------------------------------------------------------------------------------------------"""
"""--------------------------------------------------------------------------------------------------"""
# direita
direita = ttk.Frame(window, padding=10)
direita.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)
"""--------------------------------------------------------------------------------------------------"""
linha1_direita = ttk.Frame(direita, padding=5)
linha1_direita.place(relx=0, rely=0, relwidth=1, relheight=0.1)
"""--------------------------------------------------------------------------------------------------"""
linha2_direita = ttk.Frame(direita, padding=5)
linha2_direita.place(relx=0, rely=0.1, relwidth=1, relheight=0.1)
"""--------------------------------------------------------------------------------------------------"""
linha3_direita = ttk.Frame(direita, padding=5)
linha3_direita.place(relx=0, rely=0.2, relwidth=1, relheight=0.1)
"""--------------------------------------------------------------------------------------------------"""
linha4_direita = ttk.Frame(direita, padding=5)
linha4_direita.place(relx=0, rely=0.3, relwidth=1, relheight=0.1)
"""--------------------------------------------------------------------------------------------------"""
linha5_direita = ttk.Frame(direita, padding=5)
linha5_direita.place(relx=0, rely=0.4, relwidth=1, relheight=0.1)
"""--------------------------------------------------------------------------------------------------"""
# widgets
    # System Alerts
alerts_system_left = ttk.Label(linha1_esquerda, text="New Products", font="Arial 12 bold")
alerts_system_left.place(relx=0.5, rely=0.5, anchor='center')
"""--------------------------------------------------------------------------------------------------"""
alerts_system_right = ttk.Label(linha1_direita, text="Update Products", font="Arial 12 bold")
alerts_system_right.place(relx=0.5, rely=0.5, anchor='center')
"""--------------------------------------------------------------------------------------------------"""
"""--------------------------------------------------------------------------------------------------"""
    # Product Name
label_new_product = ttk.Label(linha2_esquerda, text="Nome do produto:")
label_new_product.place(relx=0.3, rely=0.5, anchor='e')
"""--------------------------------------------------------------------------------------------------"""
VAR_entry_new_product = tk.StringVar()
entry_new_product = ttk.Entry(linha2_esquerda, width="35", textvariable=VAR_entry_new_product)
entry_new_product.place(relx=0.3, rely=0.5, anchor='w')
"""--------------------------------------------------------------------------------------------------"""
label_update_product = ttk.Label(linha2_direita, text="Nome do produto:")
label_update_product.place(relx=0.3, rely=0.5, anchor='e')

VAR_entry_selected_product = tk.StringVar()
entry_selected_product = ttk.Entry(linha2_direita, width="35", textvariable=VAR_entry_selected_product)
entry_selected_product.place(relx=0.3, rely=0.5, anchor='w')
"""--------------------------------------------------------------------------------------------------"""
"""--------------------------------------------------------------------------------------------------"""
    # Product Quantity
label_new_product_quantity = ttk.Label(linha3_esquerda, text="Quantidade:")
label_new_product_quantity.place(relx=0.3, rely=0.5, anchor='e')
"""--------------------------------------------------------------------------------------------------"""
VAR_entry_new_product_quantity = tk.IntVar()
entry_new_product_quantity = ttk.Entry(linha3_esquerda, width="35", textvariable=VAR_entry_new_product_quantity)
entry_new_product_quantity.place(relx=0.3, rely=0.5, anchor='w')
"""--------------------------------------------------------------------------------------------------"""
label_update_product_quantity = ttk.Label(linha3_direita, text="Quantidade:")
label_update_product_quantity.place(relx=0.3, rely=0.5, anchor='e')
"""--------------------------------------------------------------------------------------------------"""
VAR_entry_update_product_quantity = tk.IntVar()
entry_update_product_quantity = ttk.Entry(linha3_direita, width="35", textvariable=VAR_entry_update_product_quantity)
entry_update_product_quantity.place(relx=0.3, rely=0.5, anchor='w')
"""--------------------------------------------------------------------------------------------------"""
    # Products Value
label_new_product_value = ttk.Label(linha4_esquerda, text="Valor:")
label_new_product_value.place(relx=0.3, rely=0.5, anchor='e')

VAR_entry_new_product_value = tk.DoubleVar()
entry_new_product_value = ttk.Entry(linha4_esquerda, width="35", textvariable=VAR_entry_new_product_value)
entry_new_product_value.place(relx=0.3, rely=0.5, anchor='w')
"""--------------------------------------------------------------------------------------------------"""
label_update_product_value = ttk.Label(linha4_direita, text="Valor:")
label_update_product_value.place(relx=0.3, rely=0.5, anchor='e')
"""--------------------------------------------------------------------------------------------------"""
VAR_entry_update_product_value = tk.DoubleVar()
entry_update_product_value = ttk.Entry(linha4_direita, width="35", textvariable=VAR_entry_update_product_value)
entry_update_product_value.place(relx=0.3, rely=0.5, anchor='w')
"""--------------------------------------------------------------------------------------------------"""
    # Buttons
# New Product
button_new_product = ttk.Button(linha5_esquerda, text="Adicionar", command=Add_New_Product)
button_new_product.place(relx=0.3, rely=0.5, anchor='e')


# run
window.mainloop()
