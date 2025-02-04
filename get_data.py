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

def create_imdb_local_file(content):
    '''
    Create a HTML file locally from a content
    '''
    try:
        with open('imdb.html', 'w') as f:
            f.write(content)
            soup = BeautifulSoup(f, 'html.parser')
    except:
        pass


def get_imdb_file_local_file():
    '''
    Read the HTML file
    '''
    content = None
    
    try:
        with open('imdb.html', 'r') as f:
            content = f.read()
    except:
        pass
    
    return content

def get_local_imdb_content():
    '''
    Get the content of the HTML file
    if it does not exist, download it
    
    Returns:
        The content of the HTML file
    '''
    content = get_imdb_file_local_file()
    if content:
        return content
    
    content = get_imbdb_content()
    create_imdb_local_file(content)
    
    return content

def main():
    pass

if __name__ == "__main__":
    main()