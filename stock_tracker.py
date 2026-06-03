"""
Stock Portfolio Tracker
Allows users to input stock names and quantities, then calculates total investment
based on hardcoded stock prices.
"""

import csv
from datetime import datetime


# Hardcoded stock prices dictionary
STOCK_PRICES = {
    "AAPL": 10.00,
    "TSLA": 20.00,
    "GOOGL": 60.00,
    "MSFT": 40.00,
    "AMZN": 80.00,
    "META": 30.00,
    "NVDA": 70.00,
    "AMD": 50.00
}


def display_available_stocks():
    print("\n" + "="*50)
    print("AVAILABLE STOCKS")
    print("="*50)
    for symbol, price in sorted(STOCK_PRICES.items()):
        print(f"  {symbol}: ${price:.2f}")
    print("="*50 + "\n")


def get_portfolio_from_user():
    portfolio = {}
    
    print("Enter your stock portfolio (or 'done' when finished)")
    print("-" * 50)
    
    while True:
        stock_symbol = input("Enter stock symbol (or 'done' to finish): ").strip().upper()
        
        if stock_symbol == "DONE":
            break
        
        if stock_symbol not in STOCK_PRICES:
            print(f"❌ '{stock_symbol}' not found. Available stocks: {', '.join(STOCK_PRICES.keys())}")
            continue
        
        try:
            quantity = float(input(f"Enter quantity for {stock_symbol}: ").strip())
            if quantity <= 0:
                print("❌ Quantity must be positive!")
                continue
            portfolio[stock_symbol] = quantity
            print(f"✓ Added {quantity} shares of {stock_symbol}")
        except ValueError:
            print("❌ Invalid quantity! Please enter a number.")
            continue
    
    return portfolio


def calculate_portfolio_value(portfolio):
    if not portfolio:
        return 0, {}
    
    breakdown = {}
    total_value = 0
    
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        investment = quantity * price
        breakdown[symbol] = {
            "quantity": quantity,
            "price": price,
            "total": investment
        }
        total_value += investment
    
    return total_value, breakdown


def display_portfolio_summary(portfolio, total_value, breakdown):
    print("\n" + "="*80)
    print("PORTFOLIO SUMMARY")
    print("="*80)
    
    if not portfolio:
        print("Your portfolio is empty!")
        return
    
    # Header
    print(f"{'Stock':<10} {'Quantity':<12} {'Price/Share':<15} {'Total Value':<15}")
    print("-"*80)
    
    # Portfolio items
    for symbol in sorted(breakdown.keys()):
        data = breakdown[symbol]
        print(f"{symbol:<10} {data['quantity']:<12.2f} ${data['price']:<14.2f} ${data['total']:<14.2f}")
    
    print("-"*80)
    print(f"{'TOTAL INVESTMENT VALUE':<37} ${total_value:,.2f}")
    print("="*80 + "\n")


def save_to_text_file(portfolio, total_value, breakdown, filename=None):
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"portfolio_{timestamp}.txt"
    
    filepath = f"c:\\Stock Portfolio tracker\\output\\{filename}"
    
    try:
        with open(filepath, 'w') as f:
            f.write("STOCK PORTFOLIO TRACKER REPORT\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*70 + "\n\n")
            
            f.write("PORTFOLIO DETAILS\n")
            f.write("-"*70 + "\n")
            f.write(f"{'Stock':<10} {'Quantity':<15} {'Price/Share':<15} {'Total Value':<15}\n")
            f.write("-"*70 + "\n")
            
            for symbol in sorted(breakdown.keys()):
                data = breakdown[symbol]
                f.write(f"{symbol:<10} {data['quantity']:<15.2f} ${data['price']:<14.2f} ${data['total']:<14.2f}\n")
            
            f.write("-"*70 + "\n")
            f.write(f"TOTAL INVESTMENT VALUE: ${total_value:,.2f}\n")
            f.write("="*70 + "\n")
        
        print(f"✓ Portfolio saved to: {filepath}")
        return True
    except Exception as e:
        print(f"❌ Error saving to text file: {e}")
        return False


def save_to_csv_file(portfolio, total_value, breakdown, filename=None):
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"portfolio_{timestamp}.csv"
    
    filepath = f"c:\\Stock Portfolio tracker\\output\\{filename}"
    
    try:
        with open(filepath, 'w', newline='') as f:
            writer = csv.writer(f)
            
            # Header
            writer.writerow(["STOCK PORTFOLIO TRACKER REPORT"])
            writer.writerow([f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"])
            writer.writerow([])
            
            # Column headers
            writer.writerow(["Stock Symbol", "Quantity", "Price per Share", "Total Investment"])
            
            # Portfolio data
            for symbol in sorted(breakdown.keys()):
                data = breakdown[symbol]
                writer.writerow([symbol, data['quantity'], data['price'], data['total']])
            
            # Summary
            writer.writerow([])
            writer.writerow(["TOTAL PORTFOLIO VALUE", "", "", total_value])
        
        print(f"✓ Portfolio saved to: {filepath}")
        return True
    except Exception as e:
        print(f"❌ Error saving to CSV file: {e}")
        return False


def main():
    print("\n" + "="*50)
    print("   STOCK PORTFOLIO TRACKER")
    print("="*50)
    
    # Display available stocks
    display_available_stocks()
    
    # Get portfolio from user
    portfolio = get_portfolio_from_user()
    
    if not portfolio:
        print("No stocks were added to the portfolio.")
        return
    
    # Calculate values
    total_value, breakdown = calculate_portfolio_value(portfolio)
    
    # Display summary
    display_portfolio_summary(portfolio, total_value, breakdown)
    
    # Ask if user wants to save
    save_choice = input("Would you like to save the portfolio? (txt/csv/both/no): ").strip().lower()
    
    if save_choice in ["txt", "both"]:
        save_to_text_file(portfolio, total_value, breakdown)
    
    if save_choice in ["csv", "both"]:
        save_to_csv_file(portfolio, total_value, breakdown)
    
    print("\n✓ Program completed successfully!")


if __name__ == "__main__":
    main()
