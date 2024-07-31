from re import search

d = "SSNV79610-MX80-1"
mean = [    #список регулярных выражений для поиска HostName
    '[A-Z]{4}\d{5}-[A-Z]{2}\d{2}-\d'  #соответствует значению пример UAK6-CR4-B "[A-Z]{4}-[A-Z]{2}\d" {A-Z]\d-[A-Z]{2}\d-[A-Z]
]

for i in mean:
    print(len(d))
    print(search(i, d))

