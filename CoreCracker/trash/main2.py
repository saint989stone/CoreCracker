from tkinter import *
from tkinter import messagebox
import re
import regular
"""
Нужно сделать:
    1. Удалить проверенную строку после ТОчки А;
    2. Проверка на агрегаты;
    3. Проверка на наличие точки в Точке А Точки B;
    4. Если есть интерф. Huawei Gi проверить скорость с другой стороны
    ? в случае если есть перенос строк в строке из Zabbix продумать проверку на наличие
"""

def display():
    messagebox.showinfo("GUI Python", zabx.get())

def start():
    parsZabx()
    for i in zabxList:
        print(i)
    #findPont()

def parsZabx():      #функция удаления ненужных строк и преобрзования в список Host А и B
    tempList = zabx.get().split("\n")[0::2]    #преобразуем строку в список строк по признаку переноса строк. выбираем нечетные строки
    for strg in tempList:   #перебираем элементы строк в списке
        strgTemp = strg
        HostA = str
        IntcA = str
        HostB = str
        IntcB = str
        Rate = int
        listHost = list()   #список найденных Host
        listHostEnd = list()    #список значений индексов окончания в строке Hostname
        listIntc = list()   #список найденных Intc
        listIntcEnd = list()    #список значений индексов окончания в строке Intc
        listRate = list()
        trgrDubl = False    #триггер проверки дублирования
        trgrRecd = True
        listChekIndx = list()

        #блок цикла по внесению HostName
        for patn in regular.patnHost:   #перебираем регулярные выражения Host
            Temp = re.search(patn, strgTemp)  #осуществляем поиск строках значения соответствющим рег. выражениям Host
            if Temp is not None:    #осуществляем проверку не пустых полученных значений
                listHost.append(Temp[0])    #добавляем Host в список
                listHostEnd.append(Temp.end())      #добавляем значение индекса окончания Host в список
                strgTemp = strg.replace(strg[0:Temp.end()], '')  # удаляем проверенную часть строки после внесения в список Host A
                print(strgTemp)
        minHostEnd = min(listHostEnd)   #находим минимальный индекс
        indxMinHostEnd = listHostEnd.index(minHostEnd)  #по min индексу получаем индекс в списке соответствующий точке B
        HostA = listHost[indxMinHostEnd]    #по min индексу в списке получаем значение Host A
        #strgTemp = strg.replace(strg[0:minHostEnd], '')  # удаляем проверенную часть строки после внесения в список Host A

        maxHostEnd = max(listHostEnd)   #по max индексу получаем индекс в списке соответствующий точке B
        indxMaxHostEnd = listHostEnd.index(maxHostEnd)  # по min индексу получаем индекс в списке
        HostB = listHost[indxMaxHostEnd]    #по max индексу в списке получаем значение Host B
        #проверка на дублирование Host
        for indx, elem in enumerate(zabxList):      #осуществляем проверку дублирования в списке путем проверки наличия в списке Host А соотвествущей Host B
            if elem.get('Host A') == HostB:     #получаем значение в словаре по ключу Host A
                trgrDubl = True     #вкллюаем тригер для дополнительной проверки интерф.
                listChekIndx.append(indx)   #добавляем индекс элемента в списке для проверки интерфейса

        #блок цикла по внесению Intc
        for patn in regular.patnIntc:   #перебираем регулярные выражения Intc
            Temp = re.search(patn, strg)   #осуществляем поиск строках значения соответствющим рег. выражениям Intc
            if Temp is not None:    #осуществляем проверку не пустых полученных значений
                listIntc.append(Temp[0])    #добавляем Intc в список
                listIntcEnd.append(Temp.end())  #добавляем значение индекса окончания Inst в список
                listRate.append(regular.patnIntc[patn])
        Rate = listRate[0]
        minIntcEnd = min(listIntcEnd)
        indxMinIntcEnd = listIntcEnd.index(minIntcEnd)
        IntcA = listIntc[indxMinIntcEnd]

        maxIntcEnd = max(listIntcEnd)
        indxMaxIntcEnd = listIntcEnd.index(maxIntcEnd)
        IntcB = listIntc[indxMaxIntcEnd]

        #проверка на дублирование Intc
        if trgrDubl:
            for indx in listChekIndx:
                if zabxList[indx].get('Intc A') == IntcB: trgrRecd = False

        if trgrRecd:
            zabxList.append({'Host A' : HostA,
                             'Intc A' : IntcA,
                             'Host B' : HostB,
                             'Intc B' : IntcB,
                             'Rate' : Rate
                             })
                # IntcA = Temp[0]   #если значение поиска не пустое добавляем его в значение для добавления в список
                # strgTemp = strgTemp.replace(strgTemp[0:Temp.end()], '')     #удаляем проверенную часть строки
                # rate = patnIntc[patn]   #ищем по регулярному выражению тип интерфейса
                # break   #после первого нахождения шаблона прерываем цикл patnIntc

        # блок цикла по внесению информации по точке B
        # for patn in patnHost:
        #     Temp = re.search(patn, strgTemp)    #осуществляем поиск строках значения соответствющим рег. выражениям Host
        #     if Temp is not None:
        #         HostB = Temp[0]     #если значение поиска не пустое добавляем его в значение для добавления в список
        #         for zabxDict in zabxList:   #цикл проверки найденной Точки B в списке Точки A
        #             for key in zabxDict:
        #                 if key == 'Host A':
        #                     print(HostB)
        #                     print(zabxDict[key])
        #                     if HostB == zabxDict[key]:
        #                         print(HostB)


                #strgTemp = strgTemp.replace(strgTemp[0:Temp.end()], '')     #удаляем проверенную часть строки
                #break   #после первого нахождения шаблона прерываем цикл patnHost

zabxList = list()    #список получаемый после удаления ненужных строк функ. deltRow


winw = Tk()
winw.title("GUI на Python")

zabx = StringVar()

zabxLabl = Label(text="Введите строку из Zabbix:")
zabxLabl.grid(row=0, column=0, sticky="w")

zabxEntr = Entry(textvariable=zabx)

zabxEntr.grid(row=0, column=1, padx=5, pady=5)

message_button = Button(text="Click Me", command=start)
message_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

winw.mainloop()