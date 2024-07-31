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
    summDirn()

def parsZabx():      #функция удаления ненужных строк и преобрзования в список Host А и B
    tempList = zabx.get().split("\n")[0::2]    #преобразуем строку в список строк по признаку переноса строк. выбираем нечетные строки
    for strg in tempList:   #перебираем элементы строк в списке
        strgList = strg.split(' ')
        rate = int
        listHost = list()   #список найденных Host
        listIntc = list()   #список найденных Intc
        listRate = list()   #список скоростей Кфеу
        trgrDubl = False    #триггер проверки дублирования
        trgrRecd = True     #триггер записи в zabxList
        trgrIntcHuGi = False    #триггер проверки Intc Huawei Gi
        listChekIndx = list()
        #блок цикла по внесению HostName
        for elem in strgList:
            for patnHost in regular.patnHost:   #перебираем регулярные выражения Host
                host = re.search(patnHost, elem)  #осуществляем поиск строках значения соответствющим рег. выражениям Host
                if host is not None:    #осуществляем проверку не пустых полученных значений
                    listHost.append(host[0])    #добавляем Host в список

            for patnIntc in regular.patnIntc:    #перебираем регулярные выражения Inst
                intc = re.search(patnIntc, elem)     #осуществляем поиск в строках значения соответствющим рег. выражениям Host
                if intc is not None:    #осуществляем проверку не пустых полученных значений
                    listIntc.append(intc[0])    #добавляем Intc в список
                    listRate.append(regular.patnIntc[patnIntc])
                    if patnIntc == 'Gi\d/\d{1,2}/\d{1,2}:\d': trgrIntcHuGi = True

        if trgrIntcHuGi:    #проверка Intc Huawei Gi
            if 10 in listRate: rate = 10
            elif 1 in listRate: rate = 1
            else: "Проверка"
        else: rate = int(sum(listRate)/2) #в противном случае производим расчет

        for indx, elem in enumerate(zabxList):  # осуществляем проверку дублирования в списке путем проверки наличия в списке Host А соотвествущей Host B
            if elem.get('Host A') == listHost[-1]:     #получаем значение в словаре по ключу Host A
                trgrDubl = True     #вкллюаем тригер для дополнительной проверки интерф.
                listChekIndx.append(indx)   #добавляем индекс элемента в списке для проверки интерфейса

        if trgrDubl:    #проверка на дублирование Intc
            for indx in listChekIndx:   #проверка индексов
                if zabxList[indx].get('Intc A') == listIntc[-1]: trgrRecd = False   #осуществляем проверку IntcA c IntcB

        if trgrRecd:
            zabxList.append({'Host A' : listHost[0],
                             'Intc A' : listIntc[0],
                             'Host B' : listHost[-1],
                             'Intc B' : listIntc[-1],
                             'Host A-B': listHost[0] + ' - ' + listHost[-1],
                             'Host B-A': listHost[-1] + ' - ' + listHost[0],
                             'Rate' : rate
                             })
def summDirn():
    for zl in zabxList:
        hostAB = str
        hostBA = str
        rateFull = int
        trgrFullRecd = False
        trgrUpdtRecd = False
        trgrStop = False
        print(zl)
        if len(zabxDirn) == 0:  #первая проверка когда список пустой
            hostAB = zl['Host A-B']
            hostBA = zl['Host B-A']
            rateFull = zl['Rate']
            trgrFullRecd = True
        else:   #если список не пустой осуществляем проверку в zabxDirn
             rateUpdt = int
             trgrUpdtRecd = False
             for zd in zabxDirn:
                 print(zd)
                 if zl['Host A-B'] != zd['Host A-B']:   #осуществляем проверку по назначению A-B если они не равны
                     if zl['Host A-B'] != zd['Host B-A']:   #осуществляем проверку A-B и B-A на дублирования назначений если не равны значит запись отсутствует в ZabxDirn. Производим Полную запись
                         hostAB = zl['Host A-B']
                         hostBA = zl['Host B-A']
                         rateFull = zl['Rate']
                         trgrFullRecd = True
                     else:  #['Host A-B'] == zd['Host B-A'] если равны значит запись есть, но назначение указаное в ZabxDirn cоотвествует A-B c целью исключения дублирования назначений производим Обновление записи
                         rateUpdt = zl['Rate'] + zd['Rate']
                         trgrUpdtRecd = True
                 if zl['Host A-B'] == zd['Host A-B']:  #если равны значит даное назначение есть. Производим Обновление записи
                     rateUpdt = zl['Rate'] + zd['Rate']
                     trgrUpdtRecd = True

                 if trgrUpdtRecd:   #осуществляем обновление записи
                     zd['Rate'] = rateUpdt
                     trgrUpdtRecd = False
                     continue
                 if trgrFullRecd:  # осуществляем полную запись
                     zabxDirn.append({'Host A-B': hostAB,
                                      'Host B-A': hostBA,
                                      'Rate': rateFull
                                      })
                     trgrFullRecd = False
                     continue

        if trgrFullRecd:    #осуществляем полную запись
            zabxDirn.append({'Host A-B': hostAB,
                             'Host B-A': hostBA,
                             'Rate': rateFull
                             })
        # if trgrIntcRecd:
        #     zabxDirn.append('Rate': rate)
        print(zabxDirn)
        #
        #     else:
        #         if hostAB == j['Host A-B'] or hostAB == j['Host B-A']:
        #             i['Rate'] += j['Rate']


zabxList = list()    #список получаемый после удаления ненужных строк функ. deltRow
zabxDirn = list()


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