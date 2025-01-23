import requests
from bs4 import BeautifulSoup

def scrape_medical_data(url):
    """
    Scrapes data from the provided URL and organizes it into a knowledge base.
    Args:
        url (str): The URL to scrape data from.
    Returns:
        list of dict: A structured list containing medical data.
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from {url}. Status Code: {response.status_code}")

    soup = BeautifulSoup(response.content, 'html.parser')
    data = []

    # Example: Scraping articles or FAQs from the medical center page
    faqs = soup.find_all('div', class_='faq-item')  # Update the selector as per the website structure
    for faq in faqs:
        question = faq.find('h3').text.strip()
        answer = faq.find('p').text.strip()
        data.append({"question": question, "answer": answer})
    
    return data
