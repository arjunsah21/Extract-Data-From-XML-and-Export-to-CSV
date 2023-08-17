import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse('sample.xml')

### Exporting to CSV
# Extracting Data from XML File
item_data = []
for section in tree.findall('section'):
    for item in section.findall('item'):
        item_id = item.get('id')
        name = item.find('name').text
        brand = item.find('brand').text
        price = item.find('price').text
        currency = item.find('price').get('currency')
        item_data.append([item_id, name, brand, price, currency])

# Creating Pandas Data Farme for item_data
columns = ["ID", "Name", "Brand", "Price", "Currency"]
df = pd.DataFrame(item_data, columns=columns)

# Exporting to CSV
csv_filename = "item_details.csv"
df.to_csv(csv_filename, index=False, encoding="utf-8")
print(f"CSV file {csv_filename} created successfully")