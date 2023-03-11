import json

#a = {'herik':{"mãe":{"pai":{"marrom":["gordo","obeso"]}}}}
#print(a[0]['mãe']['pai'])

with open('bd_suporte.json','r',encoding='utf-8') as db:
    bd = json.load(db)

