from pyzabbix import ZabbixAPI
#zabx = ZabbixAPI(url='http://zabbix-mpls.noc.rt.ru/', user='a.pantyukhov', password='2цыч№УВС')
#answer = zabx.do_request('apiinfo.version')


def uninUtilStrgPasr(zabxIntc):
    """
    Функция обертка для получения скоростей и графиков для интерфейсов полученных от модуля parser по запросу utilization_string
    Получает список zabxList и дополнив его HighSpeed и ссылками на графики возвращает обратно
    :param zabxIntc: list
    :return: list
    """
    zabx = lognZabx()
    for intc in zabxIntc:
        hostID_A = getHostID(intc['host_A'], zabx)
        hostID_B = getHostID(intc['host_B'], zabx)
        itemIDHighSped = getIntcItemID(hostID_A, intc['intc_A'], 'HighSpeed', zabx)   #получаем itemID 'HighSpeed'
        itemIDBitsRecd = getIntcItemID(hostID_A, intc['intc_A'], 'Bits received', zabx)   #получаем itemID 'Bits received', 'Bits sent
        itemIDBitsSent = getIntcItemID(hostID_A, intc['intc_A'], 'Bits sent', zabx)   #получаем itemID 'Bits sent'
        intc['IP_A'] = getHostIntcIP(hostID_A, zabx)   #задаем значениев словаре intc ip host A
        intc['IP_B'] = getHostIntcIP(hostID_B, zabx)   #задаем значениев словаре intc ip host B
        intc['highSped'] = getItemVal(itemIDHighSped, zabx)   #задаем значениев словаре intc High Speed
        intc['linkGrah'] = getGrah([itemIDHighSped, itemIDBitsRecd, itemIDBitsSent], 'speed')   #задаем ссылку на график  HighSpeed Bits received Bits sent
    logtZabx(zabx)
    return zabxIntc

def lognZabx(url="mpls"):
    """
    Функция авторизации
    :param url:
    :return:
    """
    if url == "mpls":
        return ZabbixAPI(url='http://zabbix-mpls.noc.rt.ru/', user='a.pantyukhov', password='2цыч№УВС')

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
    hostID = zabx.host.get(filter={'host':hostName})[0]['hostid'] #получаем host ID
    return hostID

def getHostIntcIP(hostID, zabx):
    """
    Функция поиска host interface ip
    :param hostID: str
    :return ip: str
    """
    hostIntcIP = zabx.hostinterface.get(hostids=hostID, output=['ip'])
    return hostIntcIP[0]['ip']

def getIntcItemID(hostID, intc, itemName, zabx):
    """
    Функция поиска item ID по host ID, номеру interface и строке содержащейсе в имене item
    :param hostID: str
    :param intc: str
    :param itemName: str
    :return itemID: str
    """
    itemID = str()
    items = zabx.item.get(hostids=hostID, output=['itemid', 'name', 'lastvalue'], search={"name":intc})
    for item in items:
        if itemName in item['name']:
            itemID = item['itemid']
            break
    if itemID == '': itemID = None
    return itemID

    #return items

def getItemVal(itemID, zabx):
    """
    Функция получения значения item по item ID
    :param itemID: str
    :return value: str
    """
    value = 0
    if itemID is None: value = None
    else:
        item = zabx.item.get(itemids=itemID, output=['name', 'lastvalue'])[0]
        for itemName in ['HighSpeed', 'Bits received', 'Bits sent']:
            if itemName in item['name']:
                value = int(item['lastvalue'])/10**9
                break
    return value

def getGrah(itemsID, typeGrah):
    """
    Функция на вход принимает список items ID и возврщает ссылку на график в соответствии с типом запроса (typeGrah):
    speed - High Speed, Bits received,  Bits sent
    status - Admin status, Operational status
    error - FSC
    :param itemsID: list
    :param type: str
    :return: str
    """
    if typeGrah == 'speed' or typeGrah == 'status':
        linkGrah = "http://zabbix-mpls.noc.rt.ru/history.php?action=batchgraph"
        for itemID in itemsID:
            linkGrah += "&itemids%5B{}%5D={}".format(itemID, itemID)
    elif typeGrah == 'error':
        linkGrah = "http://zabbix-mpls.noc.rt.ru/history.php?action=showgraph&itemids[]="+itemsID[0]
    return linkGrah

#zabx = lognZabx("mpls")


#        strgItem = "itemids%5B14175680%5D=14175680"

        #&itemids%5B14175680%5D=14175680&itemids%5B14175386%5D=14175386&itemids%5B14174504%5D=14174504&graphtype=0"
#http://zabbix-mpls.noc.rt.ru/history.php?action=batchgraph&itemids%5B14175827%5D=14175827&graphtype=0
#http://zabbix-mpls.noc.rt.ru/history.php?action=batchgraph&itemids%5B14175827%5D=14175827&itemids%5B14175974%5D=14175974&graphtype=0
#"http://zabbix-mpls.noc.rt.ru/history.php?action=batchgraph&itemids%5B14175680%5D=14175680&itemids%5B14175386%5D=14175386&itemids%5B14174504%5D=14174504&graphtype=0" highspeed bitsent bitreceveid
#"http://zabbix-mpls.noc.rt.ru/history.php?action=batchgraph&itemids%5B14175680%5D=14175680&itemids%5B14175386%5D=14175386&itemids%5B14174504%5D=14174504&graphtype=0"
#http://zabbix-mpls.noc.rt.ru/history.php?action=batchgraph&itemids%5B15497572%5D=15497572&itemids%5B15501256%5D=15501256&itemids%5B15502484%5D=15502484&graphtype=0
#http://zabbix-mpls.noc.rt.ru/history.php?action=batchgraph&itemids%5B15497572%5D=15497572&itemids%5B15501256%5D=15501256&itemids%5B15502484%5D=15502484&graphtype=0
#http://zabbix-mpls.noc.rt.ru/history.php?action=batchgraph&itemids%5B15497573%5D=15497573&itemids%5B15501257%5D=15501257&itemids%5B15502485%5D=15502485&graphtype=0
#http://zabbix-mpls.noc.rt.ru/history.php?action=showgraph&itemids[]=15494502 FSC
# host = 'KLNG-RGR4'
#
# intc = 'xe-1/3/2'
#
# hostID = getHostID(host)
# #print(hostID)
# itemID = getIntcItemID(hostID, intc, 'HighSpeed')
# print(itemID)
# itemVal = getItemVal(itemID)
# print(itemVal)
# itemsID = list()
# itemsID.append(itemID)
# print(type(itemsID))
# link = getGrah([str(15494502)], 'status')
# print(link)
# intcID = serhIntcID(hostID, intc)
# print(intcID)
# hostIntcID = serhHostIntcID(hostID)
# print(hostIntcID)


# for item in items:
#     print(item)


# for i in hostID:
#     print(i)