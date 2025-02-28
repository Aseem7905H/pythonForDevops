#developer has an api(application Programe interface)

import requests

demo_url= "https://api.publicapis.org/entries"
response = requests.get(url=demo_url)
print(response) 
print(dir(response))
print(response.json())
