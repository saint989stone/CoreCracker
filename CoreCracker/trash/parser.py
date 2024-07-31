from trash import regular as regr, zabimax

strg="2022-05-04 10:35:37				PROBLEM		FRKT-CR4	Interface et-8/0/2(<< 100GE ae50 to M7-CR9-A 100GE9/0/7, NTC Fiord ID:RT-MSK-FRA-4, CMS-22-095198, SURMS-1178703 >>): Link change state UP to DOWN\n \
     2022-05-04 10:35:37				PROBLEM		M7-CR9-A	Interface 100GE9/0/7(<< 100GE ae50 to FRKT-CR4 et-8/0/2, NTC Fiord ID:RT-MSK-FRA-4, CMS-22-095198, SURMS-1178703 >>): Link change state UP to DOWN\n \
     2022-05-04 10:35:30				PROBLEM		FRKT-CR4	Interface et-2/1/5(<< 100GE ae50 to M7-CR9-A 100GE2/0/16, NTC Fiord ID:RT-MSK-FRA-3, cms 22-095198, SURMS-1178703 >>): Link change state UP to DOWN\n \
     2022-05-04 10:35:30				PROBLEM		M7-CR9-A	Interface 100GE2/0/16(<< 100GE ae50 to FRKT-CR4 et-2/1/5, NTC Fiord ID:RT-MSK-FRA-3, cms 22-095198, SURMS-1178703 >>): Link change state UP to DOWN\n \
     2022-05-04 10:35:30				PROBLEM		FRKT-CR4	Interface et-3/1/2(<< 100GE ae48 to M7-CR9-B 100GE3/0/15, NTC Fiord ID:RT-MSK-FRA-1, CMS-22-095170, SURMS-1178700 >>): Link change state UP to DOWN\n	 \
     2022-05-04 10:35:30				PROBLEM		FRKT-CR4	Interface et-2/0/2(<< 100GE ae48 to M7-CR9-B 100GE10/0/8, NTC Fiord ID:RT-MSK-FRA-2, CMS-22-095170, SURMS-1178700 >>): Link change state UP to DOWN\n		 \
     2022-05-04 10:35:30				PROBLEM		M7-CR9-B	Interface 100GE10/0/8(<< 100GE ae48 to FRKT-CR4 et-2/0/2, NTC Fiord ID:RT-MSK-FRA-2, CMS-22-095170, SURMS-1178700 >>): Link change state UP to DOWN\n"


def union(strg):
    zabxIntc = parsIntc(strg)
    zabxDirn = summDirn(zabxIntc)
    for i in zabxDirn:
        print(i)

def parsIntc(strg):      #функция удаления ненужных строк и преобрзования в список Host А и B
    """

    :param strg:
    :return:
    """
    zabxIntc = list()
    tempList = strg.split("\n")   #преобразуем строку в список строк по признаку переноса строк. выбираем нечетные строки
    for strg in tempList:   #Блок Функции перебора строк в списке
        if 'Link change state UP to DOWN' not in strg:   #по контрольному слову отсекаем неииформативные строки
            continue
        strgList = strg.split(' ')  #получаем список полученых из строки путем разделения по знаку пробела
        listHost = list()   #список найденных Host
        listIntc = list()   #список найденных Intc
        trgrDubl = False    #триггер проверки дублирования
        trgrRecd = True     #триггер записи в zabxIntc
        listChekIndx = list()

        for elem in strgList:   #Блок Функции перебора элеметов строк в списке
            host = regr.serhHost(elem)  #по средством функции проверяем элемент в списке шаблоном, функция возвращает значение соотвествующее последнему найденному шаблону. В обратном случае функция возвращает None
            if host is not None:   #если функция возвращает не пустое значение
                listHost.append(host)   #добавляем значение в список

            intc = regr.serhIntc(elem)    #осуществляем поиск в строках значения соответствющим рег. выражениям Host
            if intc is not None:    #осуществляем проверку не пустых полученных значений
                listIntc.append(intc[0])    #добавляем Intc в список

        for indx, elem in enumerate(zabxIntc):  # осуществляем проверку дублирования в списке путем проверки наличия в списке Host А соотвествущей Host B
            if elem.get('host_A') == listHost[-1]:     #получаем значение в словаре по ключу Host A
                trgrDubl = True     #вкллюаем тригер для дополнительной проверки интерф.
                listChekIndx.append(indx)   #добавляем индекс элемента в списке для проверки интерфейса

        if trgrDubl:    #проверка на дублирование Intc
            for indx in listChekIndx:   #проверка индексов
                if zabxIntc[indx].get('intc_A') == listIntc[-1]: trgrRecd = False   #осуществляем проверку IntcA c IntcB

        if trgrRecd:
            zabxIntc.append({'host_A' : listHost[0],
                             'IP_A': 0,
                             'intc_A' : listIntc[0],
                             'host_B' : listHost[-1],
                             'intc_B' : listIntc[-1],
                             'IP_B': 0,
                             'host_A_B': listHost[0] + ' _ ' + listHost[-1],
                             'host_B_A': listHost[-1] + ' _ ' + listHost[0],
                             'highSped': 0,
                             'linkGrah': 'link'
                             })
    zabxIntc = zabimax.uninUtilStrgPasr(zabxIntc) #получаем значение IP, HighSpeed и ссылки на графики

    return zabxIntc

def summDirn(zabxIntc):
    zabxDirn = list()
    for zI in zabxIntc: #осуществляем перебор словарей в списке zabbList после первой записи в zabbDirn переходим к след. словарю по trgrStop
        host_A_B = str
        host_B_A = str
        host_A = str
        host_B = str
        IP_A = str
        IP_B = str
        highSpedDown = int
        trgrFullRecd = False   #триггер для полной записи
        trgrUpdtRecd = False   #триггер для обновления записи
        trgrStop = False   #триггер для остановки проверки zI
        if len(zabxDirn) == 0:  #первая проверка когда список пустой. Осуществляем полную запись
            host_A_B = zI['host_A_B']
            host_B_A = zI['host_B_A']
            host_A = zI['host_A']
            host_B = zI['host_B']
            IP_A = zI['IP_A']
            IP_B = zI['IP_B']
            highSpedDown = zI['highSped']
            trgrFullRecd = True
            trgrStop = True
        else:   #если список не пустой осуществляем проверку в zabxDirn
             rateUpdt = int
             trgrUpdtRecd = False
             for zD in zabxDirn:    #осуществляем перебор с списке zabxDirn после первого совпадения под условия прерываем цикл и переходим к след. иттерации zabxIntc
                 if zI['host_A_B'] != zD['host_A_B']:   #осуществляем проверку по назначению A-B если они не равны
                     if zI['host_A_B'] != zD['host_B_A']:   #осуществляем проверку A-B и B-A на дублирования назначений если не равны значит запись отсутствует в ZabxDirn. Производим Полную запись
                         host_A_B = zI['host_A_B']
                         host_B_A = zI['host_B_A']
                         host_A = zI['host_A']
                         host_B = zI['host_B']
                         IP_A = zI['IP_A']
                         IP_B = zI['IP_B']
                         highSpedDown = zI['highSped']
                         trgrFullRecd = True
                         break
                     else:  #['Host A-B'] == zD['Host B-A'] если равны значит запись есть, но назначение указаное в ZabxDirn cоотвествует A-B c целью исключения дублирования назначений производим Обновление записи
                         highSpedDown = zD['highSpedDown'] + zI['highSped']
                         trgrUpdtRecd = True
                 elif zI['host_A_B'] == zD['host_A_B']:  #если равны значит даное назначение есть. Производим Обновление записи
                     highSpedDown = zD['highSpedDown'] + zI['highSped']
                     trgrUpdtRecd = True

                 if trgrUpdtRecd:   #осуществляем обновление записи
                     zD['highSpedDown'] = highSpedDown
                     trgrUpdtRecd = False
                     trgrStop = True
                     break

        if trgrFullRecd:    #осуществляем полную запись
            zabxDirn.append({'host_A_B': host_A_B,
                             'host_B_A': host_B_A,
                             'host_A': host_A,
                             'host_B': host_B,
                             'IP_A': IP_A,
                             'IP_B': IP_B,
                             'highSpedDown': highSpedDown
                             })
            trgrStop = True

        if trgrStop:
            continue
    return zabxDirn
    #список получаемый после удаления ненужных строк функ. deltRow
