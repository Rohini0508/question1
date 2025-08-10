from extract import extract_sales_data
from transform import transform_sales_data
from load import load_to_csv
def main():
    d = extract_sales_data('data/sales_transactions_nested.json')
    df = transform_sales_data(d)
    load_to_csv(df, 'data/output.csv')
if __name__ == "__main__":
    main()
