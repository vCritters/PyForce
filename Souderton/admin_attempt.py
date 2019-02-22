import requests

username = "admin"
password = "admin"

url = "http://" + username + ":" + password + "@10.88.0.1/Home"

r = requests.post(url)

print (r.content)
