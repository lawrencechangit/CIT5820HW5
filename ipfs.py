import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	json_object = json.dumps(data, indent = 4)
	
	files = {
    		'file': 'json_object'
	}
	
	projectId = "2LRLd1HNXgtfnG9eQ5OkDYy1Lqw"
	projectSecret = "50ea124b3ea0cbb760fae468e2554c5e"
	response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files, auth=(projectId,projectSecret))
	
	#print(response.text)
	cid=response.text[23:69]
	
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	params = (
	('arg',cid),
	)
	projectId = "2LRLd1HNXgtfnG9eQ5OkDYy1Lqw"
	projectSecret = "50ea124b3ea0cbb760fae468e2554c5e"
	
	response = requests.post('https://ipfs.infura.io:5001/api/v0/cat', params=params, auth=(projectId,projectSecret))
	json_object=response.text
	print(response)
	print(json_object)
	data=json_object
	print(data)
	
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
