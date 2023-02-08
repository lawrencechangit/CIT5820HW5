import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	#print(data.keys())
	print(data)
	json_object = json.dumps(data, indent = 4)
	print(json_object)
	
	files = {
    		'file': 'json_object'
	}
	
	projectId = "2LRLd1HNXgtfnG9eQ5OkDYy1Lqw"
	projectSecret = "50ea124b3ea0cbb760fae468e2554c5e"
	response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files, auth=(projectId,projectSecret))
	cid=response.text
	print(response)
	hash=cid.get("Hash")
	print("cid is ", hash)
	
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
