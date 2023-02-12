import requests
from pprint import pprint

_print = print
print = pprint

def buscar_dados():
    url = "https://liturgia.up.railway.app/7-02"
    headers = {'Authorization': 'Bearer test_87432fa0ab80035651782b93180ed9', 'Content-Type': 'application/json'}
    response = requests.get(url=url, headers=headers)
    response_data = response.json()

    if response.status_code == 200:
        print(response.status_code)
        print(response.reason)
        print(response_data)
    else:
        print(response.status_code)
        print(response.reason)

    salmo = response_data['salmo']
    liturgia = response_data['liturgia']
    with open('liturgia.txt', 'w') as file:
        file.write(f'LITURGIA:\n\n{liturgia}\n\nSALMO:\n\n{salmo}')
buscar_dados()