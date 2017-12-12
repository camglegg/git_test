from lxml import html
import requests

page = requests.get('https://fusioncine.com/rentals/audio')
tree = html.fromstring(page.content)

# This will create a list of product Descriptions
product = tree.xpath('//*[@id="divforcomparing8"]/div/div[2]')
# This will create a list of the prices
price = tree.xpath('//*[@id="divforcomparing8"]/div/div[3]/div/span/span')

print('Product: ', product)
print('Prices: ', price)