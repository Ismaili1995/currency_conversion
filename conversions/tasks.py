import requests
from starlette.exceptions import HTTPException
from starlette.applications import Starlette
from starlette.routing import Route


url = 'https://api.exchangerate-api.com/v4/latest/USD'
base_currency = 'USD'
data= requests.get(url).json()
currencies = data['rates']

        
def convert_currency(request):
    data = request.json()
    print(data)
    from_currency = data['from_currency']
    to_currency = request.query_params['to_currency']
    amount =  request.query_params['amount']
    """[Convert Money from Currency to another]

    Args:
        from_currency ([str]): [currency that you want to convert]
        to_currency ([str]): [The result currency you want to get]
        amount ([float]): [Amount of currency that you want to convert]

    Returns:
        [float]: [amount of The result currency you wanted to get ]
    """
    try:
        # checking from_currency if is the same with base currency (USD)
        if from_currency != base_currency: 
            amount = amount / currencies[from_currency] 

        # limiting the precision to 2 decimal places 
        amount = round(amount * currencies[to_currency], 2) 
        return amount
    except:
        return HTTPException(
            status_code=4040, detail="One or both of Currency codes are not found on this free plan of API"
        )

