import re
from app.pattern import patnHost, patnIntc, patnIntcAggn, listHostExcn

def serhHost(strg):   #функция поиску hostName на основании списка шаблонов
    hostList = list()
    for patn in patnHost:  # перебираем регулярные выражения Host
        host = re.search(patn, strg)  # осуществляем поиск строках значения соответствющим рег. выражениям Host
        if host is not None:  # осуществляем проверку не пустых полученных значений
            hostList.append(host[0])   #добавляем найденный hostname в список
    if len(hostList):   #если список не пустой
        host = hostList[-1]   #с целью избежания некорректного найденного шаблона отправляем последний найденный hostName (проблема UAK6-CR4-B - M7-CR9-A)
        if host in listHostExcn:
            return False
        else: return host

def serhIntc(strg):
    for patn in patnIntc:   #перебираем регулярные выражения Intc
        intc = re.search(patn, strg)   #осуществляем поиск строках значения соответствющим рег. выражениям Intc
        if intc is not None:   #осуществляем проверку не пустых полученных значений
            return intc

def serhIntcAggn(strg):
    for patn in patnIntcAggn:
        intc = re.search(patn, strg)
        if intc is not None:
            return True

def serhHostCEP(strg):
    hostList = ['error']
    patnList = ['error']
    lenhList = ['error']
    for patn in patnHost:  # перебираем регулярные выражения Host
        host = re.search(patn, strg)  # осуществляем поиск строках значения соответствющим рег. выражениям Host
        if host is not None:  # осуществляем проверку не пустых полученных значений
            hostList.append(host[0])
            patnList.append(patn)
            lenhList.append(len(host[0]))

    return hostList[-1], patnList[-1], lenhList[-1]

print(serhHost('10G:::39-YNTR-AR1[xe-0/0/0]:-----:gskalauhov:2015-06-25'))
