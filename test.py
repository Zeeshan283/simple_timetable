import requests 

respone = requests.get('https://randomfox.ca/floof')

values =  respone.json()

print(values['image'])