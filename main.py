from readFile import read_file
from generate_stock_report import generate_stock_report
from generate_stillhalter_report import generate_stillhalter_report
# Column names for each DataFrame

stock_positions_columns = [
    'Record Type', 'Account ID', 'Ticker Symbol', 'Name', 'Currency',
    'Unknown', 'Time', 'Amount', 'Contract Size', 'Entry Price',
    'Total Amount', 'Exchange Rate'
]

# read tlg file
file_path = 'U9066428_20220215_20221230.tlg'
pdf_path = 'tmp.pdf'
lines = read_file(file_path)

generate_stock_report(lines)
generate_stillhalter_report(lines)


# option_transactions_list = parse_transactions(lines, 'OPTION_TRANSACTIONS', 'CURRENCY_TRANSACTIONS')
# stock_positions_list = parse_transactions(lines, 'STOCK_POSITIONS', '')
# stock_positions_df = create_dataframe(stock_positions_list, stock_positions_columns)
# option_transactions_df = create_dataframe(option_transactions_list, option_transactions_columns)


