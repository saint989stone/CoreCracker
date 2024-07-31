from pyzabbix import ZabbixAPI
zabi = ZabbixAPI(url='http://zabbix-mpls.noc.rt.ru/', user='a.pantyukhov', password='2цыч№УВС')
host_get_id = zabi.host.get(output=['hostid','host'], filter={'name':'KLNG-RGR4'})
print(host_get_id)
print(host_get_id[0]['hostid'])
l='M10-CR9-A'
item_get2 = zabi.item.get(hostids=host_get_id[0]['hostid'], output=['itemid','name','lastvalue','lastclock','key_'], search={'name':l})
HighSpeed=0
HighSpeed_Admin_status_up=0
bits_received=0
bits_sent=0
index_interface=''
list_if_id_adm=[]
list_if_id_oper=[]
for item in item_get2:

        if 'Interface ae' not in item['name'] and 'Interface as' not in item['name'] and '-mpls' not in item[
            'name'] and 'Interface Eth-Trunk' not in item['name'] and 'Interface lag' not in item['name']:
            if ': Admin status' in item['name']:
                if item['lastvalue'] == '1':
                    print('Admin status', item['lastvalue'],'KEY', item['key_'].split('.')[-1][:-1])
            if ': Operational status' in item['name']:
                if item['lastvalue'] == '1':
                    print('Operational status', item['lastvalue'], 'KEY', item['key_'].split('.')[-1][:-1])
            if ': Bits received' in item['name']:
                bits_received += int(item['lastvalue'])
                print('Bits received', bits_received)

            if ': Bits sent' in item['name']:
                bits_sent += int(item['lastvalue'])
                print('Bits sent', bits_sent)