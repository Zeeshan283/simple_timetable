import requests 

respone = requests.get('https://randomfox.ca/floof')

print(respone.status_code)

values =  respone.json()


print(values['image'])