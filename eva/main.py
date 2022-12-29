import codecs

sku_list = ['740767', '740768', '740769', '740770', '740771']


def get_items_descriptions(file_name: str, sku_list: list):
    text = ''
    products = {}
    file = codecs.open(file_name, 'r', 'utf-8')
    for line in file.readlines():
        for sku in sku_list:
            if sku in line:
                text = ''
            else:
                if line.strip() and '<p>&nbsp;</p>' not in line and 'href' not in line:
                    line = line.replace('strong>', 'b>')
                    text += f'{line.strip()}\n'
            products = {sku: text}

    for k, v in products.items():
        print(f'{k} => {v}')


print(get_items_descriptions('rus-text.html', sku_list))
