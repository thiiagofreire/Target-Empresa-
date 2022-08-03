import json

f = open('teste03/dados.json')
dados = json.load(f)

aux = 0
max = 0
min = 0
s = 0
m= 0

for dia in dados:
    if (dia['valor']) != 0:
        aux = dia['valor']
        
        if (min == 0):
            min = aux
        elif (aux < min):
            min = aux

        if (aux > max):
            max = aux
                
        s += dia['valor']

        s += dia['valor']

print('Menor valor de faturamento do mês = R$ ' + str(min) + '.')
print('Maior valor de faturamento do mês = R$ ' + str(max) + '.')

m = s / len(dados)

DiasFat = ''

for i in dados:
    if (i['valor']) != 0:
        if (i['valor']) > m:
           DiasFat += (str(i['dia']) + ' ')
        
print('Dias que valor do faturamento diário foi acima da média mensal: ' + DiasFat)