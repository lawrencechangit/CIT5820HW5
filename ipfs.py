import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	projectId = "<API_KEY>"
	projectSecret = "<API_KEY_SECRET>"
	response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=data, auth=(projectId,projectSecret))
	cid=response
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
