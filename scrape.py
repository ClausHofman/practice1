import requests
from bs4 import BeautifulSoup

def get_wikipedia_article_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the main content of the article
    content = soup.find('div', {'class': 'mw-content-ltr mw-parser-output'})
    if not content:
        print("Error: Could not find the main content of the article.")
        return None

    # Extract headers and paragraphs
    elements = content.find_all(['h1', 'h2', 'h3', 'p'])
    if not elements:
        print("Error: Could not find any headers or paragraphs in the article.")
        return None

    # Combine the text from all headers and paragraphs
    article_text = '\n'.join([element.get_text() for element in elements])

    return article_text

def filter_text(text):
    # Split the text into lines
    lines = text.split('\n')
    # Filter out single character lines, empty lines, and lines containing "displaystyle"
    filtered_lines = [line for line in lines if len(line.strip()) > 1 and 'displaystyle' not in line]
    # Remove unwanted sections
    unwanted_sections = ["See also", "Explanatory notes", "References", "Further reading", "External links"]
    filtered_lines = [line for line in filtered_lines if not any(section in line for section in unwanted_sections)]
    # Combine the filtered lines back into a single string
    filtered_text = '\n'.join(filtered_lines)
    return filtered_text

# URL of the Wikipedia article
url = 'https://en.wikipedia.org/wiki/Quantum_mechanics'

# Get the article text
article_text = get_wikipedia_article_text(url)

if article_text:
    # Filter the article text
    filtered_article_text = filter_text(article_text)
    # Save the filtered article text to a file
    with open('quantum_mechanics_article.txt', 'w', encoding='utf-8') as file:
        file.write(filtered_article_text)
    print("Filtered article text has been saved to 'quantum_mechanics_article.txt'")
else:
    print("Failed to retrieve the article text.")
    
# In console:
# python scrape_website.py