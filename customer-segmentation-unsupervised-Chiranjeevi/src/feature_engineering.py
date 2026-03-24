import pandas as pd
import numpy as np

def create_rfm(df):
    reference_date = df['InvoiceDate'].max()

    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (reference_date - x.max()).days,
        'InvoiceNo': 'count',
        'TotalPrice': 'sum',
        'Quantity': 'sum'
    })

    rfm.columns = ['Recency', 'Frequency', 'Monetary', 'Total_Quantity']

    rfm['Avg_Order_Value'] = rfm['Monetary'] / rfm['Frequency']

    first = df.groupby('CustomerID')['InvoiceDate'].min()
    last = df.groupby('CustomerID')['InvoiceDate'].max()

    rfm['Purchase_Frequency'] = (last - first).dt.days / rfm['Frequency']

    rfm['Customer_Value'] = rfm['Monetary'] * rfm['Frequency']

    rfm = rfm.fillna(0)

    return rfm