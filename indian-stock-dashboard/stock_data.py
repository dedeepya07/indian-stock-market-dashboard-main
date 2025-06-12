import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import streamlit as st

class StockDataFetcher:
    """
    Class to fetch and process Indian stock market data using yfinance
    """
    
    def __init__(self):
        self.nse_suffix = ".NS"
        self.bse_suffix = ".BO"
    
    def get_stock_data(self, symbol, period="1y", add_suffix=True):
        """
        Fetch stock data for a given symbol and period
        
        Args:
            symbol (str): Stock symbol
            period (str): Time period (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
            add_suffix (bool): Whether to add NSE suffix
        
        Returns:
            pandas.DataFrame: Stock data with OHLCV columns
        """
        try:
            # Try NSE first, then BSE if NSE fails
            stock_symbol = f"{symbol}{self.nse_suffix}" if add_suffix else symbol
            
            # Create yfinance ticker object
            ticker = yf.Ticker(stock_symbol)
            
            # Fetch historical data
            stock_data = ticker.history(period=period)
            
            # If NSE data is empty or fails, try BSE
            if stock_data.empty and add_suffix:
                stock_symbol = f"{symbol}{self.bse_suffix}"
                ticker = yf.Ticker(stock_symbol)
                stock_data = ticker.history(period=period)
            
            # Clean and validate data
            if not stock_data.empty:
                # Remove timezone info for consistency
                stock_data.index = stock_data.index.tz_localize(None)
                
                # Ensure all required columns are present
                required_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
                for col in required_columns:
                    if col not in stock_data.columns:
                        stock_data[col] = np.nan
                
                # Remove rows with all NaN values
                stock_data = stock_data.dropna(how='all')
                
                # Forward fill missing values
                stock_data = stock_data.ffill()
                
                return stock_data
            else:
                return None
                
        except Exception as e:
            st.error(f"Error fetching data for {symbol}: {str(e)}")
            return None
    
    def get_current_price(self, symbol):
        """
        Get current price for a stock
        
        Args:
            symbol (str): Stock symbol
            
        Returns:
            float: Current price or None if failed
        """
        try:
            stock_data = self.get_stock_data(symbol, period="1d")
            if stock_data is not None and not stock_data.empty:
                return float(stock_data['Close'].iloc[-1])
            return None
        except:
            return None
    
    def get_stock_info(self, symbol):
        """
        Get additional stock information
        
        Args:
            symbol (str): Stock symbol
            
        Returns:
            dict: Stock information or empty dict if failed
        """
        try:
            stock_symbol = f"{symbol}{self.nse_suffix}"
            ticker = yf.Ticker(stock_symbol)
            info = ticker.info
            
            # If NSE info is empty, try BSE
            if not info or len(info) <= 1:
                stock_symbol = f"{symbol}{self.bse_suffix}"
                ticker = yf.Ticker(stock_symbol)
                info = ticker.info
            
            return info
        except:
            return {}
    
    def validate_symbol(self, symbol):
        """
        Validate if a stock symbol exists and has data
        
        Args:
            symbol (str): Stock symbol
            
        Returns:
            bool: True if symbol is valid, False otherwise
        """
        try:
            data = self.get_stock_data(symbol, period="5d")
            return data is not None and not data.empty
        except:
            return False
    
    def get_multiple_stocks_data(self, symbols, period="1y"):
        """
        Fetch data for multiple stocks
        
        Args:
            symbols (list): List of stock symbols
            period (str): Time period
            
        Returns:
            dict: Dictionary with symbol as key and DataFrame as value
        """
        stocks_data = {}
        
        for symbol in symbols:
            try:
                data = self.get_stock_data(symbol, period)
                if data is not None and not data.empty:
                    stocks_data[symbol] = data
            except Exception as e:
                st.warning(f"Failed to fetch data for {symbol}: {str(e)}")
                continue
        
        return stocks_data
    
    def calculate_basic_metrics(self, stock_data):
        """
        Calculate basic financial metrics from stock data
        
        Args:
            stock_data (pandas.DataFrame): Stock OHLCV data
            
        Returns:
            dict: Dictionary containing basic metrics
        """
        if stock_data is None or stock_data.empty:
            return {}
        
        try:
            current_price = stock_data['Close'].iloc[-1]
            
            # Price changes
            daily_change = stock_data['Close'].iloc[-1] - stock_data['Close'].iloc[-2] if len(stock_data) > 1 else 0
            daily_change_pct = (daily_change / stock_data['Close'].iloc[-2]) * 100 if len(stock_data) > 1 and stock_data['Close'].iloc[-2] != 0 else 0
            
            # High/Low
            high_52w = stock_data['High'].max()
            low_52w = stock_data['Low'].min()
            
            # Volume
            avg_volume = stock_data['Volume'].mean()
            current_volume = stock_data['Volume'].iloc[-1]
            
            # Volatility (annualized)
            daily_returns = stock_data['Close'].pct_change().dropna()
            volatility = daily_returns.std() * np.sqrt(252) * 100  # Annualized volatility
            
            # Returns
            total_return = ((current_price / stock_data['Close'].iloc[0]) - 1) * 100 if stock_data['Close'].iloc[0] != 0 else 0
            
            return {
                'current_price': current_price,
                'daily_change': daily_change,
                'daily_change_pct': daily_change_pct,
                'high_52w': high_52w,
                'low_52w': low_52w,
                'avg_volume': avg_volume,
                'current_volume': current_volume,
                'volatility': volatility,
                'total_return': total_return
            }
            
        except Exception as e:
            st.error(f"Error calculating metrics: {str(e)}")
            return {}
    
    def get_sector_stocks(self, sector=None):
        """
        Get stocks from a specific sector (placeholder for future enhancement)
        
        Args:
            sector (str): Sector name
            
        Returns:
            list: List of stock symbols in the sector
        """
        # This would require additional data sources or APIs
        # For now, return empty list
        return []
    
    def search_stocks(self, query, indian_stocks_dict):
        """
        Search for stocks based on query
        
        Args:
            query (str): Search query
            indian_stocks_dict (dict): Dictionary of Indian stocks
            
        Returns:
            list: List of matching stock symbols and names
        """
        if not query:
            return []
        
        query = query.lower()
        matches = []
        
        for symbol, name in indian_stocks_dict.items():
            if (query in symbol.lower() or 
                query in name.lower()):
                matches.append((symbol, name))
        
        return matches[:20]  # Limit to top 20 matches
