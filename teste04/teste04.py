sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
out = 19849.53

total = sp + rj + mg + es + out

psp = (float(sp/total)*100)
prj = (float(rj/total)*100)
pmg = (float(mg/total)*100)
pes = (float(es/total)*100)
pout = (float(out/total)*100)

print(f'Porcentagem faturamento SP: {psp:.2f} %')
print(f'Porcentagem faturamento RJ: {prj:.2f} %')
print(f'Porcentagem faturamento MG: {pmg:.2f} %')
print(f'Porcentagem faturamento ES: {pes:.2f} %')
print(f'Porcentagem faturamento Outros: {pout:.2f} %')
