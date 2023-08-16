# Function to create a DataFrame from a list of transactions with specified column names
import pandas as pd

def create_dataframe(transactions_list, column_names):
    """
    Convert a list of transaction data into a DataFrame.
    Each string in transactions_list is split into a list of values based on the delimiter '|',
    and then loaded into a DataFrame with the specified column names.
    """
    # Split each string in transactions_list into a list of values based on the delimiter '|'
    transactions_data = [line.split('|') for line in transactions_list]

    # Create a DataFrame from the list of values
    df = pd.DataFrame(transactions_data, columns=column_names)

    # Specify the columns that need to be converted to numeric
    numeric_columns = [
        'Transaction ID', 'Number of Shares/Contracts',
        'Contract Size', 'Price', 'Total Amount', 'Order Fees', 'Exchange Rate'
    ]

    # Convert the specified columns to appropriate numeric data types
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    return df