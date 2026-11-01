import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    print("WEB SCRAPER PROJECT")
    print("-" * 40)

    for book in books:
        title = book.h3.a["title"]
        price = book.find(
            "p", class_="price_color"
        ).text

        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()

        print("Book Name:", title)
        print("Price:", price)
        print("Availability:", availability)
        print("-" * 40)

except requests.exceptions.RequestException as e:
    print("Error:", e)
