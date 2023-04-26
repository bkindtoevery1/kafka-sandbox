import requests
import json

headers = {
	'Content-Type': 'application/vnd.kafka.json.v2+json',
}

data = '{"records":[{"value":{"id":"jeonyeok"}}]}'

response = requests.post('http://localhost:8082/topics/please', headers=headers, data=data)

print(response)
print(json.dumps(response.json(), indent=4))
