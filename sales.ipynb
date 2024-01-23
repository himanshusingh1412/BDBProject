import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def generate_sales_data(num_records=1000):
    np.random.seed(0)  # For reproducibility
    dates = [datetime.now() - timedelta(days=i) for i in range(num_records)]
    product_ids = np.random.randint(1000, 2000, num_records)
    quantities = np.random.randint(1, 10, num_records)
    unit_price = np.random.uniform(10, 500, num_records)
    customer_ids = np.random.randint(10000, 20000, num_records)


    data = {
        'Date': dates,
        'ProductID': product_ids,
        'Quantity': quantities,
        'UnitPrice': unit_price,
        'CustomerID': customer_ids
        # ... add other columns here
    }

    df = pd.DataFrame(data)
    return df


def clean_data(df):

    df = df[df['UnitPrice'] > 0]

    return df


def transform_data(df):
    df['TotalSales'] = df['Quantity'] * df['UnitPrice']

    return df


def calculate_kpis(df):
    total_sales = df['TotalSales'].sum()
    average_sales_per_item = df['TotalSales'].mean()
    
    sales_growth = df['TotalSales'].pct_change().mean() * 100

    kpis = {
        'Total Sales': total_sales,
        'Average Sales per Item': average_sales_per_item,
        'Sales Growth': sales_growth
    }
    return kpis

def main():
    sales_data = generate_sales_data()
    cleaned_data = clean_data(sales_data)
    transformed_data = transform_data(cleaned_data)
    kpis = calculate_kpis(transformed_data)

    print("KPIs:", kpis)
    return transformed_data, kpis

if __name__ == "__main__":
    sales_df, sales_kpis = main()
