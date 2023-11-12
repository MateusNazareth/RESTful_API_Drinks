import requests 

response = requests.get('HTTP://127.0.0.1:8000/drinks/7')


response = requests.post('HTTP://127.0.0.1:8000/drinks' body={"name":"testeconsumo", "description": "resultado teste consumo"})



print (response.json())
