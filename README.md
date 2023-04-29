# price_api

This is a simple API that retrieves the latest price of Lithium-ion batteries from the website https://www.metal.com/Lithium-ion-Battery/202303240001 and returns it as a JSON response.

## API Endpoint

The API has a single endpoint:
    GET /price
## Response Format
    The response is returned in JSON format and has the following fields:
    {
    price: The latest price of Lithium-ion batteries as a float value.
    }
Example response:
    {"price": "0.12"}
    
## Error Handling
    The API returns an error response with a status code of 400 for invalid requests.
    
## How to Run
    To run the API locally, follow these steps:
        1.)Clone the repository: "git clone https://github.com/trickster26/price_api.git"
        2.)Install the required dependencies: "pip install -r requirements.txt"
        3.)Run the Django development server: "python manage.py runserver"
        4.)The API will be available at "http://localhost:8000/price"
        
        
## Deployment
    i.)  It is deployed on railway at with domain name https://priceapi-production-b1e1.up.railway.app/
    ii.) For Price api will be available at https://priceapi-production-b1e1.up.railway.app/price/
    iii.)Simply create a new app, link it to your GitHub repository, and configure the build and deployment settings.
