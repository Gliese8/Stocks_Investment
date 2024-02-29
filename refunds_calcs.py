import pandas as pd
import os
import glob
import sys

def main(path_to_folder):
    files = glob.glob(os.path.join(path_to_folder, "*.csv"))

    secs = {os.path.basename(file).split('_')[0] for file in files}

    secs = {}
    for file_path in files:
        filename = os.path.basename(file_path)
        parts = filename.split('_')
        if len(parts) >= 2:
            sec = parts[0]  # Stock symbol
            id_f = parts[1].split('.')[0]  # File ID

            if sec not in secs:
                secs[sec] = {'files': [], 'num_files': 0, 'dfs': {}}

            secs[sec]['files'].append(file_path)
            secs[sec]['num_files'] += 1
            secs[sec]['dfs'][id_f] = pd.read_csv(file_path)

    for key, value in secs.items():
        value['final_df'] = pd.concat([value['dfs']['2'], value['dfs']['1']])
        value['final_df']['Date'] = pd.to_datetime(pd.to_datetime(value['final_df']['Date'], utc=True).dt.date)
        value['final_df'] = value['final_df'].set_index('Date')
        value['final_df']['prev_close'] = value['final_df']['Close'].shift(1)
        value['final_df'] = value['final_df'][['Close', 'prev_close']]

    fund_df = secs['META']['final_df'] * 0.15 + secs['NFLX']['final_df'] * 0.1 + secs['AAPL']['final_df'] * 0.25 + secs['TSLA']['final_df'] * 0.15 + secs['GOOGL']['final_df'] * 0.2 + secs['AMZN']['final_df'] * 0.15

    fund_df['Daily Gain/Loss %'] = (fund_df['Close'] - fund_df['prev_close']) / fund_df['prev_close'] * 100
    fund_df['Accumulated Gain/Loss %'] = fund_df['Daily Gain/Loss %'].cumsum()
 
    print(fund_df) 

    users_file_path = os.path.join(path_to_folder, 'users.csv')
    users_df = pd.read_csv(users_file_path)

    users_df['amount_refund'] = 0.0
    
    for index, row in users_df.iterrows():
        investment_open_date = row['investment_open_date']
        investment_close_date = row['investment_close_date']    
     
        if investment_open_date in fund_df.index and investment_close_date in fund_df.index:
            
            close_price_on_opening_date = fund_df.at[investment_open_date, 'Close']
            close_price_on_refund_date = fund_df.at[investment_close_date, 'Close']
           
            refund_amount = (row['amount_invested'] / close_price_on_opening_date) * close_price_on_refund_date
            users_df.at[index, 'amount_refund'] = refund_amount
        else:
            # Handle missing dates
            users_df.at[index, 'amount_refund'] = 'Date not found'

    users_refund_file_path = os.path.join(path_to_folder, 'users_refund.csv')
    users_df.to_csv(users_refund_file_path, index=False)
    print("Refund calculation completed and saved to:", users_refund_file_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python refunds_calcs.py <path_to_folder>")
    else:
        path_to_folder = sys.argv[1]
        main(path_to_folder)












