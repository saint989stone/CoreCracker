from tkinter import *
from tkinter import messagebox
import re
import util4.regular as regr
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
    print(zabxDirn)

def parsZabx():      #функция удаления ненужных строк и преобрзования в список Host А и B
    tempList = zabx.get().split("\n")[0::2]    #преобразуем строку в список строк по признаку переноса строк. выбираем нечетные строки
    for strg in tempList:   #перебираем элементы строк в списке
        strgList = strg.split(' ')  #получаем список полученых из строки путем разделения по знаку пробела
        rate = int
        listHost = list()   #список найденных Host
        listIntc = list()   #список найденных Intc
        listRate = list()   #список скоростей Кфеу
        trgrDubl = False    #триггер проверки дублирования
        trgrRecd = True     #триггер записи в zabxIntc
        trgrIntcHuGi = False    #триггер проверки Intc Huawei Gi
        listChekIndx = list()

        for elem in strgList:   #перебираем элементы в списке значений
            host = regr.serhHost(elem)  #по средством функции проверяем элемент в списке шаблоном, функция возвращает значение соотвествующее последнему найденному шаблону. В обратном случае функция возвращает None
            if host is not None:   #если функция возвращает не пустое значение
                listHost.append(host)   #добавляем значение в список

            for patnIntc in regr.patnIntc:    #перебираем регулярные выражения Inst
                intc = re.search(patnIntc, elem)     #осуществляем поиск в строках значения соответствющим рег. выражениям Host
                intcTest = regr.serhIntc(elem) #заглушка для использования функции из regular. Необходимость zabbixAPI
                if intc is not None:    #осуществляем проверку не пустых полученных значений
                    listIntc.append(intc[0])    #добавляем Intc в список
                    #listRate.append(regr.patnIntc[patnIntc])   #в дальнейшем получаем скорость с помощью zabbixAPI
                    if patnIntc == 'Gi\d/\d{1,2}/\d{1,2}:\d': trgrIntcHuGi = True

        if trgrIntcHuGi:    #проверка Intc Huawei Gi
            if 10 in listRate: rate = 10
            elif 1 in listRate: rate = 1
            else: "Проверка"
        else: rate = int(sum(listRate)/2) #в противном случае производим расчет

        for indx, elem in enumerate(zabxIntc):  # осуществляем проверку дублирования в списке путем проверки наличия в списке Host А соотвествущей Host B
            if elem.get('Host A') == listHost[-1]:     #получаем значение в словаре по ключу Host A
                trgrDubl = True     #вкллюаем тригер для дополнительной проверки интерф.
                listChekIndx.append(indx)   #добавляем индекс элемента в списке для проверки интерфейса

        if trgrDubl:    #проверка на дублирование Intc
            for indx in listChekIndx:   #проверка индексов
                if zabxIntc[indx].get('Intc A') == listIntc[-1]: trgrRecd = False   #осуществляем проверку IntcA c IntcB

        if trgrRecd:
            zabxIntc.append({'Host A' : listHost[0],
                             'Intc A' : listIntc[0],
                             'Host B' : listHost[-1],
                             'Intc B' : listIntc[-1],
                             'Host A-B': listHost[0] + ' - ' + listHost[-1],
                             'Host B-A': listHost[-1] + ' - ' + listHost[0],
                             'Rate' : 0   #Необходимость zabbixAPI
                             })
def summDirn():
    for zI in zabxIntc: #осуществляем перебор словарей в списке zabbList после первой записи в zabbDirn переходим к след. словарю по trgrStop
        hostAB = str
        hostBA = str
        rateFull = int
        trgrFullRecd = False   #триггер для полной записи
        trgrUpdtRecd = False   #триггер для обновления записи
        trgrStop = False   #триггер для остановки проверки zI
        if len(zabxDirn) == 0:  #первая проверка когда список пустой. Осуществляем полную запись
            hostAB = zI['Host A-B']
            hostBA = zI['Host B-A']
            rateFull = zI['Rate']
            trgrFullRecd = True
            trgrStop = True
        else:   #если список не пустой осуществляем проверку в zabxDirn
             rateUpdt = int
             trgrUpdtRecd = False
             for zD in zabxDirn:    #осуществляем перебор с списке zabxDirn после первого совпадения под условия прерываем цикл и переходим к след. иттерации zabxIntc
                 if zI['Host A-B'] != zD['Host A-B']:   #осуществляем проверку по назначению A-B если они не равны
                     if zI['Host A-B'] != zD['Host B-A']:   #осуществляем проверку A-B и B-A на дублирования назначений если не равны значит запись отсутствует в ZabxDirn. Производим Полную запись
                         hostAB = zI['Host A-B']
                         hostBA = zI['Host B-A']
                         rateFull = zI['Rate']
                         trgrFullRecd = True
                         break
                     else:  #['Host A-B'] == zD['Host B-A'] если равны значит запись есть, но назначение указаное в ZabxDirn cоотвествует A-B c целью исключения дублирования назначений производим Обновление записи
                         rateUpdt = zI['Rate'] + zD['Rate']
                         trgrUpdtRecd = True
                 if zI['Host A-B'] == zD['Host A-B']:  #если равны значит даное назначение есть. Производим Обновление записи
                     rateUpdt = zI['Rate'] + zD['Rate']
                     trgrUpdtRecd = True

                 if trgrUpdtRecd:   #осуществляем обновление записи
                     zD['Rate'] = rateUpdt
                     trgrUpdtRecd = False
                     trgrStop = True
                     break

        if trgrFullRecd:    #осуществляем полную запись
            zabxDirn.append({'Host A-B': hostAB,
                             'Host B-A': hostBA,
                             'Rate': rateFull
                             })
            trgrStop = True

        if trgrStop:
            continue
    return 'yes'

zabxIntc = list()    #список получаемый после удаления ненужных строк функ. deltRow
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