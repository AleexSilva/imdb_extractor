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
    """
    Fetch the HTML content of the IMDB page via an HTTP GET request.

    Returns:
        str or None: The HTML content of the page if the request is successful; 
        otherwise, None.
    """
    # Define the request headers with a User-Agent to mimic a browser
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    
    # Send a GET request to the specified URL
    response = requests.get(URL, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Return the HTML content of the response
        return response.text
    else:
        # Return None if the request failed
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
    """
    Reads the HTML file and returns its content.

    Returns:
        str: The content of the HTML file, or None if an error occurs.
    """
    content = None
    
    try:
        # Attempt to open the file in read mode
        with open('imdb.html', 'r') as f:
            # Read the file content
            content = f.read()
    except Exception as e:
        # Catch any exceptions and set content to None
        content = None
    
    # Return the file content or None if an error occurred
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
    """
    Extracts movie data such as name, categories, and cast from an HTML tag.

    Args:
        tag (Tag): A BeautifulSoup Tag object containing movie information.

    Returns:
        tuple: A tuple containing the movie name, a list of categories, and a list of cast members.
    """
    # Find the main div that contains the movie information
    main_div = tag.find('div', {'class': 'ipc-metadata-list-summary-item__c'})
    
    # Extract the movie name
    name = main_div.div.a.text
    
    # Find the unordered list that contains the categories
    ul_category = main_div.div.find('ul', {
        'class': 'ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--no-wrap ipc-inline-list--inline ipc-metadata-list-summary-item__tl base'
    })
    
    # Find the unordered list that contains the cast
    ul_cast = main_div.div.find('ul', {
        'class': 'ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--no-wrap ipc-inline-list--inline ipc-metadata-list-summary-item__stl base'
    })

    # Extract the categories as a list of strings
    categories = [category.span.text for category in ul_category.find_all('li')]
    
    # Extract the cast as a list of strings, if available
    cast = [cast.span.text for cast in ul_cast.find_all('li')] if ul_cast else []
    
    return (name, categories, cast)

def create_csv_movies(movies):
    """
    Converts a list of movie tuples into a CSV file.

    Args:
        movies (list): A list of tuples, each containing the movie name,
                       categories, and cast.

    The CSV file 'movies.csv' is created in the 'data' directory with the
    following structure:
    Name;Categories;Cast
    Movie Name;Category1, Category2;Actor1, Actor2
    ...
    """
    # Open the CSV file for writing
    with open('data/movies.csv', 'w', encoding='Latin-1') as file:
        # Create a CSV writer with a semicolon delimiter
        writer = csv.writer(file, delimiter=';')
        
        # Write the header row
        writer.writerow(['Name', 'Categories', 'Cast'])
        
        # Write each movie as a row
        for movie in movies:
            writer.writerow([
                movie[0],  # Movie name
                ', '.join(movie[1]),  # Categories, comma-separated
                ', '.join(movie[2])  # Cast, comma-separated
            ])

def create_json_movies(movies):

    # Create a list of dictionaries from the list of movie tuples
    movies_list = [
        {
            'Name': movie[0],
            'Categories': movie[1],
            'Cast': movie[2]
        }
        for movie in movies
    ]
    
    # Write the list of dictionaries to a JSON file
    with open('data/movies.json', 'w', encoding='UTF-8') as file:
        json.dump(movies_list, file, indent=4, ensure_ascii=False)

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