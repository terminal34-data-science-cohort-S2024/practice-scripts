"""
Exercise #2c: Basic Data Retrieval with Search Engines and Web Scraping
Scenario

Your task is to scrape data from a webpage listing books, extract information about each book, and perform a simple analysis. We'll use the "Books to Scrape" website for this exercise, a demo site for practicing web scraping.

Website for Scraping

Website URL: [http://books.toscrape.com/](http://books.toscrape.com/)

The website lists books with their titles, prices, and ratings.

Tasks
Web Scraping:
Use Python to scrape the first page of the website.
Extract the title, price, and rating for each book.
Data Analysis:
Convert the scraped data into a Pandas DataFrame.
Calculate and print the average price of the books.

Implementation

You will need to implement a Python solution for this exercise. Ensure you have the `requests` and `pandas` libraries installed, and optionally `matplotlib` for plotting.

Here's a Python solution for the exercise. Make sure you have the `requests`, `bs4` (Beautiful Soup), and `pandas` libraries installed.
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Web Scraping
url = 'http://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract book data
books = soup.find_all('article', class_='product_pod')
book_data = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text[1:] # Remove pound symbol
    rating = book.p['class'][1] # e.g., 'Three'
    book_data.append({'title': title, 'price': float(price), 'rating': rating})

# Data Analysis
df = pd.DataFrame(book_data)
print(df.head()) # Display the first few rows

# Calculate and print average book price
average_price = df['price'].mean()
print(f"Average Price: £{average_price:.2f}")

