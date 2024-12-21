import yfinance as yf
import pandas as pd

class StockPortfolioTracker:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, shares, purchase_price):
        """Adds a stock to the portfolio."""
        self.portfolio[symbol] = {
            'shares': shares,
            'purchase_price': purchase_price
        }

    def remove_stock(self, symbol):
        """Removes a stock from the portfolio."""
        if symbol in self.portfolio:
            del self.portfolio[symbol]

    def get_current_value(self):
        """Calculates the current value of the portfolio."""
        total_value = 0
        for symbol, data in self.portfolio.items():
            try:
                current_price = yf.download(symbol)['Adj Close'][-1]
                total_value += data['shares'] * current_price
            except Exception as e:
                print(f"Error fetching data for {symbol}: {e}")
        return total_value

    def get_portfolio_performance(self):
        """Calculates the portfolio's overall performance."""
        current_value = self.get_current_value()
        initial_investment = sum(
            data['shares'] * data['purchase_price']
            for data in self.portfolio.values()
        )
        return (current_value - initial_investment) / initial_investment

    def display_portfolio(self):
        """Displays the current portfolio holdings."""
        print("Current Portfolio:")
        for symbol, data in self.portfolio.items():
            print(f"{symbol}: {data['shares']} shares")

# Example usage
portfolio_tracker = StockPortfolioTracker()

# Add some stocks
portfolio_tracker.add_stock('AAPL', 100, 150)
portfolio_tracker.add_stock('GOOG', 50, 2800)

# Display initial portfolio
portfolio_tracker.display_portfolio()

# Get and print current portfolio value
current_value = portfolio_tracker.get_current_value()
print(f"Current Portfolio Value: ${current_value:.2f}")

# Get and print portfolio performance
performance = portfolio_tracker.get_portfolio_performance()
print(f"Portfolio Performance: {performance:.2%}")

# Remove a stock
portfolio_tracker.remove_stock('GOOG')

# Display updated portfolio
portfolio_tracker.display_portfolio()