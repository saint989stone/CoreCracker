"""
Retrieves history data for a given numeric (either int or float) item_id
"""

from pyzabbix import ZabbixAPI
from datetime import datetime
import time
from math import ceil
from functools import reduce

# The hostname at which the Zabbix web interface is available
#ZabbixAPI(url='http://zabbix-mpls.noc.rt.ru/', user='a.pantyukhov', password='2цыч№УВС')
# ZABBIX_SERVER = 'http://zabbix-mpls.noc.rt.ru/'
#
# zapi = ZabbixAPI(ZABBIX_SERVER)
#
# # Login to the Zabbix API
# zapi.login('Admin', 'zabbix')

zabx = ZabbixAPI(url='http://zabbix-mpls.noc.rt.ru/', user='a.pantyukhov', password='2цыч№УВС')

item_id = '17263581'

listItemID = [15447388, 15447408, 15447808, 15447811, 15447368, 15447428, 15447464, 15447464]

listItemIDHighSped = ['15455227', '15455211', '15455219']
listItemIDSpedRecd = ['15454163', '15454147', '15454155']




# Create a time range
time_till = time.mktime(datetime.now().timetuple()) - 3600 * 6 # по какое время -6 часов от настоящего времени
time_from = time_till - 3600 * 168  # 4 hours # с какого времени -7 дней от вычисленного по какое времени

# Query item's history (integer) data
# history = zabx.history.get(itemids=[item_id],
#                            time_from=time_from,
#                            time_till=time_till,
#                            output='extend',
#                            limit='5000',
#                            )

# If nothing was found, try getting it from history (float) data

dictTred = zabx.trend.get(itemids=listItemID,
                               time_from=time_from,
                               time_till=time_till,
                               output='extend',
                               limit='5000',
                               )

# Print out each datapoint

# listMaxxTred = [int(i['value_max']) for i in dictTred]
# maxxTred = round(max(listMaxxTred) / 10**9, 3)
# print(maxxTred)

# timeTest = datetime.fromtimestamp(1658599200).strftime('%X')
# print(timeTest, type(timeTest))

# for tred in dictTred:
#        print("{0}: {1}".format(datetime.fromtimestamp(int(tred['clock']))
#                                  .strftime("%x %X"), tred))

def fortTime(clok):
    clok = datetime.fromtimestamp(clok).strftime('%x %X')
    return clok


def getTredAvrg (itemID, zabx, highSpedUp=False, dayFrom=7, dayTill=0, valType='max'):
    dictTredAvrg = dict()
    tredBitsAvrg = float()
    timeTill = time.mktime(datetime.now().timetuple()) - ((3600 * 6) + (3600 * 24 * dayTill)) # по какое время -6 часов от настоящего времени
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

    for i in listTred:   #Блок в котором Словарь в котором ключами явлется время, а значениями являются списки значений различных ITEM значения которых сняты в различные дни (прим. оставлено для проверки)
        clok, val = list(i.items())[0]  #получаем значения ключа(clock) и значения(value)
        if clok in dictTredAvrg: #если ключ уже присутствует в словаре добавляем в список значение value
            dictTredAvrg[clok].append(val)
        else:   #если ключ отсутствует создаем список добавляем значение в словарь
            dictTredAvrg[clok] = list()
            dictTredAvrg[clok].append(val)
    # for key, value in dictTredAvrg.items():
    #      print(key, len(value), value)

    for clok, val in dictTredAvrg.items():
        dictTredAvrg[clok] = round((sum(val) / len(val)) / 10**9, 3) * len(itemID)   #складываем все значения делим на количество значений в списке переводим в Гб/с и округляем до 3 знака для получения максимального значения по всем интерфейсам умножаем на количество элементов в переданном списке
    # for key, value in dictTredAvrg.items():
    #     print(key, value)
    if valType == 'max': tredBitsAvrg = max(dictTredAvrg.values())   #получаем среднее значение в зависимимости от valType
    elif valType == 'min': tredBitsAvrg = min(dictTredAvrg.values())

    if highSpedUp:   #Блок функции Время деградации
        clokSort = sorted(dictTredAvrg.keys())   #сортируем список ключей(времени)
        tempDegnList = [[]]
        for clok in clokSort:   #перебираем ключи
            if dictTredAvrg[clok] < highSpedUp:  #сравниваем значения с текущей емкостью если значения больше ничего не делаем
                tempDegnList.append([])  #добавляем пустой список
            else:   #если значение текущей емкости меньше
                tempDegnList[-1].append(clok)   #добавляем значение в последний добавленный список
        degnClokList = [[elem[0], elem[-1]] for elem in tempDegnList if elem]   #генератор списков удаляет пустые списки и добавляет только начальное и конечное время
        print(tredBitsAvrg)
        return tredBitsAvrg, degnClokList

    return tredBitsAvrg

def getTredAvrg2(itemID, zabx, highSpedUp=False, dayFrom=7, dayTill=0, valType='max'):
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

    if highSpedUp:  # Блок функции Время деградации
        # clokSort = sorted(dictTredAvrg.keys())  # сортируем список ключей(времени)
        tempDegnList = [[]]
        for clok in dictTredAvrg:  # перебираем ключи
            #print(clok, dictTredAvrg[clok])
            if dictTredAvrg[clok] < highSpedUp:  # сравниваем значения с текущей емкостью если значения больше ничего не делаем
                tempDegnList.append([])  # добавляем пустой список
            else:  # если значение текущей емкости меньше
                tempDegnList[-1].append(clok)  # добавляем значение в последний добавленный список

        tredListClokDegn = [[elem[0], elem[-1]] for elem in tempDegnList if elem]  # генератор списков удаляет пустые списки и добавляет только начальное и конечное время
        # print(1, tredBitsAvrg, tredListClokDegn)
        return tredBitsAvrg, tredListClokDegn, dictTredAvrg

    return tredBitsAvrg, tredBitsAvrg, dictTredAvrg



valMax, listClokDegn, listClokLoad = getTredAvrg2(listItemID, zabx, highSpedUp=600)
# print(valMax, listClokDegn)
# for i in listClokLoad:
#     print(i, listClokLoad[i])


def getTred (itemID, zabx, dayFrom=7, dayTill=0, getTime=False, valType='max'):
    val = int()
    clok = int()
    tred = float()
    timeTill = time.mktime(datetime.now().timetuple()) - ((3600 * 6) + (3600 * 24 * dayTill)) # по какое время -6 часов от настоящего времени
    timeFrom = timeTill - (3600 * 24 * dayFrom)  # 4 hours # с какого времени -7 дней от вычисленного по какое времени
    type = 'value_' + valType
    dictTred = zabx.trend.get(itemids=[itemID],
                              time_from=timeFrom,
                              time_till=timeTill,
                              output='extend',
                              limit='5000')
    # print(fortTime(timeFrom))
    # print(fortTime(timeTill))
    listTred = [int(i[type]) for i in dictTred] #генератор списков перебирает словарь
    if valType == 'max':  #если тип искомого значения макс.
        val = max(listTred)
        tred = round(val / 10**9, 3)
    elif valType == 'min':
        val = min(listTred)  #если тип искомого значения мин.
        tred = round(val / 10**9, 3)
    if getTime:   #если требуется время наступления собятия
        clok = int()
        for i in dictTred:   #перебираем словарь
            if i[type] == str(val): clok = int(i['clock'])   #по неформатированному значению находим неформатированную дату.
        return tred, clok
    return tred

# value, clock = getTred(item_id, zabx, dayFrom=7, dayTill=0, getTime=True, valType='max')
# print(value, fortTime(clock))

# def getTredAvrg (itemID, zabx, dayFrom=8, dayTill=0, getTime=False, valType='max'):
#     listTred = list()
#     for i in range(dayTill + 1, dayFrom):
#         tred, clok = getTred(itemID, zabx, dayFrom=1, dayTill=i-1, getTime=True, valType='max')
#         # print(i, i-1, tred, fortTime(clok))
# #getTredAvrg(item_id, zabx)

#def getTredAvrg (itemID, zabx, timePerd=7, type='max', cout=5):
#     tred = float()
#     timeTill = time.mktime(datetime.now().timetuple()) - 3600 * 6  # по какое время -6 часов от настоящего времени
#     timeFrom = timeTill - 3600 * 24 * timePerd  # 4 hours # с какого времени -7 дней от вычисленного по какое времени
#     type = 'value_' + type
#     dictTred = zabx.trend.get(itemids=[itemID],
#                           time_from=timeFrom,
#                           time_till=timeTill,
#                           output='extend',
#                           limit='5000')
#     listTred = [int(i[type]) for i in dictTred]   #генератор списков перебирает словарь
#     for i in range(cout):   #цикл перебирает значения, отбирает cout макисмальных значений
#         val = max(listTred)
#         listTred.remove(val)
#         tred += val
#     tred = round((tred / 10 ** 9) / 5, 3)
#     return tred
#
# def getTredAvrgTime (itemID, zabx, days=7, type='max'):
#     tred = float()
#     timeTill = time.mktime(datetime.now().timetuple()) - 3600 * 6  # по какое время -6 часов от настоящего времени
#     timeFrom = timeTill - 3600 * 24 * timePerd  # 4 hours # с какого времени -7 дней от вычисленного по какое времени
#     type = 'value_' + type
#     dictTred = zabx.trend.get(itemids=[itemID],
#                           time_from=timeFrom,
#                           time_till=timeTill,
#                           output='extend',
#                           limit='5000')
#     listTred = [{int(i[type]), i['clock']} for i in dictTred]   #генератор списков перебирает словарь
#     for i in listTred:
#         print(i)
#     for i in range(cout):   #цикл перебирает значения, отбирает cout макисмальных значений
#         val = max(listTred)
#         listTred.remove(val)
#         tred += val
#     tred = round((tred / 10 ** 9) / 5, 3)
#     return tred

#getTredAvrgTime(item_id,zabx)
# value = getTredAvrg(item_id, zabx)
# print(value)

