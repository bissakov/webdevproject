import re

data = ''
with open('original.txt','r',encoding='utf8') as f:
    data = f.read()

data = data.replace(',\n];',']')
data = data.replace('export const products = ','')
data = data.replace('\'','\"')
data = data.replace('id:','\"id\":')
data = data.replace('name','\"name\"')
data = data.replace('price','\"price\"')
data = data.replace('description','\"description\"')
data = data.replace('category','\"category\"')
data = data.replace('link:','\"link\":')
data = data.replace('link2','\"link2\"')
data = data.replace('likes','\"likes\"')
data = data.replace('\" +\n','')

with open('products.json','w',encoding='utf8') as f2:
    f2.write(data)