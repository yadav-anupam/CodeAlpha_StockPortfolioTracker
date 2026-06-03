"""
Stock Portfolio Tracker - Example/Demo Script
This script demonstrates how to use the stock tracker functionality programmatically.
"""

from stock_tracker import (
    STOCK_PRICES,
    calculate_portfolio_value,
    display_portfolio_summary,
    save_to_text_file,
    save_to_csv_file
)


def demo_portfolio_1():
    print("\n" + "="*80)
    print("DEMO 1: Basic Portfolio (Apple & Tesla)")
    print("="*80)
    
    portfolio = {
        "AAPL": 10,
        "TSLA": 5
    }
    
    print("\nPortfolio Input:")
    for symbol, quantity in portfolio.items():
        print(f"  {symbol}: {quantity} shares")
    
    total_value, breakdown = calculate_portfolio_value(portfolio)
    display_portfolio_summary(portfolio, total_value, breakdown)
    
    return portfolio, total_value, breakdown


def demo_portfolio_2():
    print("\n" + "="*80)
    print("DEMO 2: Diversified Portfolio (Tech Stocks)")
    print("="*80)
    
    portfolio = {
        "AAPL": 5,
        "MSFT": 3,
        "GOOGL": 8,
        "NVDA": 2,
        "META": 4
    }
    
    print("\nPortfolio Input:")
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        print(f"  {symbol}: {quantity} shares @ ${price:.2f}/share = ${quantity * price:,.2f}")
    
    total_value, breakdown = calculate_portfolio_value(portfolio)
    display_portfolio_summary(portfolio, total_value, breakdown)
    
    return portfolio, total_value, breakdown


def demo_portfolio_3():
    print("\n" + "="*80)
    print("DEMO 3: Single Stock Portfolio")
    print("="*80)
    
    portfolio = {
        "NVDA": 100
    }
    
    print("\nPortfolio Input:")
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        print(f"  {symbol}: {quantity} shares @ ${price:.2f}/share = ${quantity * price:,.2f}")
    
    total_value, breakdown = calculate_portfolio_value(portfolio)
    display_portfolio_summary(portfolio, total_value, breakdown)
    
    return portfolio, total_value, breakdown


def demo_show_all_stocks():
    print("\n" + "="*80)
    print("AVAILABLE STOCKS AND PRICES")
    print("="*80)
    
    total_cost_per_share = 0
    print(f"\n{'Symbol':<10} {'Price':<12} {'Cost for 10 shares':<20}")
    print("-"*50)
    
    for symbol in sorted(STOCK_PRICES.keys()):
        price = STOCK_PRICES[symbol]
        cost_10 = price * 10
        total_cost_per_share += price
        print(f"{symbol:<10} ${price:<11.2f} ${cost_10:<19,.2f}")
    
    print("-"*50)
    print(f"Average stock price: ${total_cost_per_share / len(STOCK_PRICES):.2f}")
    print(f"Total if buying 10 of each: ${sum(STOCK_PRICES.values()) * 10:,.2f}")


def demo_file_export():
    print("\n" + "="*80)
    print("DEMO 4: File Export")
    print("="*80)
    
    portfolio = {
        "AAPL": 10,
        "TSLA": 5,
        "MSFT": 7
    }
    
    total_value, breakdown = calculate_portfolio_value(portfolio)
    
    print("\nSaving portfolio to files...")
    save_to_text_file(portfolio, total_value, breakdown, "demo_portfolio.txt")
    save_to_csv_file(portfolio, total_value, breakdown, "demo_portfolio.csv")


def demo_investment_comparison():
    print("\n" + "="*80)
    print("DEMO 5: Investment Scenarios Comparison")
    print("="*80)
    
    scenarios = {
        "Conservative": {"AAPL": 20, "MSFT": 15},
        "Tech-Heavy": {"NVDA": 5, "TSLA": 10, "META": 8},
        "Balanced": {"AAPL": 10, "MSFT": 10, "GOOGL": 10, "TSLA": 5}
    }
    
    results = []
    
    for scenario_name, portfolio in scenarios.items():
        total_value, _ = calculate_portfolio_value(portfolio)
        results.append((scenario_name, total_value))
    
    print(f"\n{'Scenario':<20} {'Total Investment':<20} {'Comparison':<30}")
    print("-"*70)
    
    min_value = min(r[1] for r in results)
    max_value = max(r[1] for r in results)
    
    for name, value in results:
        diff = value - min_value
        print(f"{name:<20} ${value:>18,.2f} {'(Min)' if value == min_value else f'(+${diff:,.2f})' if value > min_value else '':<30}")


def main():
    print("\n" + "="*80)
    print("  STOCK PORTFOLIO TRACKER - DEMONSTRATION")
    print("="*80)
    
    # Demo: Show all stocks
    demo_show_all_stocks()
    
    # Demo 1: Basic portfolio
    demo_portfolio_1()
    
    # Demo 2: Diversified portfolio
    demo_portfolio_2()
    
    # Demo 3: Single stock
    demo_portfolio_3()
    
    # Demo 4: Investment comparison
    demo_investment_comparison()
    
    # Demo 5: File export
    demo_file_export()
    
    print("\n" + "="*80)
    print("  ALL DEMOS COMPLETED SUCCESSFULLY!")
    print("="*80)
    print("\nTo use the interactive version, run:")
    print("  python stock_tracker.py")
    print("\n" + "="*80 + "\n")


if __name__ == "__main__":
    main()