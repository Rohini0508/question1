import json
def extract_sales_data(p):
    with open(p, 'r', encoding='utf-8') as f:
        return json.load(f)
