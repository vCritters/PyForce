import requests



username = "admin"
password = open().readline()


url = "http://" + username + ":" + password + "@10.88.0.1/Home"

r = requests.post(url)

print (r.content)
