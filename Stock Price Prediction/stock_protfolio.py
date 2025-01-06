import streamlit as st
import yfinance as yf
import pandas as pd

# Initialize portfolio
if "portfolio" not in st.session_state:
    st.session_state["portfolio"] = []

# Function to fetch stock data
def fetch_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        data = {
            "Name": info.get("longName", "N/A"),
            "Current Price": info.get("currentPrice", "N/A"),
            "Previous Close": info.get("previousClose", "N/A"),
            "Market Cap": info.get("marketCap", "N/A"),
            "52 Week High": info.get("fiftyTwoWeekHigh", "N/A"),
            "52 Week Low": info.get("fiftyTwoWeekLow", "N/A"),
        }
        return data
    except Exception as e:
        st.error(f"Error fetching data for {ticker}: {e}")
        return None

# App Title
st.title("📊 Stock Tracker and Portfolio Manager")

# Sidebar: Stock Search
st.sidebar.header("🔍 Search Stock")
search_ticker = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, TSLA)")
if st.sidebar.button("Search"):
    if search_ticker:
        stock_data = fetch_stock_data(search_ticker.upper())
        if stock_data:
            st.sidebar.write("### Stock Information")
            for key, value in stock_data.items():
                st.sidebar.write(f"**{key}:** {value}")
    else:
        st.sidebar.error("Please enter a valid stock ticker.")

# Sidebar: Add Stock to Portfolio
st.sidebar.header("➕ Add Stock to Portfolio")
add_ticker = st.sidebar.text_input("Ticker (e.g., MSFT)")
add_quantity = st.sidebar.number_input("Quantity", min_value=1, step=1)
add_price = st.sidebar.number_input("Purchase Price per Share", min_value=0.0, step=0.01)

if st.sidebar.button("Add to Portfolio"):
    if add_ticker:
        st.session_state["portfolio"].append({
            "Ticker": add_ticker.upper(),
            "Quantity": add_quantity,
            "Purchase Price": add_price
        })
        st.sidebar.success(f"Added {add_ticker.upper()} to portfolio!")
    else:
        st.sidebar.error("Please enter a valid stock ticker.")

# Main Section: Portfolio Management
st.header("📜 Your Portfolio")

# Display Portfolio
portfolio_df = pd.DataFrame(st.session_state["portfolio"])
if not portfolio_df.empty:
    portfolio_data = []
    for stock in st.session_state["portfolio"]:
        stock_data = fetch_stock_data(stock["Ticker"])
        if stock_data:
            current_price = stock_data["Current Price"]
            purchase_price = stock["Purchase Price"]
            quantity = stock["Quantity"]
            market_value = quantity * current_price if current_price != "N/A" else "N/A"
            portfolio_data.append({
                "Ticker": stock["Ticker"],
                "Quantity": quantity,
                "Purchase Price (per share)": purchase_price,
                "Current Price": current_price,
                "Market Value": market_value,
                "Profit/Loss": (current_price - purchase_price) * quantity if current_price != "N/A" else "N/A"
            })

    portfolio_df = pd.DataFrame(portfolio_data)
    st.dataframe(portfolio_df)

    # Remove Stock from Portfolio
    st.subheader("🗑️ Remove Stock from Portfolio")
    remove_ticker = st.text_input("Enter Ticker to Remove")
    if st.button("Remove Stock"):
        st.session_state["portfolio"] = [stock for stock in st.session_state["portfolio"] if stock["Ticker"] != remove_ticker.upper()]
        st.success(f"Removed {remove_ticker.upper()} from portfolio!")
else:
    st.write("Your portfolio is empty. Add stocks to start tracking!")

# Footer
st.markdown("mr.chinnu_raghu")
