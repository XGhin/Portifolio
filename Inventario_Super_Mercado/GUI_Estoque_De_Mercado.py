import tkinter as tk
import ttkbootstrap as ttk
from Controle_De_Estoque import Produtos

# Produtos Cadastrados
produtos_cadastrados = []

# defs
def teste():
    if novo_produto.get() in produtos_cadastrados:
        print(f"o produto {novo_produto.get()} já existe")
    else:
        produtos_cadastrados.append(novo_produto.get())
        print(f"o novo produto {novo_produto.get()} foi adicionado")

# window
window = tk.Tk()
window.geometry("450x390")


# Frames
    # esquerda
esquerda = ttk.Frame(window, padding=5)
esquerda.pack(side="left", fill="both")

linha1_esquerda = ttk.Frame(esquerda, padding=5)
linha1_esquerda.pack(side="top", fill="both")

linha2_esquerda = ttk.Frame(esquerda, padding=5)
linha2_esquerda.pack(side="top", fill="both")

linha3_esquerda = ttk.Frame(esquerda, padding=5)
linha3_esquerda.pack(side="top", fill="both")

    # esquerda
direita = ttk.Frame(window, padding=5)
direita.pack(side="right", fill="both")

linha1_direita = ttk.Frame(direita, padding=5)
linha1_direita.pack(side="top", fill="both")

linha2_direita = ttk.Frame(direita, padding=5)
linha2_direita.pack(side="top", fill="both")

linha3_direita = ttk.Frame(direita, padding=5)
linha3_direita.pack(side="top", fill="both")


# widgets
    # linha1_esquerda
label_novos_produtos = ttk.Label(linha1_esquerda, text="Cadastrar Novos Produtos", font="Arial 12 bold")
label_novos_produtos.pack(padx=5)

    # linha2_esquerda
label_nome = ttk.Label(linha2_esquerda, text="Nome do produto")
label_nome.pack(side="left", padx=5)

novo_produto = ttk.StringVar()
entry_nome_do_produto = ttk.Entry(linha2_esquerda, width="35", textvariable=novo_produto)
entry_nome_do_produto.pack(side="right", padx=5)

    # linha3_esquerda
button = ttk.Button(linha3_esquerda, text="Cadastrar", command=teste)
button.pack(padx=5)




    # linha1_direita
label_atualizar_produtos = ttk.Label(linha1_direita, text="Atualizar Produtos", font="Arial 12 bold")
label_atualizar_produtos.pack(padx=5)
# run
window.mainloop()