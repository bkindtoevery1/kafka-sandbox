import requests
import json

headers = {
    'Content-Type': 'application/vnd.kafka.v2+json',
}

data = '{"topics":["please"]}'

response = requests.post('http://localhost:8082/consumers/consumer_a/instances/jeonmun_hasa/subscription', headers=headers, data=data)

print(response)
print(response.text)
