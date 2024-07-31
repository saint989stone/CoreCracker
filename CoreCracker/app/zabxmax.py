from pyzabbix import ZabbixAPI
import app.regular as regr
from app import parser
from copy import deepcopy
from app.pattern import patnDictZabxIntc
from datetime import datetime
from math import ceil
import time

#zabx = ZabbixAPI(url='-', user='-', password='-')
#answer = zabx.do_request('apiinfo.version')


def uninUtilStrgIntcPasr(zabxIntc, inst):
    """
    Функция получает список интерфейсов от модуля parser по запросу utilization_strg
    Получает список zabxList словарей и дополнив его HighSpeed и ссылками на графики возвращает обратно
    :param zabxIntc: list
    :return: list
    """
    zabx = lognZabx(inst)
    for intc in zabxIntc:
        hostID_A = getHostID(intc['host_A'], zabx)
        itemIDHighSped = getIntcItemID(hostID_A, intc['intc_A'], 'HighSpeed', zabx)   #получаем itemID 'HighSpeed'
        itemIDBitsRecd = getIntcItemID(hostID_A, intc['intc_A'], 'Bits received', zabx)   #получаем itemID 'Bits received', 'Bits sent
        itemIDBitsSent = getIntcItemID(hostID_A, intc['intc_A'], 'Bits sent', zabx)   #получаем itemID 'Bits sent'
        intc['highSped'] = getItemVal(itemIDHighSped, 'spedIntr', zabx)   #задаем значениев словаре intc High Speed
        intc['linkGrahSped'] = getGrah([itemIDHighSped, itemIDBitsRecd, itemIDBitsSent], 'sped', 0, inst)   #задаем ссылку на график  HighSpeed Bits received Bits sent
        intc['listItemID'] = [itemIDHighSped, itemIDBitsRecd, itemIDBitsSent]
    logtZabx(zabx)
    return zabxIntc

def uninUtilDirn(zabxDirn, inst):
    """
    Функция получает список словарей направлений, содержащий hostname точек A и B
    :param listDirn:
    :return:
    """
    zabx = lognZabx(inst)
    listItemNameStts = ['Admin status', 'Operational status']
    listItemNameSped = ['HighSpeed', 'Bits received', 'Bits sent']
    #Блок функции первоначального формирования списка интерфейсов с указанием intc_A, intc_B, admin status
    for dirn in zabxDirn:
        listItemStts = getDirnIntcItem(dirn['host_A'], dirn['host_B'], itemName=listItemNameStts[0], value=0, zabx=zabx)  #Блок формирования списка интерфейсов по направленияем на осснове Admin Status. C получения значений intc_A, intc_B, admin status, а также добавления ItemID Admin Status
        for item in listItemStts:
            dictIntc = deepcopy(patnDictZabxIntc)
            intc_A, intc_B = parser.parsIntcItem(item['name'])   #получаем имена интерфейсов
            dictIntc['intc_A'] = intc_A
            dictIntc['intc_B'] = intc_B
            dictIntc['admnStts'] = getItemVal(item['itemid'], 'stts', zabx)
            dictIntc['itemIDAdmnStts'] = item['itemid']
            dirn['listIntcItem'].append(dictIntc)

    #Блок функции заполняющий инф. дополняющий список интерфейсов
    for dirn in zabxDirn:
        hostID_A = getHostID(dirn['host_A'], zabx)
        # Блок функции повторного обхода уже сформированного списка интерфейсов с указанием intc_A, intc_B, admin status
        for intc in dirn['listIntcItem']:
            operSttsID = getIntcItemID(hostID_A, intc['intc_A'], listItemNameStts[1], zabx, host_B=dirn['host_B'])
            highSpedID = getIntcItemID(hostID_A, intc['intc_A'], listItemNameSped[0], zabx, host_B=dirn['host_B'])
            bitsRecdID = getIntcItemID(hostID_A, intc['intc_A'], listItemNameSped[1], zabx, host_B=dirn['host_B'])
            bitsSentID = getIntcItemID(hostID_A, intc['intc_A'], listItemNameSped[2], zabx, host_B=dirn['host_B'])
            intc['operStts'] = getItemVal(operSttsID, 'stts', zabx)
            intc['highSped'] = getItemVal(highSpedID, 'spedIntr', zabx)
            intc['bitsRecd'] = getItemVal(bitsRecdID, 'spedFlot', zabx)
            intc['bitsSent'] = getItemVal(bitsSentID, 'spedFlot', zabx)
            intc['itemIDOperStts'] = operSttsID
            intc['itemIDHighSped'] = highSpedID
            intc['itemIDBitsRecd'] = bitsRecdID
            intc['itemIDBitsSent'] = bitsSentID
            intc['tredBitsRecdMax'] = getTredMax(intc['itemIDBitsRecd'], zabx)
            intc['tredBitsSentMax'] = getTredMax(intc['itemIDBitsSent'], zabx)
            intc['linkGrahStts'] = getGrah([intc['itemIDAdmnStts'], intc['itemIDOperStts']], 'stts', 0, inst)
            intc['linkGrahSped'] = getGrah([intc['itemIDHighSped'], intc['itemIDBitsRecd'], intc['itemIDBitsSent']], 'sped', 0, inst)

    #Блок функции выполняющий суммирование значений
    for dirn in zabxDirn:
        hostID_A = getHostID(dirn['host_A'], zabx)
        hostID_B = getHostID(dirn['host_B'], zabx)
        for intc in dirn['listIntcItem']:
            dirn['listItemIDAdmnStts'].append(intc['itemIDAdmnStts'])
            dirn['listItemIDOperStts'].append(intc['itemIDOperStts'])
            dirn['listItemIDHighSped'].append(intc['itemIDHighSped'])
            dirn['listItemIDBitsRecd'].append(intc['itemIDBitsRecd'])
            dirn['listItemIDBitsSent'].append(intc['itemIDBitsSent'])
            if intc['admnStts'] == 'Up':
                dirn['highSpedFull'] += intc['highSped']
                dirn['tredBitsRecdMax'] += intc['tredBitsRecdMax']
                dirn['tredBitsSentMax'] += intc['tredBitsSentMax']
                if intc['operStts'] == 'Up':
                    dirn['highSpedUp'] += intc['highSped']

                    dirn['bitsRecd'] += intc['bitsRecd']
                    dirn['bitsSent'] += intc['bitsSent']
                elif intc['operStts'] == 'Down': dirn['highSpedDown'] += intc['highSped']
        dirn['bitsRecd'] = round(dirn['bitsRecd'], 3)
        dirn['bitsSent'] = round(dirn['bitsSent'], 3)
        dirn['tredBitsRecdMax'] = round(dirn['tredBitsRecdMax'], 3)
        dirn['tredBitsSentMax'] = round(dirn['tredBitsSentMax'], 3)
        dirn['tredBitsRecdMaxAvrg'], dirn['tredListClokDegnRecd'], dirn['tredListClokLoadRecd'] = getTredAvrg(dirn['listItemIDBitsRecd'], zabx, dirn['highSpedUp'])
        dirn['tredBitsSentMaxAvrg'], dirn['tredListClokDegnSent'], dirn['tredListClokLoadSent'] = getTredAvrg(dirn['listItemIDBitsSent'], zabx, dirn['highSpedUp'])
        dirn['linkGrahStts'] = getGrah(dirn['listItemIDAdmnStts'] +
                                       dirn['listItemIDOperStts'],
                                       'stts', 0, inst)
        dirn['linkGrahSpedFull'] = getGrah(dirn['listItemIDHighSped'] +
                                           dirn['listItemIDBitsRecd'] +
                                           dirn['listItemIDBitsSent'],
                                           'sped', 0, inst)
        dirn['host_A_B'] = dirn['host_A'] + ' - ' + dirn['host_B']
        dirn['strm'] = 'Down' if dirn['tredBitsRecdMaxAvrg'] > dirn['tredBitsSentMaxAvrg'] else 'Up'
        dirn['linkGrahBitsRecd'] = getGrah(dirn['listItemIDBitsRecd'], 'sped', 1, inst)
        dirn['linkGrahBitsSent'] = getGrah(dirn['listItemIDBitsSent'], 'sped', 1, inst)
        # getTredAvrgTest(dirn['listIntcItem'], dirn['highSpedFull'], zabx)
        getTredAvrg2(dirn['listIntcItem'], zabx)
        if hostID_A: dirn['IP_A'] = getHostIntcIP(hostID_A, zabx)
        if hostID_B: dirn['IP_B'] = getHostIntcIP(hostID_B, zabx)
    logtZabx(zabx)
    return zabxDirn

def getTred(itemID, timeFrom, timeTill, zabx):
    dictTred = zabx.trend.get(itemids=itemID,
                             time_from=timeFrom,
                             time_till=timeTill,
                             output='extend',
                             limit='5000')
    return dictTred

def getTredAvrg2(listIntcItem, zabx):
    listItemIDOperStts = [intc['itemIDOperStts'] for intc in listIntcItem]   #формируем список соотвествующих itemID
    listDays = getTredSerhDays(listItemIDOperStts, zabx)   #получаем список временных периодов, когда ни один из интерфейсов не падал


def getTredSerhDays(itemID, zabx, val=2, perd=20):
    """
    Функция получающая на входе itemID и возвращающая список периодов вермени, когда itemID не равнялся данному значению
    :param itemID:
    :param zabx:
    :param val:
    :param perd:
    :return:
    """
    listDays = list()
    tempListPerdDays = list()
    listPerdDays = list()
    day = 0
    while len(listDays) < perd:   #цикл while выполняется пока не наберется соответсвующее количество дней
        trgrStop = False
        timeTill = time.mktime(datetime.now().timetuple()) - ((3600 * 2) + (3600 * 24 * day))  # по какое время -2 часов от настоящего времени
        timeFrom = timeTill - (3600 * 24 * (day + 1))  # 4 hours # с какого времени -7 дней от вычисленного по какое времени
        dictTred = getTred(itemID, timeFrom, timeTill, zabx)
        for tred in dictTred:
            print(day, dislTimeTred(tred))
            if tred['value_max'] == str(val):  #если значение tred`a совпадает с ссоотвествущим значением
                trgrStop = True  #взводим триггер
                break   #прерываем цикл for
        if day > 180:
            break
        if trgrStop:
            day += 1
            continue
        else:
            listDays.append(day)
            day += 1
    print(listDays)
    for cout, day in enumerate(listDays):
        print(cout)
        if cout == 0: tempListPerdDays.append([day])   #создаем список в списке с началом периода
        else: #сравниваем предущее значение в списке с текущим
            if day - tempListPerdDays[-1][-1] >= 2:  #если разница больше или равна 2
                tempListPerdDays[-1].append(tempListPerdDays[-1][-1] + 1)   #добавляем в предыдущий список конец периода
                tempListPerdDays.append([day])   #создаем список в списке с началом периода
            else:
                tempListPerdDays[-1].append(day) # если разница составляет 1 добавляем текущее значение в конец периода предыдущего
    for cout, perdDays in enumerate(tempListPerdDays):
        if cout == len(tempListPerdDays) - 1:
            listPerdDays.append([tempListPerdDays[cout][0], tempListPerdDays[cout][-1]])
        else:
            listPerdDays.append([tempListPerdDays[cout][0], tempListPerdDays[cout][-2]])

    print(listDays)
    print(tempListPerdDays)
    print(listPerdDays)

def dislTimeTred(tred):
    """
    Функция вовращающая форматированное время Tred
    :param tred:
    :return:
    """
    return "{0}: {1}".format(datetime.fromtimestamp(int(tred['clock']))
                                          .strftime("%x %X"), tred)



def getTredAvrg1(listIntcItem, highSpedFull, zabx, valType='max'):
    listDays = list()
    listOperStts = [intc['itemIDOperStts'] for intc in listIntcItem]
    day = 0
    for day in range(7):
        trgrStop = False
        timeTill = time.mktime(datetime.now().timetuple()) - ((3600 * 2) + (3600 * 24 * day))  # по какое время -6 часов от настоящего времени
        timeFrom = timeTill - (3600 * 24 * (day + 1))  # 4 hours # с какого времени -7 дней от вычисленного по какое времени
        type = 'value_' + valType
        dictTredOperStts = zabx.trend.get(itemids=listOperStts,
                                  time_from=timeFrom,
                                  time_till=timeTill,
                                  output='extend',
                                  limit='5000')
        for tred in dictTredOperStts:
            print(day, dislTimeTred(tred))
            if tred['value_max'] == '2':
                trgrStop = True
                break
        if trgrStop:
            listDays.remove(day)
            continue
        else:
            listDays.append(day)
        day += 1

    print(listDays)
def uninUtilStrgDirnPasr(zabxDirn, inst):
    """
    Функция получает список направлений от модуля parser по запросу utilization_strg.
    Получает список zabxDirn и дополнив его возвращает обратно
    :param zabxDirn:
    :return:
    """
    zabx = lognZabx(inst)
    listItemName = ['HighSpeed', 'Bits received', 'Bits sent']
    for dirn in zabxDirn:   #перебираем направления точек A - B
        listItemID = list()  # список itemsID для формирования ссылки по направлениям (linkGrah)
        highSpedUp = int()
        highSpedDown = int()
        hostID_A = getHostID(dirn['host_A'], zabx)
        hostID_B = getHostID(dirn['host_B'], zabx)

        for itemName in listItemName:   #Цикл перебора всех item интерфейсов между точкой А и B. Перебираем соответствующие имена item
            listItem = getDirnIntcItem(dirn['host_A'], dirn['host_B'], itemName=itemName, value=1, zabx=zabx)   #от функции getDirnIntcItem получаем списки словарей, соотвествующие каждому елементу listItemName, содержащий item('itemid', 'name', 'lastvalue'), которые сейчас находятся в состоянии UP
            for item in listItem:   #перебираем списки словарей, соотвествующие каждому елементу listItemName
                if listItemName[0] in item['name']:   #для получения текущей емкости проверяем item HighSpeed
                    highSpedUp += getItemVal(item['itemid'], 'sped', zabx)  #cкладываем емкость с результирующей
                listItemID.append(item['itemid'])   #добавляем item id в результирующий список
        for intc in dirn['listIntcTrgr']:   #Цикл перебора item интерфейсов из строки триггеров
            for item in intc['listItemID']:   #добавляем item id результирующий список
                listItemID.append(item)
        if hostID_A: dirn['IP_A'] = getHostIntcIP(hostID_A, zabx)
        if hostID_B: dirn['IP_B'] = getHostIntcIP(hostID_B, zabx)
        dirn['highSpedFull'] = highSpedUp + dirn['highSpedDown']
        dirn['highSpedUp'] = highSpedUp
        dirn['linkGrah'] = getGrah(listItemID, 'sped', 0, inst)
    logtZabx(zabx)
    return zabxDirn

def getDirnIntcItem(host_A, host_B, itemName, value, zabx):
    """
    Функция получения items ID интерфейсов (без агрегатов) между указанным оборудованием cо следующимт параметрами:
    1. Имя item (HighSpeed, Bit Sent, Bit Receceid;
    2. Значением item (0-отсутствует; 1-присутвует)
    Возвращает список Items ID

    :param host_A: str
    :param host_B: str
    :param itemName: str
    :param value: str
    :param zabx: obj
    :return: list
    """
    listIntcItem = list()
    hostID_A = getHostID(host_A, zabx)  #получаем hostID точки A
    if host_B:
        items = zabx.item.get(hostids=hostID_A,   #получаем все items интерфейсов между точкой A и B по имени точки B
                          output=['itemid', 'name', 'lastvalue'],
                          search={'name': host_B})
    else:
        items = zabx.item.get(hostids=hostID_A,
                              output=['itemid', 'name', 'lastvalue'],
                              search={'name': 'Interface '})
    for item in items:
        if regr.serhIntcAggn(item['name']):   #пропускаем Аггрегирующие интерфейсы
            pass
        else:
            if itemName in item['name']:
                if int(item['lastvalue']) > value:
                    listIntcItem.append(item)
    return listIntcItem

def lognZabx(inst="mpls"):
    """
    Функция авторизации
    :param url:
    :return: obj
    """
    if inst == 'mpls':
        return ZabbixAPI(url='http://zabbix-mpls.noc.rt.ru/', user='a.pantyukhov', password='2цыч№УВС')
    elif inst == 'west':
        return ZabbixAPI(url='http://zabbix-west.noc.rt.ru/', user='a.pantyukhov', password='2wsx#EDC')

def logtZabx(zabx):
    """
    Функция расавторизации
    :return:
    """
    zabx.user.logout()

def getHostID(hostName, zabx):
    """
    Функция поиска host ID по строковому значению hostName
    :param hostName: str
    :return hostID: str
    """
    try:
        hostID = zabx.host.get(filter={'host':hostName})[0]['hostid'] #получаем host ID
    except:
        return False
    return hostID

def chekInst(host):
    zabxMpls = lognZabx('mpls')
    zabxWest = lognZabx('west')
    listInst = []
    dictInstHostID = {'mpls' : getHostID(host, zabxMpls),
                      'west' : getHostID(host, zabxWest)}
    for inst, hostID in dictInstHostID.items():
        if hostID is not False: listInst.append(inst)
    return listInst

def chekHostID(listHost):
    zabxMpls = lognZabx('mpls')
    zabxWest = lognZabx('west')
    listHostErrr = []
    for host in listHost:
        hostIDMpls = getHostID(host, zabxMpls)
        hostIDWest = getHostID(host, zabxWest)
        if hostIDMpls is not False or hostIDWest is not False:  #если найденные hostID в экземлярах Zabbix True
            pass
        else:   #если хотя бы один из найденных hostID в экземплярах Zabbix False
            listHostErrr.append(host)
    logtZabx(zabxMpls)
    logtZabx(zabxWest)
    return listHostErrr

def getHostIntcIP(hostID, zabx):
    """
    Функция поиска host interface ip
    :param hostID: str
    :return ip: str
    """
    hostIntcIP = zabx.hostinterface.get(hostids=hostID, output=['ip'])
    return hostIntcIP[0]['ip']

def getIntcItemID(hostID_A, intc, itemName, zabx, host_B=False):
    """
    Функция поиска item ID по host ID, номеру interface и строке содержащейсе в имене item
    :param hostID: str
    :param intc: str
    :param itemName: str
    :return itemID: str
    """
    itemID = str()
    items = zabx.item.get(hostids=hostID_A, output=['itemid', 'name', 'lastvalue'], search={"name":intc})

    if host_B:
        for item in items:
            if itemName in item['name'] and host_B in item['name']: #проверяем  содержание itemName на указание имени item (Admin Status) и Host_B. Проблема SPBR-CR4-A_SKTV-RGR3
                itemID = item['itemid']
                break
    else:
        for item in items:
            if itemName in item['name']:
                itemID = item['itemid']
                break
    if itemID == '': itemID = None
    return itemID

def getItemVal(itemID, typeVal, zabx):
    """
    Функция получения значения item по item ID
    :param itemID: str
    :param typeVal: str
    :return value: str
    """
    value = 0
    if itemID is None: value = None
    else:
        item = zabx.item.get(itemids=itemID, output=['name', 'lastvalue'])[0]
        lastVal = int(item['lastvalue'])
        if typeVal == 'spedIntr':
            value = int(lastVal / 10**9)
        elif typeVal == 'spedFlot':
            value = round(lastVal / 10**9, 3)
        elif typeVal == 'stts':
            if lastVal == 2: value = 'Down'
            elif lastVal == 1: value = 'Up'
    return value

def getTredMax (itemID, zabx, timePerd=7, valType='max'):
    """
    Функция на вход принимает item ID и возвращает значение в соответствии с type за период timePerd
    :param itemID:
    :param zabx:
    :param timePerd:
    :param type:
    :return:
    """
    timeTill = time.mktime(datetime.now().timetuple()) - 3600 * 6  # по какое время -6 часов от настоящего времени
    timeFrom = timeTill - 3600 * 24 * timePerd  # 4 hours # с какого времени -7 дней от вычисленного по какое времени
    valType = 'value_' + valType
    dictTred = zabx.trend.get(itemids=[itemID],
                              time_from=timeFrom,
                              time_till=timeTill,
                              output='extend',
                              limit='5000')
    listTred = [int(i[valType]) for i in dictTred]   #генератор списков перебирает словарь
    tred = round(max(listTred) / 10**9, 3)
    return tred

#def getTredAvrgTest(itemID, zabx, highSpedUp):


def getTredAvrg(itemID, zabx, highSpedUp, dayFrom=7, dayTill=0, valType='max'):
    """
    Функция на вход принимает item ID, составляет по-часовой список нагрузки в соответствии с периодом и typr.
    Возвращает среднее значение, оптиционально возвращает период времени деградации.

    :param itemID:
    :param zabx:
    :param highSpedUp:
    :param dayFrom:
    :param dayTill:
    :param valType:
    :return:
    """
    dictTredAvrg = dict()
    tredBitsAvrg = float()
    timeTill = time.mktime(datetime.now().timetuple()) - ((3600 * 6) + (3600 * 24 * dayTill))  # по какое время -6 часов от настоящего времени
    timeFrom = timeTill - (3600 * 24 * dayFrom)  # 4 hours # с какого времени -7 дней от вычисленного по какое времени
    type = 'value_' + valType
    dictTred = zabx.trend.get(itemids=itemID,
                              time_from=timeFrom,
                              time_till=timeTill,
                              output='extend',
                              limit='5000')

    # for i in dictTred:
    #      print(fortTime(i['clock']))

    listTred = [{datetime.fromtimestamp(i['clock']).strftime('%X')[0:5]: int(i[type])} for i in dictTred]  # генератор списков перебирает словарь и формирует список словарей где ключами является переформатирование datetime в формате 05:00:00, а значениями являются value определенного типа

    for i in listTred:  # Блок в котором Словарь в котором ключами явлется время, а значениями являются списки значений различных ITEM значения которых сняты в различные дни (прим. оставлено для проверки)
        clok, val = list(i.items())[0]  # получаем значения ключа(clock) и значения(value)
        if clok in dictTredAvrg:  # если ключ уже присутствует в словаре добавляем в список значение value
            dictTredAvrg[clok].append(val)
        else:  # если ключ отсутствует создаем список добавляем значение в словарь
            dictTredAvrg[clok] = list()
            dictTredAvrg[clok].append(val)
    # for key, value in dictTredAvrg.items():
    #      print(key, len(value), value)

    for clok, val in dictTredAvrg.items():
        dictTredAvrg[clok] = ceil((sum(val) / len(val)) * len(itemID) / 10**9)  # складываем все значения делим на количество значений в списке переводим в Гб/с и округляем до 3 знака для получения максимального значения по всем интерфейсам умножаем на количество элементов в переданном списке
    dictTredAvrg['24:00'] = dictTredAvrg['00:00']   #для правильного отображения периода времени добавляем в словарь значение для 24:00 равное 00:00
    dictTredAvrg = dict(sorted(dictTredAvrg.items(), key=lambda  x: x[0]))   #преобразуем словарь в кортеж [(key : val}], затем отсортировываем их по первому элементу и преобразовываем обра
    # for i in dictTredAvrg:
    #     print(i, dictTredAvrg[i])
    if valType == 'max':
        tredBitsAvrg = round(max(dictTredAvrg.values()), 3)  # получаем среднее значение в зависимимости от valType
    elif valType == 'min':
        tredBitsAvrg = round(min(dictTredAvrg.values()), 3)


        # clokSort = sorted(dictTredAvrg.keys())  # сортируем список ключей(времени)
    tempDegnList = [[]]
    for clok in dictTredAvrg:  # перебираем ключи
            # print(clok, dictTredAvrg[clok])
        if dictTredAvrg[clok] < highSpedUp:  # сравниваем значения с текущей емкостью если значения больше ничего не делаем
            tempDegnList.append([])  # добавляем пустой список
        else:  # если значение текущей емкости меньше
            tempDegnList[-1].append(clok)  # добавляем значение в последний добавленный список

        tredListClokDegn = [[elem[0], elem[-1]] for elem in tempDegnList if elem]  # генератор списков удаляет пустые списки и добавляет только начальное и конечное время
        return tredBitsAvrg, tredListClokDegn, dictTredAvrg

def getGrah(itemsID, typeItem, typeGrah, inst):
    """
    Функция на вход принимает список items ID и возврщает ссылку на график в соответствии с типом запроса (typeGrah):
    speed - High Speed, Bits received,  Bits sent
    status - Admin status, Operational status
    error - FSC
    :param itemsID: list
    :param type: str
    :return: str
    """
    #http://zabbix-west.noc.rt.ru/history.php?action=batchgraph&itemids%5B14361785%5D=14361785&itemids%5B14361965%5D=14361965&graphtype=0
    linkGrah = str()
    if inst == 'mpls': linkGrah += 'http://zabbix-mpls.noc.rt.ru/'
    elif inst == 'west': linkGrah += 'http://zabbix-west.noc.rt.ru/'
    if typeItem == 'sped' or typeItem == 'stts':
        linkGrah += 'history.php?action=batchgraph'
        for itemID in itemsID:
            linkGrah += "&itemids%5B{}%5D={}".format(itemID, itemID)
        linkGrah += '&graphtype={}'.format(str(typeGrah))
    elif typeItem == 'errr':
        linkGrah += 'history.php?action=showgraph&itemids[]={}'.format(itemsID[0])
    return linkGrah

