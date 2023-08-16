# Function to identify transaction pairs (OPEN and CLOSE) for a given set of transactions
def identify_transaction_pairs(df):
    """
    Updated function to identify pairs of transactions for each unique stock symbol,
    considering both long and short trades.
    """
    unique_stocks = df['Ticker Symbol'].unique()
    short_transaction_pairs = []
    long_transaction_pairs = []

    for stock in unique_stocks:
        stock_data = df[df['Ticker Symbol'] == stock]

        # For long trades: Pair 'BUYTOOPEN' with 'SELLTOCLOSE'
        open_long_transactions = stock_data[stock_data['Action'] == 'BUYTOOPEN']
        close_long_transactions = stock_data[stock_data['Action'] == 'SELLTOCLOSE']

        for _, open_transaction in open_long_transactions.iterrows():
            for _, close_transaction in close_long_transactions.iterrows():
                if open_transaction['Number of Shares/Contracts'] == -close_transaction['Number of Shares/Contracts']:
                    long_transaction_pairs.append((open_transaction, close_transaction))
                    break

        # For short trades: Pair 'SELLTOOPEN' with 'BUYTOCLOSE'
        open_short_transactions = stock_data[stock_data['Action'] == 'SELLTOOPEN']
        close_short_transactions = stock_data[stock_data['Action'] == 'BUYTOCLOSE']

        for _, open_transaction in open_short_transactions.iterrows():
            for _, close_transaction in close_short_transactions.iterrows():
                if open_transaction['Number of Shares/Contracts'] == -close_transaction['Number of Shares/Contracts']:
                    short_transaction_pairs.append((open_transaction, close_transaction))
                    break

    return long_transaction_pairs, short_transaction_pairs
