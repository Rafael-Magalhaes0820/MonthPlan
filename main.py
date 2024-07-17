'''
MonthPlan 2.0 é um app para organização pessoal, onde o usuário irá inserir quanto dinheiro é recebido e quanto é gasto no mês.
O programa então fará os calculos necessários e retornará quanto dinheiro sobra no mês.
'''
pegabusao = False
output = 0
import tkinter as tk
import functions as fc

window = tk.Tk()
window.geometry('800x500')

label1 = tk.Label(window, text="MonthPlan", font=('Times New Roman', 30))
label1.pack()

frame = tk.Frame(window)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)
frame.columnconfigure(4, weight=1)
frame.columnconfigure(5, weight=1)
frame.columnconfigure(6, weight=1)
frame.columnconfigure(7, weight=1)
frame.columnconfigure(8, weight=1)
frame.columnconfigure(9, weight=1)



# Salario recebido
salarioLabel = tk.Label(frame, text= 'Informe seu salário', font=('Calibri', 18))
salarioLabel.grid(row=0, column=0, sticky = tk.W+tk.E)

salarioInput = tk.Entry(frame)
salarioInput.grid(row=0, column = 1, sticky=tk.W+tk.E)

# Saidas do mês
saidasLabel = tk.Label(frame, text= 'Informe o valor de saída(contas, dívidas)', font=('Calibri', 18))
saidasLabel.grid(row=2, column=0, sticky = tk.W+tk.E, pady=30)

saidasInput = tk.Entry(frame)
saidasInput.grid(row=2, column = 1, sticky=tk.W+tk.E, pady= 30)

# valor transporte

# Função para calcular o total
def calcular(event=None):
    global pegabusao
    if pegabusao == False:
        transp = 0
    else:
        transp = transpInput.get()

    salario = salarioInput.get()
    saidas = saidasInput.get()
    gasto = int(saidas) + int(transp)
    output = int(salario) - int(gasto)
    result.config(text='Resta ' + str(output))
    result.grid(row=7, column=0, pady = 20)

    print(output)
    
    return

def submit_input(event=None):
    value = salarioInput.get()
    print(f"Valor inputado: {value}")

def ChoiceSim(event=None):
    btnCalcular.grid(row=8, column = 0)
    pegaBusao = True
    transpLabel.grid_remove()
    transpSim.grid_remove()
    transpNo.grid_remove()
    transpInput.grid(row=4, column=1, sticky=tk.W+tk.E)
    transpTrueLabel.grid(row=4, column =0, sticky=tk.W+tk.E)
    print('Sim')
    return

def ChoiceNo(event=None):
    btnCalcular.grid(row=8, column = 0)
    pegaBusao = False
    print('No')
    return

# Transporte
transpLabel = tk.Label(frame, text= 'Você gasta com transporte?', font=('Calibri', 18))
transpLabel.grid(row=4, column =0, sticky=tk.W+tk.E)
transpSim = tk.Button(frame, text= 'Sim', font=('Nunito', 14), command=ChoiceSim)
transpSim.grid(row=4, column=1)
transpNo = tk.Button(frame, text= 'Não', font=('Nunito', 14), command=ChoiceNo)
transpNo.grid(row=4, column=2)

# Caso tenha gasto com transporte
transpTrueLabel = tk.Label(frame, text= 'Insira o valor gasto com transporte', font=('Calibri', 18))
transpInput = tk.Entry(frame)

# calcular
btnCalcular = tk.Button(frame, text='Calcular', font=('Calibri', 14), command=calcular)

frame.pack(fill='x')

result = tk.Label(frame, text= 'Resta ' + str(output), font=('Calibri', 18))


window.mainloop()



