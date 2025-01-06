Stock Tracker and Portfolio Manager
This is a Streamlit web application that allows users to track stocks, view detailed stock information, and manage a portfolio. It integrates with the Yahoo Finance API to fetch real-time stock data.

Features
Search Stock Information

Enter a stock ticker (e.g., AAPL, TSLA) to view detailed information such as:
Current Price
Previous Close
Market Cap
52 Week High/Low
Portfolio Management

Add stocks to your portfolio by specifying:
Stock ticker
Quantity
Purchase price per share
View portfolio details, including:
Current market value
Profit/Loss calculations
Remove stocks from your portfolio.
Real-Time Updates

Fetches live stock data to keep your portfolio up to date.
Interactive UI

Simple and intuitive interface using Streamlit.
Requirements
Python Libraries
streamlit
yfinance
pandas
Installation
Clone this repository or copy the code into a .py file:

bash
Copy code
git clone <repository_url>
cd <repository_directory>
Install the required libraries:

bash
Copy code
pip install streamlit yfinance pandas
Run the application:

bash
Copy code
streamlit run <filename>.py
Usage
1. Stock Search
Use the sidebar to enter a stock ticker (e.g., AAPL, TSLA) and view detailed stock information.
2. Add Stock to Portfolio
Specify the stock ticker, quantity, and purchase price to add a stock to your portfolio.
3. View Portfolio
Check your portfolio in the main section of the app.
View details like:
Current price
Market value
Profit/Loss
4. Remove Stock
Enter the ticker of a stock you wish to remove from your portfolio.
Screenshots
(Include relevant screenshots of the app interface here.)

Known Issues
Stocks with unavailable data will show "N/A" for missing fields.
Ensure the stock ticker is valid to avoid errors.


Author
Raghuvardhan Bonjuri
Feel free to reach out for suggestions or improvements! 😊