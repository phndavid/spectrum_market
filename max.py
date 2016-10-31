import json
import csv

maxBWA = 0
sumBWA = 0
data = {"list": []}
with open('operadorA.json') as json_data:
    operador = json.load(json_data)
    for key,value in operador.iteritems():
		for son in value:
			sumBWA = sumBWA + son['maxBW']
			if(maxBWA < son['maxBW']):
				maxBWA = son['maxBW']

data['list'].append({'BW':maxBWA, 'sum':sumBWA})

maxBWB = 0
sumBWB = 0
with open('operadorB.json') as json_data:
    operador = json.load(json_data)
    for key,value in operador.iteritems():
		for son in value:
			sumBWB = sumBWB + son['maxBW']
			if(maxBWB < son['maxBW']):
				maxBWB = son['maxBW']

data['list'].append({'BW':maxBWB, 'sum': sumBWB})

maxBWC = 0
sumBWC = 0
with open('operadorC.json') as json_data:
    operador = json.load(json_data)
    for key,value in operador.iteritems():
		for son in value:
			sumBWC = sumBWC + son['maxBW']
			if(maxBWC < son['maxBW']):
				maxBWC = son['maxBW']

data['list'].append({'BW':maxBWC,'sum':sumBWC})

maxBWD = 0
sumBWD = 0
with open('operadorD.json') as json_data:
    operador = json.load(json_data)
    for key,value in operador.iteritems():
		for son in value:
			sumBWD =  sumBWD + son['maxBW']
			if(maxBWD < son['maxBW']):
				maxBWD = son['maxBW']

data['list'].append({'BW':maxBWD,'sum':sumBWD})

maxBWE = 0
sumBWE = 0
with open('operadorE.json') as json_data:
    operador = json.load(json_data)
    for key,value in operador.iteritems():
		for son in value:
			sumBWE =  sumBWE + son['maxBW']
			if(maxBWE < son['maxBW']):
				maxBWE = son['maxBW']

data['list'].append({'BW':maxBWE,'sum':sumBWE})

print data
"""
Genera archivo en formato CSV con la suma y ancho de banda maximo de los delta de t.
"""
f = csv.writer(open("operadores.csv", "wb+"))
# Write CSV Header, If you dont need that, remove this line
f.writerow(["MaxBW", "SumBW"])

for key,value in data.iteritems():
	for son in value:
		f.writerow([son['BW'], son['sum']])