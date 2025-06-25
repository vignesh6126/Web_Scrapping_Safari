import requests
from bs4 import BeautifulSoup
import csv

# URL of GitHub trending page
url = "https://github.com/trending"

# Send a GET request to the GitHub trending page
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all repository elements - they're in <article> tags with class="Box-row"
    repos = soup.find_all('article', class_='Box-row')[:5]  # Get only top 5
    
    # Prepare data for CSV
    data = []
    for repo in repos:
        # Extract repository name (includes owner)
        name_element = repo.find('h2', class_='h3 lh-condensed')
        name = name_element.get_text(strip=True).replace('\n', '').replace(' ', '')
        
        # Extract repository URL (relative URL needs to be converted to absolute)
        relative_url = name_element.find('a')['href']
        url = f"https://github.com{relative_url}"
        
        data.append([name, url])
    
    # Write data to CSV file
    with open('github_trending_top5.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['repository name', 'link'])  # Write header
        writer.writerows(data)  # Write data rows
    
    print("Successfully saved top 5 trending repositories to 'github_trending_top5.csv'")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")