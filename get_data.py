import requests
from bs4 import BeautifulSoup


"""
    1. Obtain & parse HTML
    2. Obtain the correct infomration
    3. Create a DataFrame
"""

URL = 'https://www.imdb.com/calendar/?region=AR'

def get_imbdb_content():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def main():
    pass

if __name__ == "__main__":
    main()