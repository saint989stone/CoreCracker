from pyzabbix import ZabbixAPI

def lognZabx(inst="mpls"):
    """
    Функция авторизации
    :param url:
    :return: obj
    """
    if inst == 'mpls':
        return ZabbixAPI(url='http://zabbix-mpls.noc.rt.ru/', user='a.pantyukhov', password='2цыч№УВС')
    elif inst == 'west':
        print("WEST")

def getHostID(hostName, zabx):
    """
    Функция поиска host ID по строковому значению hostName
    :param hostName: str
    :return hostID: str
    """
    try:
        hostID = zabx.host.get(filter={'host':hostName})[0]['hostid'] #получаем host ID
    except:
        return 0
    return hostID
zabx = lognZabx()
host = 'Data-IX'

print(getHostID(host, zabx))