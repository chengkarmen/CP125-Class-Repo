import pandas as pd


def critical_inventory(filename):
    data = pd.read_csv(filename)
    total_products = len(data)
    critical_count = len(data.loc[(data['StockLevel'] < data['ReorderThreshold']) & (data['DaysSinceRestock'] > 30)])
    critical_products = set(data.loc[(data['StockLevel'] < data['ReorderThreshold']) & (data['DaysSinceRestock'] > 30), 'ProductName'])
    print({"total_products": total_products,
            "critical_count": critical_count,
            "critical_products": critical_products})

critical_inventory('labs/lab09/data/students.csv')


