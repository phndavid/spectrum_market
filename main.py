import json
import random
import csv
operador = {"deltas": [
	{   "id": 1,
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

def delta(id, cqi, users):
	delta  = {
		"id": id,
		"cqi": cqi,
		"users": users,
		"totallyBW": totallyBW(users),
		"maxBW": maxBW(users)
	}	
	return delta

def createUser(id, bin_service, time_service): 
	bw = bwByService(time_service)
	sum_bw = sumBw(bw)
	user = {"user":id, "bin_service":bin_service, "time_service":time_service, "bw": bw, "sum_bw": sum_bw}	
	return user

def addUsers(size):
  users = []  
  for i in xrange(1,size+1):
  	bin_service = [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]
  	time_service = [0,0,0,0,0]
  	for i in xrange(1,5):
  		if bin_service[i] == 1:
  			time_service[i] = random.randint(1,20)
  	
  	users.append(createUser(i,bin_service, time_service))
  return users;

def bwByService(array):
	#ftp, web, video, voip, games
	bw = []
 	services =[467.20, 338.39, 53.02, 21.42, 21.42]
	for i in xrange(0,5):
		bwi = array[i] * services[i];
		bw.append(bwi)	
	return bw

def sumBw(array):
	sumBw = 0;
	for i in xrange(0,5):
		sumBw += array[i];
	return sumBw

def totallyBW(users):
	totallyBW = 0
	for user in users:
		sum_bw = user['sum_bw']
		totallyBW += sum_bw
	return totallyBW

def maxBW(users):
	maxBW = 0
	for user in users:
		sum_bw = user['sum_bw']
		if maxBW < sum_bw:
			maxBW = sum_bw
	return maxBW

def addDeltas(size):
	for i in xrange(1,size+1):		
		cqi = random.randint(1, 15)
		num_users = random.randint(1, 5);
		operador["deltas"].append(delta(i,cqi, addUsers(num_users)))

addDeltas(2)

with open('operador.json', 'w') as outfile:
    json.dump(operador, outfile)


f = csv.writer(open("operadors.csv", "wb+"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["MaxBW", "SumBW"])

for key,value in operador.iteritems():
	for son in value:
		f.writerow([son['maxBW'], son['totallyBW']])
