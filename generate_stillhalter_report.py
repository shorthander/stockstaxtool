from tlgParser import parse_transactions
from create_dataframe_from_tlg_data import create_dataframe
from identify_transaction_pairs import identify_transaction_pairs
from calculate_profit_and_loss import calculate_profit_loss
from prepare_and_print_pdf import prepare_and_print_pdf
import pandas as pd


option_transactions_columns = [
    'Record Type', 'Transaction ID', 'Ticker Symbol', 'Name', 'Exchange',
    'Action', 'Trade Type', 'Trade Date', 'Trade Time', 'Currency',
    'Number of Shares/Contracts', 'Contract Size', 'Price', 'Total Amount',
    'Order Fees', 'Exchange Rate'
]


def generate_stillhalter_report(lines):
    stillhalter_pdf_path = 'stillhalter.pdf'
    termin_pdf_path = 'termin.pdf'
    # Parse data
    option_transactions_list = parse_transactions(lines, 'OPTION_TRANSACTIONS', 'CURRENCY_TRANSACTIONS')

    # Create DataFrames
    option_transactions_df = create_dataframe(option_transactions_list, option_transactions_columns)

    long_option_pairs, short_option_pairs = identify_transaction_pairs(option_transactions_df)

    stillhalter_pnl = calculate_profit_loss(short_option_pairs)
    termingeschaeft_pnl = calculate_profit_loss(long_option_pairs)
    prepare_and_print_pdf(stillhalter_pnl, stillhalter_pdf_path)
    prepare_and_print_pdf(termingeschaeft_pnl, termin_pdf_path)
