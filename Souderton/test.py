import requests

password_url = 'https://github.com/vCritters/PyForce/blob/master/Password_Lists/password_list_1.txt'

username = "admin"
password = open().readline()


url = "http://" + username + ":" + password + "@10.88.0.1/Home"

r = requests.post(url)

print (r.content)
