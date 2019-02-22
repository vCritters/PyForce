import requests


username = "root"
password = "root"

url = "http://" + username + ":" + password + "@10.88.0.1/Home"

r = requests.post(url)

print (r.content)
