import requests


user_check = input("What user do you want to get?")

url = 'https://github.com/settings/admin'
myobj = {'form-data', user_check}



attempt_to_claim = requests.post(url, data=myobj)

print (attempt_to_claim.text)