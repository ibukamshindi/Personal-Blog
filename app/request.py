import requests

def get_quotes():
    '''
    fetches and returns quotes from api
    '''

    url = 'http://quotes.stormconsultancy.co.uk/random.json'
    response = requests.get(url)
    quote = response.json()

    return quote


