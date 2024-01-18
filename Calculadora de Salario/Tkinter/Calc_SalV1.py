import tkinter as tk
import ttkbootstrap as ttk


# defs
def calcular_salario():
    horas = horas_variable
    minutos = minutos_variable
    ganho_hora = ganho_hora_variable
    salario = (horas + minutos) * (ganho_hora/60)
    
    print(salario)

# window
window = tk.Tk()
window.geometry("450x390")
# frames

linha1 = ttk.Frame(window, padding=5)
linha1.pack(side="top", fill="x")

linha2 = ttk.Frame(window, padding=5)
linha2.pack(side="top", fill="x")

linha3 = ttk.Frame(window, padding=5)
linha3.pack(side="top", fill="x")

linha4 = ttk.Frame(window, padding=5)
linha4.pack(side="top", fill="x")

linha5 = ttk.Frame(window, padding=5)
linha5.pack(side="top", fill="x")

linha6 = ttk.Frame(window, padding=5)
linha6.pack(side="top", fill="x")

linha7 = ttk.Frame(window, padding=5)
linha7.pack(side="top", fill="x")
# widgets
    # linha1
Welcome_Text = ttk.Label(linha1, text="Welcome", font="Arial 15 bold")
Welcome_Text.pack()

    # linha2
label_horas = ttk.Label(linha2, text="Quantas horas voce trabalhou?")
label_horas.pack(side='left', padx=20)
label_minutos = ttk.Label(linha2, text="Quantos minutos voce trabalhou?")
label_minutos.pack(side='right', padx=20)

    # linha3
entry_horas = ttk.Entry(linha3, width=25)
horas_variable = tk.IntVar()
entry_horas.pack(side='left', padx=20)
entry_minutos = ttk.Entry(linha3, width=28)
minutos_variable = tk.IntVar()
entry_minutos.pack(side='right', padx=20)

    # linha4
label_ganho_hora = ttk.Label(linha4, text="Quanto voce ganha por hora?")
label_ganho_hora.pack(padx=20)
    
    # linha5
entry_ganho_hora = ttk.Entry(linha5, width=25)
ganho_hora_variable = tk.IntVar()
entry_ganho_hora.pack(padx=20)

    # linha6
button_calc_sal = ttk.Button(linha6, text="Calcular Salario", command=calcular_salario)
button_calc_sal.pack(padx=20)

    # linha7
result_seu_salario = ttk.Label(linha7, text="___________")
result_seu_salario.pack(padx=20)





# run
window.mainloop()
