reglIntc = {
    'xe-\d/\d{1,2}/\d{1,2}' : 10,   #xe-1/33/22
    'Gi\d/\d{1,2}/\d{1,2}:\d' : (1, 10)     #'Gi\d/\d{1,2}/\d{1,2}:\d'
}

for key in reglIntc:
    print(key, reglIntc[key])