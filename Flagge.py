txt = b'Flagge_OSTD'
tXt = "Flagge_OST"
x = b'Flagge_S\xc3\x9cD'
txt= tXt.encode()
x=x.decode(encoding='UTF-8',errors='strict')
print (x+"STADT")