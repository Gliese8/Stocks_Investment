# Stocks_Investment
We are the lead data scientist of SmartInvestment.com. Our company sells investment funds tailored to maximise results and minimise risk. 
An investment fund is just a basket of investment products. Our star fund is called FAANG+_forever.

The fund composition is the following:

- 15% Facebook (Meta). Symbol META
- 10% Netflix. Symbol NFLX
- 25% Apple. Symbol APPL
- 15% Tesla. Symbol TSLA
- 20% Google (Alphabet). Symbol GOOGL
- 15% Amazon. Symbol AAMZ

Tasks:

1. For regulatory reasons we need to provide to our investors a quarter by quarter report with the proformance of the fund (% increased or lost, in that case the % will be negarive) comparing it with the performance of the SPX500.

We also want to provide visual and more short term information to our customers so we want to provide the following 2 charts:

Line chart with weekly gain/loss % of the fund and SPX (both in the same chart)
Line chart with weekly acummulated gain/loss % of the fund and SPX (both in the same chart) 

2. Automate the calculation of the amounts to refund to customers that want to cancel their investment. To do so we need a script that does the following:

Uploads all files of the stocks that compose the fund and calculates the daily accumulated gain/loss in percentage. 
Uploads a file called users.csv with the following columns: user_id, investment_open_date, investment_close_date, amount_invested
The script should output a file called users_refund.csv with the same columns as the previous one plus another one called amount_refund. 

The program will receive a path as a parameter that will be the folder where all files should be read from and where the output file should be written to.

python refunds_calcs.py path_to_folder
