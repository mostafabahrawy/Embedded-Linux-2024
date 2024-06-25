import requests 

url = requests.get('https://api.ipify.org/?format=json')
print(url.text)

print('-'*50)

url = requests.get('https://ipinfo.io/156.220.92.131/geo')
print(url.text)