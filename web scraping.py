from typing import List
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
import xlsxwriter
import sys


@dataclass
class Product:
    title: str
    image: str
    price: str
    link: str


def create_excel_file(data: List[Product]) -> None:
    name_columns = [
        ('Title', 'A1'),
        ('Image', 'B1'),
        ('Price', 'C1'),
        ('Link', 'D1')
    ]
    workbook = xlsxwriter.Workbook('Dati.xlsx')
    worksheet = workbook.add_worksheet()

    bold = workbook.add_format({'bold': True})
    counter = 0
    for field_data in name_columns:
        name, field = field_data
        worksheet.set_column(counter, counter, 40)
        worksheet.write(field, name, bold)
        counter += 1
    row = 1
    for product in data:
        col_number = 0
        product_dict = product.__dict__
        for key in product_dict:
            worksheet.write(row, col_number, product_dict[key])
            col_number += 1
        row += 1

    workbook.close()


def remove_extra_spaces(text: str) -> str:
    return ''.join(text.split())


def format_price(price: str) -> str:
    euro_index = price.find('€')
    if euro_index != -1:
        price = price[:euro_index + 1]
    return price


def three_symbols_price(b: str) -> str:
    if len(b) >= 6:
        b = b[:-3] + ',' + b[-3:]
    return b


def parse_by_url(url: str) -> List[Product]:
    result = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('section', class_='product-card__list product-card__list--vertical')
    cards = table.findAll('article', class_='product-card vertical')

    for card in cards:
        a = card.find('a', class_='product_name')
        product_name = a.find('h5', class_='product-card__heading').text
        link = a['href']

        product_poster = card.find('div', class_='product-card__image-div')
        image = product_poster.find('img')['src'] if product_poster else None

        product_price_hidden = card.find('div', class_='product-card__price')
        product_price = product_price_hidden.find('div', class_='price').text if product_price_hidden else None
        product_price = remove_extra_spaces(product_price)
        product_price = three_symbols_price(product_price)
        product_price = format_price(product_price)

        result.append(
            Product(
                title=product_name.strip().replace(',', '').replace(' - Viedtālrunis', ''),
                image=image,
                price=product_price,
                link=link
            )
        )
    return result


def search_and_display_model(base_url: str, desired_model: str) -> None:
    data = parse_by_url(base_url)
    filtered_data = [product for product in data if desired_model.lower() in product.title.lower()]

    if not filtered_data:
        print(f"No data found for the iPhone model: {desired_model}")
        return

    for product in filtered_data:
        print(f"Title: {product.title}")
        print(f"Image: {product.image}")
        print(f"Price: {product.price}")
        print(f"Link: {product.link}")
        print("\n")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <iphone_model>")
        sys.exit(1)

    base_url = 'https://www.euronics.lv/telefoni/viedtalruni/iphone'
    desired_model = sys.argv[1]
    search_and_display_model(base_url, desired_model)