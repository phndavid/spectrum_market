#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import json
import random
import csv

"""Participacion en el mercado operadores móviles
http://colombiatic.mintic.gov.co/602/articles-15639_infografia.png
Abonados en servicio telefonia móvil= 57'292.621
1) Claro: 49.47%
2) Moviestar: 22.79%
3) Tigo: 19.27%
4) Virgin mobile: 4.21%
5) Otros: 4.27%
"""

"""
Ejemplo del formato Json a utilizar.
"""
operador = {"deltas": [
	{   "id": 1,
		"escala_t": 1,
		"cqi": 2,
		"users":[
		   {"user":1, "bin_service":[1,0,1,0,1], "time_service":[2,0,4,0,3], "bw":[1,0,1,0,1], "sum_bw": 3},
		   {"user":2, "bin_service":[1,0,1,0,1], "time_service":[5,0,5,0,5], "bw":[1,0,1,0,1], "sum_bw": 3},
		   {"user":3, "bin_service":[1,0,1,0,1], "time_service":[2,0,2,0,2], "bw":[1,0,1,0,1], "sum_bw": 3}
		],
		"totallyBW": 9,
		"maxBW": 3	
	}
]}

"""
Metodo: createUser
Descripción: crea un objeto usuario de acuerdo a los parametros pasados. 
Parametros:
	- id:
	- cqi: calidad del canal
	- bin_service: binaria por servicio donde 0: no hace uso del servicio 1: hace uso del servicio
	- time_service:  cantidad de tiempo por servicio
"""
def createUser(id, cqi, bin_service, time_service): 
	bw = bwByService(cqi, time_service)
	sum_bw = sumBw(bw)
	user = {"user":id, "bin_service":bin_service, "time_service":time_service, "bw": bw, "sum_bw": sum_bw}	
	return user

"""
Metodo: addUsers
Descripción: crea un array con un número de usuarios n. 
Parametros:
	- cqi: calidad del canal
	- size: número de usuarios a crear. 
	- escala_t: escala en el tiempo (ej. 1min, 10min, 60min)
"""
def addUsers(cqi, size, escala_t):
  users = []  
  for i in xrange(1,(size+1)*escala_t):
  	bin_service = [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]
  	time_service = [0,0,0,0,0]
  	for i in xrange(1,5):
  		if bin_service[i] == 1:
  			time_service[i] = random.randint(1,20)
  	
  	users.append(createUser(i,cqi, bin_service, time_service))
  return users;

"""
Ecuación: 13
Metodo: bwByService
Descripción: calcula el ancho de banda por serivicio 
Parametros:
	- cqi: calidad del canal
	- array: lista de cantidades de tiempo por servicio.
"""
def bwByService(cqi, array):
	#ftp, web, video, voip, games
	bw = []
 	services =[467.20, 338.39, 53.02, 21.42, 21.42]
	for i in xrange(0,5):
		bwi = (services[i]/cqi)*array[i];
		bw.append(bwi)	
	return bw

"""
Metodo: sumBw
Descripción: calcula la suma total del ancho de banda por serivicio de un usuario.
Parametros:
	- array: lista de anchos de banda por servicio
"""
def sumBw(array):
	sumBw = 0;
	for i in xrange(0,5):
		sumBw += array[i];
	return sumBw

"""
Ecuación: 14
Metodo: sumBw
Descripción: calcula la suma total del ancho de banda por delta de t.
Parametros:
	- users: lista de usuarios en un delta t
"""
def totallyBW(users):
	totallyBW = 0
	for user in users:
		sum_bw = user['sum_bw']
		totallyBW += sum_bw
	return totallyBW

"""
Ecuación: 15
Metodo: sumBw
Descripción: calcula el ancho de banda  maximo por delta de t.
Parametros:
	- users: lista de usuarios en un delta t
"""
def maxBW(users):
	maxBW = 0
	for user in users:
		sum_bw = user['sum_bw']
		if maxBW < sum_bw:
			maxBW = sum_bw
	return maxBW

"""
Metodo: delta
Descripción: crea un objeto delta de acuerdo a los parametros pasados. 
Parametros:
	- id:
	- escala_t: escala en el tiempo (ej. 1min, 10min, 60min)
	- cqi: calidad del canal [1,15]
	- users: lista de usuarios por delta de t
"""
def delta(id, escala_t, cqi, users):
	delta  = {
		"id": id,
		"escala_t": escala_t,
		"cqi": cqi,
		"users": users,
		"totallyBW": totallyBW(users),
		"maxBW": maxBW(users)
	}	
	return delta

"""
Metodo: sumBw
Descripción: agrega un numero de deltas n a un operador
Parametros:
	- escala_t: escala en el tiempo (ej. 1min, 10min, 60min)
	- size: número de deltas.
	- size_users: número de usuarios por delta t.
"""
def addDeltas(escala_t, size, size_users):
	for i in xrange(1,size+1):		
		cqi = random.randint(1, 15)
		num_users = random.randint(1, size_users);
		operador["deltas"].append(delta(i,escala_t, cqi, addUsers(cqi, num_users, escala_t)))

"""
Permite crear todos los deltas t que tendrá un operador.
"""
addDeltas(1,2,60);

"""
Genera archivo en formato json con todos los datos del operador
"""
with open('operador.json', 'w') as outfile:
    json.dump(operador, outfile)

"""
Genera archivo en formato CSV con la suma y ancho de banda maximo de los delta de t.
"""
f = csv.writer(open("operadors.csv", "wb+"))
# Write CSV Header, If you dont need that, remove this line
f.writerow(["MaxBW", "SumBW"])

for key,value in operador.iteritems():
	for son in value:
		f.writerow([son['maxBW'], son['totallyBW']])
