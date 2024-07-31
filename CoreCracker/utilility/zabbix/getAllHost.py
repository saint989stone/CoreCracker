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
        return ZabbixAPI(url='http://zabbix-west.noc.rt.ru/', user='a.pantyukhov', password='2wsx#EDC')

def logtZabx(zabx):
    """
    Функция расавторизации
    :return:
    """
    zabx.user.logout()

zabx = lognZabx('mpls')

hostsMPLS = zabx.host.get(output=['host'])
#hosts = zabx.host.get(output=['host'])
for host in hostsMPLS:
    print(host)