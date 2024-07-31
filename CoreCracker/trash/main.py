from tkinter import *
from tkinter import messagebox
from re import search

def display():
    messagebox.showinfo("GUI Python", zabx.get())

def parsZabx():
    deltRow()
    findPont()

def deltRow():      #функция удаления ненужных строк и преобрзования в список точек А и B
    zabxRow = zabx.get().split("\n")    #преобразуем строку в список строк по признаку переноса строк
    for row in zabxRow:     #перебираем список строк
        for mean in meanDeltRow:    #перебираем список значений определяющий необходимые строки
            if mean in row:     #перебираем значения определяющие необходимые строки в zabx для разделения строки на списки
                zabxListDeltRow.append(row.split(mean))

def findPont():     #функция поиска по регулярным значениям точек и интерфейсов.
    for elem in zabxListDeltRow:
        for j in meanSepnPont:
            a = search(j, elem[0])
            print(type(a))


zabxListDeltRow = list()    #список получаемый после удаления ненужных строк функ. deltRow
meanDeltRow = ['(<<', '(\\"<<']    #значения определяющие необходимые строки в zabx и разделяющие точки А и B

zabxListSepnPont = list()
meanSepnPont = [    #список регулярных выражений для поиска HostName
    '[A-Z]{4}-[A-Z]{3}\d',  #соответствует значению пример KLNG-RGR4 "[A-Z]{4}-[A-Z]{3}\d"
    '[A-Z]{4}-[A-Z]{2}\d',  #соответствует значению пример FRKT-CR5 "[A-Z]{4}-[A-Z]{2}\d"
    '[A-Z]{3}\d-[A-Z]{2}\d-[A-B]'  #соответствует значению пример UAK6-CR4-B "[A-Z]{4}-[A-Z]{2}\d"
]

winw = Tk()
winw.title("GUI на Python")

zabx = StringVar()

zabxLabl = Label(text="Введите строку из Zabbix:")
zabxLabl.grid(row=0, column=0, sticky="w")

zabxEntr = Entry(textvariable=zabx)

zabxEntr.grid(row=0, column=1, padx=5, pady=5)

message_button = Button(text="Click Me", command=parsZabx)
message_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

winw.mainloop()
