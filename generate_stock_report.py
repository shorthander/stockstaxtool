from tlgParser import parse_transactions
from create_dataframe_from_tlg_data import create_dataframe
from identify_transaction_pairs import identify_transaction_pairs
from calculate_profit_and_loss import calculate_profit_loss
from prepare_and_print_pdf import prepare_and_print_pdf

stock_transactions_columns = [
    'Record Type', 'Transaction ID', 'Ticker Symbol', 'Name', 'Exchange',
    'Action', 'Trade Type', 'Trade Date', 'Trade Time', 'Currency',
    'Number of Shares/Contracts', 'Contract Size', 'Price', 'Total Amount',
    'Order Fees', 'Exchange Rate'
]


def generate_stock_report(lines):
    pdf_path = 'stocks.pdf'
    # Parse data
    stock_transactions_list = parse_transactions(lines, 'STOCK_TRANSACTIONS', 'OPTION_TRANSACTIONS')

    # Create DataFrames
    stock_transactions_df = create_dataframe(stock_transactions_list, stock_transactions_columns)

    long_stock_pairs, short_stock_pairs = identify_transaction_pairs(stock_transactions_df)
    stock_pairs = long_stock_pairs + short_stock_pairs
    stock_pnl = calculate_profit_loss(stock_pairs)
    print("Stocks done.")
    prepare_and_print_pdf(stock_pnl, pdf_path)
