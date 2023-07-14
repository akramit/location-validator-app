import subprocess
import os,django
import requests
from bs4 import BeautifulSoup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "location_validator.settings")
django.setup()
from location.models import location

# Put google map api key
api_key=''

# Scrap the web
def get_all_store_address() :
    headers = requests.utils.default_headers()
    headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })
    url = 'https://www.shoppersstop.com/store-finder'
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the dropdown menu for states
    city_dropdown = soup.find('div', {'class': 'select-option'}) # Gets all city
    
    # Create a list to store the data
    data_list = []

    # Iterate over each state option in the dropdown menu
    for city_option in city_dropdown.find_all('option'):
        # Extract the state name and value
        city_name = city_option.text.strip()
        city_value = city_option['value']
    
        #print(city_value)
        city_url = f'https://www.shoppersstop.com/store-finder?q={city_value}&page=0'

        city_response = requests.get(city_url,headers=headers)
        city_store_data = city_response.json()
        results = city_store_data['results']
        #if(city_value == 'Bengaluru'):
        #    break
        for data in results:
            store =[]
            store_name = data['name']
            address = data['address']
            formatted_address = address['formattedAddress']
        
            store.append(city_value)
            store.append(store_name)
            store.append(formatted_address)
            data_list.append(store)
    return data_list

# Validates the addresses
def is_valid_address(address):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'
    response = requests.get(url)
    data=response.json()
    if data['status'] == 'OK':
        return True
    return False

# Save the data
def persist_addresses_in_db(addresses):
    for add in addresses:
        c = add[0]
        n = add[1]
        a = add[2]
        v=is_valid_address(a)
        q=location(city=c,name=n,address=a,valid=v)
        q.save()

    


if __name__ == '__main__':
    # Runs on local host - port 8000
    print("App Started..\n")
    count=location.objects.all()
    if len(count) <=1:
        list_of_addresses = get_all_store_address()
        print("All addresses fetched. \n Listing one")
        print(list_of_addresses[0])
        #print(list_of_addresses)
        print("\n Persisting...")
        persist_addresses_in_db(list_of_addresses)
        print('\nPersisted.. Starting Server \n ')
    command = 'python3 manage.py runserver'
    subprocess.run(command,shell=True)
