from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
from .models import Price



def get_price(request):
    # Make a GET request to the website
    response = requests.get("https://www.metal.com/Lithium-ion-Battery/202303240001")

    # Check if the request was successful
    if response.status_code != 200:
        return JsonResponse({'error': 'Failed to fetch price'}, status=500)

    # Extract the price from the response
    soup = BeautifulSoup(response.content, 'html.parser')
    price = soup.find('span', class_='priceDown___2TbRQ').text.strip()
    
    # To store the data into the Database
    # Price.objects.create(price=price)
    


    return JsonResponse({'price': price})

