import requests
from bs4 import BeautifulSoup


"""
    1. Obtain & parse HTML
        1.a If the HTML file doent exist locally, download it
        1.b If the HTML file exists locally, parse it
    2. Obtain the correct infomration
        - Movie Name
        - Category 
        - Cast
    3. Create a DataFrame
"""

URL = 'https://www.imdb.com/calendar/?region=AR'

def get_imbdb_content():
    '''
    Get access to IMDB trought a request
    
    Returns:
        The content of the request (HTML)
    '''
    headers={
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(URL,headers=headers)
    #soup = BeautifulSoup(response.text, 'html.parser')
    print(response.status_code)
    print(response.text)
    if response.status_code == 200:
        return response.text
    else:
        return None


def main():
    pass

if __name__ == "__main__":
    main()