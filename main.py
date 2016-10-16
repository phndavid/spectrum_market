import json
operador = {"deltas": [
	{   "id": 1,
		"cqi": 2,
		"users":[
		   {"user":1, "bin_service":[1,0,1,0,1], "time_service":[2,0,4,0,3], "bw":[1,0,1,0,1]},
		   {"user":2, "bin_service":[1,0,1,0,1], "time_service":[5,0,5,0,5], "bw":[1,0,1,0,1]},
		   {"user":3, "bin_service":[1,0,1,0,1], "time_service":[2,0,2,0,2], "bw":[1,0,1,0,1]}
		]	
	},
	{   "id": 2,
		"cqi": 4,
		"users":[
		   {"user":1, "bin_service":[1,0,1,0,1], "time_service":[1,0,1,0,1], "bw":[1,0,1,0,1]},
		   {"user":2, "bin_service":[1,0,1,0,1], "time_service":[1,0,1,0,1], "bw":[1,0,1,0,1]}
		]	
	}
]}

def delta(id, cqi, users):
	delta  = {
		"id": id,
		"cqi": cqi,
		"users": users
	}
	return delta

def createUser(id, bin_service, time_service): 
 return {"user":id, "bin_service":bin_service, "time_service":time_service, "bw": bwByService(time_service)}	

def addUsers(size):
  users = []
  for i in xrange(0,size):
  	bin_service = [1,0,1,0,1]
  	time_service = [3,0,5,0,2]
  	users.append(createUser(i,bin_service, time_service))
  return users;

def bwByService(array):
	#ftp, web, video, voip, games
	bw = []
 	services =[467.20, 338.39, 53.02, 21.42, 21.42]
	for i in xrange(0,5):
		bw.append(array[i] * services[i])
	return bw

operador["deltas"].append(delta(10,10, addUsers(2)))
#Nos devuelve el String con el JSON
data_string = json.dumps(operador)
for key,value in operador.iteritems():
	for son in value:
		print son['id']
		print son['cqi']
		print son['users']
#		for user in users:
#			print user['bin_service']
