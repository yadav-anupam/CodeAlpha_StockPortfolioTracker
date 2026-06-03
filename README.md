# Stock Portfolio Tracker

A simple Python application that helps you track your stock investments by calculating total portfolio value based on manually defined stock prices.

## Features

- ✓ **Easy Stock Input**: Add stocks and quantities interactively
- ✓ **Hardcoded Prices**: Pre-defined stock prices for quick calculations
- ✓ **Portfolio Summary**: View detailed breakdown of your investments
- ✓ **File Export**: Save your portfolio to .txt or .csv files
- ✓ **User-Friendly**: Clear prompts and formatted output

## Included Stocks

The application includes the following stocks with their prices:

| Symbol | Price  |
|--------|--------|
| AAPL   | $10.00 |
| TSLA   | $20.00 |
| GOOGL  | $60.00 |
| MSFT   | $40.00 |
| AMZN   | $80.00 |
| META   | $30.00 |
| NVDA   | $70.00 |
| AMD    | $50.00 |

## How to Use

### Running the Application

```bash
python stock_tracker.py
```

### Workflow

1. **View Available Stocks**: The app displays all available stocks and their prices
2. **Enter Portfolio**: Input stock symbols and quantities one at a time
   - Type the stock symbol (e.g., `AAPL`)
   - Enter the number of shares you own
   - Repeat until done
3. **Type "done"**: Exit the input phase
4. **View Summary**: The app displays your portfolio breakdown and total value
5. **Save (Optional)**: Choose to save to .txt, .csv, or both formats

### Example Session

```
=====================================
   STOCK PORTFOLIO TRACKER
=====================================

==================================================
AVAILABLE STOCKS
==================================================
  AMD: $50.00
  AMZN: $80.00
  AAPL: $10.00
  GOOGL: $60.00
  META: $30.00
  MSFT: $40.00
  NVDA: $70.00
  TSLA: $20.00
==================================================

Enter your stock portfolio (or 'done' when finished)
--------------------------------------------------
Enter stock symbol (or 'done' to finish): AAPL
Enter quantity for AAPL: 10
✓ Added 10.0 shares of AAPL
Enter stock symbol (or 'done' to finish): TSLA
Enter quantity for TSLA: 5
✓ Added 5.0 shares of TSLA
Enter stock symbol (or 'done' to finish): done

================================================================================
PORTFOLIO SUMMARY
================================================================================
Stock      Quantity     Price/Share     Total Value    
--------------------------------------------------------------------------------
AAPL       10.00        $10.00          $100.00        
TSLA       5.00         $20.00          $100.00        
--------------------------------------------------------------------------------
TOTAL INVESTMENT VALUE                  $200.00
================================================================================

Would you like to save the portfolio? (txt/csv/both/no): both
✓ Portfolio saved to: c:\Stock Portfolio tracker\output\portfolio_20260603_144530.txt
✓ Portfolio saved to: c:\Stock Portfolio tracker\output\portfolio_20260603_144530.csv

✓ Program completed successfully!
```

## Key Concepts Implemented

### 1. **Dictionary Usage**
- `STOCK_PRICES`: Hardcoded dictionary storing stock symbols and prices
- `portfolio`: User's stock holdings
- `breakdown`: Detailed portfolio analysis

### 2. **Input/Output**
- User input collection for stock symbols and quantities
- Formatted console output with tables and visual elements
- Error handling for invalid inputs

### 3. **Basic Arithmetic**
- Calculation: `Quantity × Price = Total Value`
- Sum calculation for total portfolio value

### 4. **File Handling**
- Text file (.txt) export with formatted report
- CSV file export for spreadsheet compatibility
- Automatic filename generation with timestamps
- Error handling for file operations

## Output Examples

### Text File Output (.txt)
```
STOCK PORTFOLIO TRACKER REPORT
Generated: 2026-06-03 14:45:30
======================================================================

PORTFOLIO DETAILS
----------------------------------------------------------------------
Stock      Quantity        Price/Share     Total Value    
----------------------------------------------------------------------
AAPL       10.00           $10.00          $100.00        
TSLA       5.00            $20.00          $100.00        
----------------------------------------------------------------------
TOTAL INVESTMENT VALUE: $200.00
======================================================================
```

### CSV File Output (.csv)
```
STOCK PORTFOLIO TRACKER REPORT
Generated: 2026-06-03 14:45:30

Stock Symbol,Quantity,Price per Share,Total Investment
AAPL,10.0,10.0,100.0
TSLA,5.0,20.0,100.0

TOTAL PORTFOLIO VALUE,,,200.0
```

## Customizing Stock Prices

To add or modify stock prices, edit the `STOCK_PRICES` dictionary in `stock_tracker.py`:

```python
STOCK_PRICES = {
    "AAPL": 10.00,
    "TSLA": 20.00,
    "GOOGL": 60.00,
    "MSFT": 40.00,
    "AMZN": 80.00,
    "META": 30.00,
    "NVDA": 70.00,
    "AMD": 50.00,
    "YOUR_STOCK": 100.00,  # Add new stocks here
}
```

## Error Handling

The application includes validation for:
- Invalid stock symbols
- Negative or zero quantities
- Non-numeric quantity inputs
- File save errors

---

**Created**: June 3, 2026  
**Version**: 1.0
**By Anupam Yadav**

Connect On Linkedin :) www.linkedin.com/in/anupam-yadavv