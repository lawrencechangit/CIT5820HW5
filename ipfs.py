import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	print(data.keys())
	print(data)
	json_object = json.dumps(data, indent = 4)
	print(json_object)
	
	projectId = "4948f0dbf13c4f82993af603b0ef4329"
	projectSecret = "7e395492a0db48f4a0d7f8244902edd7"
	response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=json_object, auth=(projectId,projectSecret))
	cid=response
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
