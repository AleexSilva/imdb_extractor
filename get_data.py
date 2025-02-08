import requests
from bs4 import BeautifulSoup
import csv
import json

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


def get_movie_data(tag):
    
    main_div = tag.find('div', {'class':'ipc-metadata-list-summary-item__c'})
        
    name = main_div.div.a.text
    
    ul_category = main_div.div.find('ul',{
            'class': 'ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--no-wrap ipc-inline-list--inline ipc-metadata-list-summary-item__tl base'})
    
    ul_cast = main_div.div.find('ul', {
            'class': 'ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--no-wrap ipc-inline-list--inline ipc-metadata-list-summary-item__stl base'
        })

    categories = [category.span.text for category in ul_category.find_all('li') ]
    

    cast = [cast.span.text for cast in ul_cast.find_all('li') ] if ul_cast else []
    
    return (name,categories,cast)
 
def create_csv_movies(movies):
    with open('data/movies.csv', 'w',encoding = 'Latin-1') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow(['Name', 'Categories', 'Cast'])
        for movie in movies:
            writer.writerow([
                movie[0],
                ", ".join(movie[1]),
                ", ".join(movie[2])
            ])

def create_json_movies(movies):
   
   movies_list = [
       {
            'Name': movie[0],
            'Categories': movie[1],
            'Cast': movie[2]
        }
       for movie in movies
   ]
   
   with open('data/movies.json', 'w',encoding ='UTF-8') as file:
        json.dump(movies_list,file, indent=4,ensure_ascii=False)

def main():
    """
    Main function to extract movie data from IMDB and save it to a CSV file.

    This function performs the following steps:
    1. Retrieves the HTML content of the IMDB page, either from a local file or by downloading it.

    3. Extracts movie data such as name, categories, and cast from each movie entry.
    4. Writes the extracted movie data into a CSV file named 'movies.csv' with columns for Name, Categories, and Cast.
    """

    content= get_local_imdb_content()
    soup = BeautifulSoup(content, 'html.parser')
    li_tags = soup.find_all('li', {
        'data-testid':'coming-soon-entry',
        'class': 'ipc-metadata-list-summary-item ipc-metadata-list-summary-item--click sc-48869e4f-0 dJwARK'
    })
    
    movies = [get_movie_data(tag) for tag in li_tags]
    create_csv_movies(movies)
    create_json_movies(movies)
    
    print('Movies saved to movies.csv and movies.json')

if __name__ == "__main__":
    main()