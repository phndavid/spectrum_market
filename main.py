import json
operador = {"deltas": [
	{   "id": 1,
		"cqi": 2,
		"users":[
		   {"user":1, "bin_service":[1,0,1,0,1], "time_service":[1,0,1,0,1], "bw":[1,0,1,0,1]},
		   {"user":2, "bin_service":[1,0,1,0,1], "time_service":[1,0,1,0,1], "bw":[1,0,1,0,1]},
		   {"user":3, "bin_service":[1,0,1,0,1], "time_service":[1,0,1,0,1], "bw":[1,0,1,0,1]}
		]	
	},
	{   "id": 2,
		"cqi": 4,
		"users":[
		   {"user":1, "bin_service":[1,0,1,0,1], "time_service":[1,0,1,0,1], "bw":[1,0,1,0,1]},
		   {"user":2, "bin_service":[1,0,1,0,1], "time_service":[1,0,1,0,1], "bw":[1,0,1,0,1]},
		]	
	}
]}
#Nos imprime en pantalla data como un tipo de dato nativo.
print 'OPERADOR:', repr(operador)
#Nos devuelve el String con el JSON
data_string = json.dumps(operador)
print 'JSON:', data_string