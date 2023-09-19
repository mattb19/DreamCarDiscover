from bs4 import BeautifulSoup
import requests

url = "https://www.target.com/s?searchTerm=ground+beef&tref=typeahead%7Cterm%7Cground+beef%7C%7C%7Chistory&ignoreBrandExactness=true&sortBy=PriceLow&moveTo=product-list-grid"
html = requests.get(url)
print(html.text)
