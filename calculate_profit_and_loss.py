# Function to calculate the Profit or Loss (P&L) for each pair of transactions
import pandas as pd


def calculate_profit_loss(transaction_pairs):
    """
    Corrected function to calculate profit or loss for each pair of transactions,
    considering both long and short trades, according to the formula:
    P&L = -1 * ((Entry Price * Quantity) + (Exit Price * Quantity))
    """
    profit_loss_data = []

    for open_transaction, close_transaction in transaction_pairs:
        entry_amount = open_transaction['Total Amount']
        exit_amount = close_transaction['Total Amount']

        # Calculate the P&L based on the provided formula
        profit_or_loss = -1 * (entry_amount + exit_amount)
        fees = open_transaction['Order Fees'] + close_transaction['Order Fees']

        # Separate columns for Profit and Loss
        if profit_or_loss > 0:
            profit = profit_or_loss
            loss = 0
        else:
            profit = 0
            loss = -profit_or_loss

        profit_loss_data.append({
            'Ticker Symbol': open_transaction['Ticker Symbol'],
            'Open Date': open_transaction['Trade Date'],
            'Open Time': open_transaction['Trade Time'],
            'Close Date': close_transaction['Trade Date'],
            'Close Time': close_transaction['Trade Time'],
            'Profit': profit,
            'Loss': loss,
            'Order Fees': fees
        })

    return pd.DataFrame(profit_loss_data)
