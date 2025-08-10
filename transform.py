import pandas as pd
from datetime import datetime
def transform_sales_data(d):
    df = pd.json_normalize(d)
    df = df[df['sale_amount'] > 50]
    df['product.product_name'] = df['product.product_name'].str.strip().str.title()
    df = df[df['product.product_name'].notna() & (df['product.product_name'] != "")]
    df = df[df['customer.customer_id'].notna() & (df['customer.customer_id'] != "")]
    def cd(s):
        try: return datetime.strptime(s, "%Y-%m-%d").strftime("%Y-%m-%d")
        except: return datetime.strptime(s, "%m/%d/%Y").strftime("%Y-%m-%d")
    df['sale_date'] = df['sale_date'].apply(cd)
    df['sale_amount'] = df['sale_amount'].round(2)
    df = df.drop_duplicates(subset=['transaction_id','sale_date'])
    def cat(a): return "Budget" if 50 <= a <= 100 else "Mid-Range" if a <= 300 else "Premium"
    df['sale_category'] = df['sale_amount'].apply(cat)
    df['discount_eligible'] = df['sale_amount'].apply(lambda x: "Yes" if x > 200 else "No")
    return df
