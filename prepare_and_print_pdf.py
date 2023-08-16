import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def prepare_and_print_pdf(data, pdf_path):
    # Format the date columns to DD.MM.YYYY
    data['Open Date'] = pd.to_datetime(data['Open Date']).dt.strftime('%d.%m.%Y')
    data['Close Date'] = pd.to_datetime(data['Close Date']).dt.strftime('%d.%m.%Y')

    # Limit the decimal places of the money amounts to two
    data['Profit'] = data['Profit'].round(2)
    data['Loss'] = data['Loss'].round(2)
    data['Order Fees'] = data['Order Fees'].round(2)

    # Add a row at the end with the sum of 'Profit', 'Loss', and 'Order Fees' columns
    sum_row = pd.DataFrame({
        'Ticker Symbol': ['Sum'],
        'Open Date': '',
        'Open Time': '',
        'Close Date': '',
        'Close Time': '',
        'Profit': [data['Profit'].sum()],
        'Loss': [data['Loss'].sum()],
        'Order Fees': [data['Order Fees'].sum()]
    })
    profit_loss_df_corrected_sum = pd.concat([data, sum_row], ignore_index=True)

    # Rename the 'Sum' row to 'Summe'
    sum_row['Ticker Symbol'] = 'Summe'

    # Replace 'NaN' entries with an empty string
    profit_loss_df_corrected_sum = profit_loss_df_corrected_sum.fillna('')

    # Make the 'Order Fees' column values positive
    profit_loss_df_corrected_sum['Order Fees'] = profit_loss_df_corrected_sum['Order Fees'].abs()

    # Create a PDF document with the updated formatting and summary row
    with PdfPages(pdf_path) as pdf:
        # Plot the DataFrame as a table and remove axis
        fig, ax = plt.subplots(figsize=(14, len(profit_loss_df_corrected_sum) * 0.5))
        ax.axis('off')

        # Add a table with the data from the DataFrame
        plt.table(cellText=profit_loss_df_corrected_sum.values,
                  colLabels=profit_loss_df_corrected_sum.columns,
                  cellLoc='center', loc='center')

        # Add a title to the table
        plt.title('Stock Transactions Profit & Loss Report', fontsize=16)

        # Save the table as a page in the PDF
        pdf.savefig(fig, bbox_inches='tight')

    # # Return the file path for user to download the updated PDF
    # pdf_path
