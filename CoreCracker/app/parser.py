import app.regular as regr
from copy import deepcopy
from app import zabxmax
from app.pattern import patnDictZabxDirn


def uninUtilParsStrgTrgr(strg, inst):
    zabxIntc = parsIntcStrgTrgr(strg, inst)
    zabxDirn = summDirnStrgTrgr(zabxIntc, inst)
    return zabxDirn

def parsHosts(strg, inst):
    zabxDirn = list()
    tempList = list()
    trgrRecd = False
    if ',' in strg: tempList = strg.split(',') #проверка на указание нескольких элементов поиска
    else: tempList.append(strg)

    for elem in tempList:
        dictZabxDirn = deepcopy(patnDictZabxDirn)
        if elem == '':   #проверка на пустой элемент
             continue
        if '_' in elem:   #Блок Точка-А - Точка-Б. Присутствие означает что указывается направление Точка-А - Точка-Б
            trgrRecd = True   #включаем тригер добавления записи в результирующий список
            listHosts = elem.split('_')   #получаем список host_a и host_b
            if len(listHosts) != 2: dictZabxDirn['listErrr'].append('Несооствествие кол-ва точек формату Точка-А - Точка-Б') #Err
            for cout, host in enumerate(listHosts):   #перебираем host и счетчик
                if cout == 0:  #счетчик 0 соостветствует host_A
                    host_A = regr.serhHost(host) #Err продумать проверку на hostname
                    dictZabxDirn['host_A'] = host_A
                elif cout == 1:  #счетчик 0 соостветствует host_B
                    host_B = regr.serhHost(host)
                    dictZabxDirn['host_B'] = regr.serhHost(host_B)
        else:   #Блок Точка-А - Соседи
            host_A = regr.serhHost(elem)   #Errr
            listHost_B = list()
            zabx = zabxmax.lognZabx(inst)
            listIntcItem = zabxmax.getDirnIntcItem(host_A, False, 'Admin status', value=0, zabx=zabx)   #получаем список item по Admin status для получения host_B
            for item in listIntcItem:   #перебираем список item
                host_B = regr.serhHost(item['name'])   #находим hostname по регулярным выражениям
                if host_B: listHost_B.append(host_B)   #если функция возвражет значение производим запись
            for host_B in set(listHost_B):
                dictZabxDirn = deepcopy(patnDictZabxDirn)
                dictZabxDirn['host_A'] = host_A
                dictZabxDirn['host_B'] = host_B
                zabxDirn.append(dictZabxDirn)
        if trgrRecd: zabxDirn.append(dictZabxDirn)   #производим запись в результирующий список для Блок Точка-А - Точка-Б.
    zabxDirn = zabxmax.uninUtilDirn(zabxDirn, inst)
    return zabxDirn

def parsIntcItem(strg):
    """
    Функция парсер строки Item Name для поиска Интерфейсов
    :param strg:
    :return:
    """
    listIntc = list()
    strgList = strg.split(' ')
    for elem in strgList:
        intc = regr.serhIntc(elem)
        if intc is not None:
            listIntc.append(intc[0])
    return listIntc[0], listIntc[-1]

def parsIntcStrgTrgr(strg, inst):      #функция удаления ненужных строк и преобрзования в список Host А и B
    """
    Функция-парсер строк тригеров Zabbix.
    На входе получает строку с тригерами. Возвращает список словарей интерфейсов очищенный от дублированных записей
    :param strg: str
    :return: list
    """
    zabxIntc = list()
    tempList = strg.split('\n')   #преобразуем строку в список строк по признаку переноса строк. выбираем нечетные строки
    for strg in tempList:   #Блок Функции перебора строк в списке
        if regr.serhIntcAggn(strg) or 'Link change state' not in strg: #по контрольному слову отсекаем неинформативные строки и интерфейсы-агрегаты
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
                             'intc_A' : listIntc[0],
                             'host_B' : listHost[-1],
                             'intc_B' : listIntc[-1],
                             'host_A_B': listHost[0] + ' - ' + listHost[-1],
                             'host_B_A': listHost[-1] + ' - ' + listHost[0],
                             'highSped': 0,
                             'linkGrahSped': 'link',
                             })
    zabxIntc = zabxmax.uninUtilStrgIntcPasr(zabxIntc, inst) #получаем значение IP, HighSpeed и ссылки на графики
    return zabxIntc

def summDirnStrgTrgr(zabxIntc, inst):
    """
    Функция объединения интерфейсов по направлениям А-B.
    На входе получает список интерфейсов от функции parsIntc. Возвращает список словарей направлений, в который включен список словарей интерфейсов
    :param zabxIntc:
    :return:
    """
    zabxDirn = list()
    zabxDirnTemp = list()   #временный список который содержит только направления A_B и B_A уже внесенные в zabxDirn
    lamdAggnHighSped = lambda intc_A, highSped: 0 if regr.serhIntcAggn(intc_A) else highSped   #анонимная функция проверки intc принадлежности интерфейса к агрегату. В случае Агрегата возвращает 0, иначе скорость интерфейса
    for zI in zabxIntc: #осуществляем перебор словарей в списке zabbList после первой записи в zabbDirn переходим к след. словарю по trgrStop
        host_A_B = str
        host_B_A = str
        host_A = str
        host_B = str
        dictIntc = dict
        trgrFullRecd = False   #триггер для полной записи
        trgrUpdtRecd = False   #триггер для обновления записи
        trgrStop = False   #триггер для остановки проверки zI
        # inst = str   #переменная хранит значение экземпляра Zabbix. Определяется по одной из Точек А из списка
        if zI['host_A_B'] not in zabxDirnTemp or zI['host_B_A'] not in zabxDirnTemp:  #Проверка на первую запись Направления (Полная запись). Проверка на осуществление записи данного напраавления с списке zabxDirnTemp
            zabxDirnTemp.append(zI['host_A_B'])
            zabxDirnTemp.append(zI['host_B_A'])
            host_A_B = zI['host_A_B']
            host_B_A = zI['host_B_A']
            host_A = zI['host_A']
            host_B = zI['host_B']
            dictIntc = {
                'intc_A': zI['intc_A'],
                'intc_B': zI['intc_B'],
                'highSped': zI['highSped'],
                'linkGrahSped': zI['linkGrahSped'],
                'listItemID': zI['listItemID']
            }
            trgrFullRecd = True
            trgrStop = True
        else:   #Проверка на обновление существующей записи. Если данное напрвление уже есть в списке zabxDirnTemp
            trgrUpdtRecd = False
            for zD in zabxDirn:    #осуществляем перебор с списке zabxDirn после первого совпадения под условия прерываем цикл и переходим к след. иттерации zabxIntc
                if zI['host_A_B'] == zD['host_A_B']:   #осуществляем проверку по назначению A-B и A-B если они равны производим обновление записи
                    dictIntc = {
                        'intc_A': zI['intc_A'],
                        'intc_B': zI['intc_B'],
                        'highSped': zI['highSped'],
                        'linkGrahSped': zI['linkGrahSped'],
                        'listItemID': zI['listItemID']
                    }
                    trgrUpdtRecd = True
                elif zI['host_A_B'] == zD['host_B_A']:  #осуществляем проверку по назначению A-B и B-A если они равны производим обновление записи. Меняем местами intc_A и intc_B
                    dictIntc = {
                        'intc_A': zI['intc_B'],
                        'intc_B': zI['intc_A'],
                        'highSped': zI['highSped'],
                        'linkGrahSped': zI['linkGrahSped'],
                        'listItemID': zI['listItemID']
                    }
                    trgrUpdtRecd = True
                else:
                    continue
                if trgrUpdtRecd:   #осуществляем обновление записи
                    zD['listIntcTrgr'].append(dictIntc)
                    trgrStop = True
                    break

        if trgrFullRecd:    #осуществляем полную запись
            dictZabxDirn = deepcopy(patnDictZabxDirn)
            dictZabxDirn['host_A_B'] = host_A_B
            dictZabxDirn['host_B_A'] = host_B_A
            dictZabxDirn['host_A'] = host_A
            dictZabxDirn['host_B'] = host_B
            dictZabxDirn['listIntcTrgr'].append(dictIntc)
            zabxDirn.append(dictZabxDirn)
            trgrStop = True

        if trgrStop:
            continue
    # inst = zabxmax.chekInst(zabxDirn[0]['host_A'])
    zabxDirn = zabxmax.uninUtilDirn(zabxDirn, inst)   #переменная хранит значение экземпляра Zabbix. Определяется по одной из Точек А из списка
    return zabxDirn



