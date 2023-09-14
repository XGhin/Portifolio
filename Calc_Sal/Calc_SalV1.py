print("Responda da seguinte forma:\nPrimeiro: o total de horas.\nSegundo: os minutos que sobraram\nTerceiro: Quanto você ganha por hora.\n\n\n")
horas =  int(input("Quantas horas você trabalhou esse mes?\nHoras: "))
minutos =  int(input("\nQuantos minutos você trabalhou esse mes?\nMinutos: "))
minutos_total = (horas * 60) + minutos
ganho_hora = int(input("\nQuanto você ganha por hora??\nGanho por Hora: ")) / 60
salario = ganho_hora * minutos_total
print("\nEsse mês você deve receber R${:.2f} reais pelas {} horas e {} minutos de trabalho!".format(salario, horas, minutos))