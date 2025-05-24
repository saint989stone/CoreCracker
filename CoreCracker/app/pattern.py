patnHost = [    #список регулярных выражений для поиска HostName. Шаблоны располагаются по воссрастанию количества символов.

]
listHostExcn = [   #список для исключений найденных по регулярным выражениям определенных значений. Проблема DATA-IX
]

patnIntc = [
    '(?:ge|xe|et)(-\d{1,2}/\d{1,2}/\d{1,2})', #JUN xe-1/33/22 #ge-1/33/22
    #'ge-\d{1,2}/\d{1,2}/\d{1,2}',
    #'xe-\d{1,2}/\d{1,2}/\d{1,2}',
    #'et-\d{1,2}/\d{1,2}/\d{1,2}',
    'GigabitEthernet\d{1,2}/\d{1,2}/\d{1,2}',   #HUA GigabitEthernet11/1/8
    '100GE\d{1,2}/\d{1,2}/\d{1,2}',   #HUA 100GE9/0/7
    '10GE\d{1,2}/\d{1,2}/\d{1,2}',   #HUA 100GE9/0/7'
    'Gi\d{1,2}/\d{1,2}',   #Cisco Gi1/1
    'Gi\d{1,2}/\d{1,2}/\d{1,2}:\d',     #Cisco 'Gi\d/\d{1,2}/\d{1,2}:\d'
    '\d{1,2}/\d{1,2}/[Cc]\d{1,2}/\d{1,2}',    #Nokia 2/1/c34/1
    'GE\d{1,2}/\d{1,2}/\d{1,2}:\d{1,2}',   #GE7/0/9:1
    'GE\d{1,2}/\d{1,2}/\d{1,2}',   #GE-7/0/9:1
    '\d{1,2}/\d{1,2}/c\d{1,2}',  # NokiA 1/6/c7
    '\d{1,2}/\d{1,2}/\d{1,2}'  #NOKIA 1/1/1
]

patnIntcAggn = {
    'Interface ae\d{1,2}',  #ae45
    'Interface Eth-Trunk\d{1,2}', #Eth-Trunk45
    'Interface lag-\d{1,2}',   #lag-
    'Interface as',
    '-mpls'
}

patnDictZabxDirn = {
    'host_A_B': str,
    'host_B_A': str,
    'host_A': str,
    'host_B': str,
    'IP_A': str,
    'IP_B': str,
    'strm': str,
    'highSpedFull': 0,
    'highSpedUp': 0,
    'highSpedDown': 0,
    'bitsRecd': 0,
    'bitsSent': 0,
    'tredBitsRecdMax': 0,
    'tredBitsSentMax': 0,
    'tredBitsRecdMaxAvrg': 0,
    'tredBitsSentMaxAvrg': 0,
    'tredListClokDegnRecd': list(),
    'tredListClokDegnSent': list(),
    'tredListClokLoadRecd': list(),
    'tredListClokLoadSent': list(),
    'linkGrahStts': str,
    'linkGrahSpedFull': str,
    'linkGrahBitsRecd': str,
    'linkGrahBitsSent': str,
    'listIntcItem': list(),
    'listItemIDAdmnStts': list(),
    'listItemIDOperStts': list(),
    'listItemIDHighSped': list(),
    'listItemIDBitsRecd': list(),
    'listItemIDBitsSent': list(),
    'listIntcTrgr': list(),
    'listErrr': list()
}

patnDictZabxIntc = {
    'intc_A': str,
    'intc_B': str,
    'admnStts': str,
    'operStts': str,
    'highSped': 0,
    'bitsRecd': 0,
    'bitsSent': 0,
    'tredBitsRecdMax': 0,
    'tredBitsSentMax': 0,
    'itemIDAdmnStts': str,
    'itemIDOperStts': str,
    'itemIDHighSped': str,
    'itemIDBitsRecd': str,
    'itemIDBitsSent': str,
    'linkGrahStts': str,
    'linkGrahSped': str
}