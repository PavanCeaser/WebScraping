import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the URL
url = "https://pavanceaser.github.io/Portfolio/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract specific data, e.g., all links
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))
else:
    print(f"Failed to retrieve content: {response.status_code}")
