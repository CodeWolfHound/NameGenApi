import requests
#Request Api from http
response = requests.get('https://randomuser.me/api')

#Displays API is connected
#print(response.status_code)
#print(response.json())

#Prints items in json
gender = response.json()['results'][0]['gender']
first_name = response.json()['results'][0]['name']['first']
last_name = response.json()['results'][0]['name']['last']
age = response.json()['results'][0]['dob']['age']

print(f'Full name: {first_name} {last_name}')
print(f'Bio: {gender} {age}')