import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
import streamlit as st

class TechnicalAnalyzer:
    """
    Class for technical analysis and investment recommendations
    """
    
    def __init__(self):
        self.indicators = {}
    
    def calculate_rsi(self, prices, period=14):
        """
        Calculate Relative Strength Index (RSI) - Manual implementation
        """
        try:
            delta = prices.diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
            rs = gain / loss
            rsi = 100 - (100 / (1 + rs))
            return rsi.values
        except Exception as e:
            # Return neutral RSI if calculation fails
            return np.full(len(prices), 50.0)
    
    def calculate_macd(self, prices, fast=12, slow=26, signal=9):
        """
        Calculate MACD - Manual implementation
        """
        try:
            ema_fast = prices.ewm(span=fast).mean()
            ema_slow = prices.ewm(span=slow).mean()
            macd = ema_fast - ema_slow
            macd_signal = macd.ewm(span=signal).mean()
            macd_histogram = macd - macd_signal
            return macd.values, macd_signal.values, macd_histogram.values
        except Exception as e:
            # Return zeros if calculation fails
            zeros = np.zeros(len(prices))
            return zeros, zeros, zeros
    
    def calculate_bollinger_bands(self, prices, period=20, std_dev=2):
        """
        Calculate Bollinger Bands - Manual implementation
        """
        try:
            middle = prices.rolling(window=period).mean()
            std = prices.rolling(window=period).std()
            upper = middle + (std * std_dev)
            lower = middle - (std * std_dev)
            return upper.values, middle.values, lower.values
        except Exception as e:
            # Return price levels if calculation fails
            price_array = prices.values
            return price_array, price_array, price_array
    
    def calculate_moving_averages(self, prices, periods=[20, 50, 200]):
        """
        Calculate Simple Moving Averages
        """
        mas = {}
        for period in periods:
            try:
                mas[f'SMA_{period}'] = prices.rolling(window=period).mean().values
            except:
                mas[f'SMA_{period}'] = prices.values
        return mas
    
    def calculate_stochastic(self, high, low, close, k_period=14, d_period=3):
        """
        Calculate Stochastic Oscillator - Manual implementation
        """
        try:
            lowest_low = low.rolling(window=k_period).min()
            highest_high = high.rolling(window=k_period).max()
            k_percent = 100 * ((close - lowest_low) / (highest_high - lowest_low))
            d_percent = k_percent.rolling(window=d_period).mean()
            return k_percent.values, d_percent.values
        except Exception as e:
            # Return neutral values if calculation fails
            neutral = np.full(len(close), 50.0)
            return neutral, neutral
    
    def calculate_indicators(self, stock_data):
        """
        Calculate all technical indicators for a stock
        """
        indicators = {}
        
        try:
            close_prices = stock_data['Close']
            high_prices = stock_data['High']
            low_prices = stock_data['Low']
            
            # RSI
            rsi = self.calculate_rsi(close_prices)
            indicators['rsi'] = rsi[-1] if len(rsi) > 0 and not np.isnan(rsi[-1]) else 50
            
            # MACD
            macd, macd_signal, macd_hist = self.calculate_macd(close_prices)
            indicators['macd'] = macd[-1] if len(macd) > 0 and not np.isnan(macd[-1]) else 0
            indicators['macd_signal'] = macd_signal[-1] if len(macd_signal) > 0 and not np.isnan(macd_signal[-1]) else 0
            indicators['macd_histogram'] = macd_hist[-1] if len(macd_hist) > 0 and not np.isnan(macd_hist[-1]) else 0
            
            # Moving Averages
            mas = self.calculate_moving_averages(close_prices, [20, 50, 200])
            indicators['sma_20'] = mas['SMA_20'][-1] if len(mas['SMA_20']) > 0 and not np.isnan(mas['SMA_20'][-1]) else close_prices.iloc[-1]
            indicators['sma_50'] = mas['SMA_50'][-1] if len(mas['SMA_50']) > 0 and not np.isnan(mas['SMA_50'][-1]) else close_prices.iloc[-1]
            indicators['sma_200'] = mas['SMA_200'][-1] if len(mas['SMA_200']) > 0 and not np.isnan(mas['SMA_200'][-1]) else close_prices.iloc[-1]
            
            # Bollinger Bands
            bb_upper, bb_middle, bb_lower = self.calculate_bollinger_bands(close_prices)
            indicators['bb_upper'] = bb_upper[-1] if len(bb_upper) > 0 and not np.isnan(bb_upper[-1]) else close_prices.iloc[-1]
            indicators['bb_middle'] = bb_middle[-1] if len(bb_middle) > 0 and not np.isnan(bb_middle[-1]) else close_prices.iloc[-1]
            indicators['bb_lower'] = bb_lower[-1] if len(bb_lower) > 0 and not np.isnan(bb_lower[-1]) else close_prices.iloc[-1]
            
            # Stochastic
            stoch_k, stoch_d = self.calculate_stochastic(high_prices, low_prices, close_prices)
            indicators['stoch_k'] = stoch_k[-1] if len(stoch_k) > 0 and not np.isnan(stoch_k[-1]) else 50
            indicators['stoch_d'] = stoch_d[-1] if len(stoch_d) > 0 and not np.isnan(stoch_d[-1]) else 50
            
            # Current price
            indicators['current_price'] = close_prices.iloc[-1]
            
            # Volume indicators
            indicators['volume_sma'] = stock_data['Volume'].rolling(window=20).mean().iloc[-1]
            indicators['current_volume'] = stock_data['Volume'].iloc[-1]
            
        except Exception as e:
            # Return default values if any error occurs
            current_price = stock_data['Close'].iloc[-1] if len(stock_data) > 0 else 100
            indicators = {
                'rsi': 50, 'macd': 0, 'macd_signal': 0, 'macd_histogram': 0,
                'sma_20': current_price, 'sma_50': current_price,
                'sma_200': current_price, 'bb_upper': current_price,
                'bb_middle': current_price, 'bb_lower': current_price,
                'stoch_k': 50, 'stoch_d': 50, 'current_price': current_price,
                'volume_sma': stock_data['Volume'].iloc[-1] if len(stock_data) > 0 else 1000000,
                'current_volume': stock_data['Volume'].iloc[-1] if len(stock_data) > 0 else 1000000
            }
        
        return indicators
    
    def get_recommendation(self, stock_data):
        """
        Generate investment recommendation based on technical indicators
        """
        try:
            indicators = self.calculate_indicators(stock_data)
            
            buy_signals = 0
            sell_signals = 0
            reasons = []
            confidence = 50
            
            # RSI Analysis (Simple explanation)
            rsi = indicators['rsi']
            if rsi < 30:
                buy_signals += 2
                reasons.append(f"Stock is oversold (RSI: {rsi:.1f}) - Good buying opportunity")
            elif rsi > 70:
                sell_signals += 2
                reasons.append(f"Stock is overbought (RSI: {rsi:.1f}) - Consider selling")
            else:
                reasons.append(f"Stock momentum is neutral (RSI: {rsi:.1f})")
            
            # Price vs Moving Average Analysis
            current_price = indicators['current_price']
            sma_20 = indicators['sma_20']
            sma_50 = indicators['sma_50']
            
            if current_price > sma_20 > sma_50:
                buy_signals += 1
                reasons.append("Stock price is above short and medium-term averages - Upward trend")
            elif current_price < sma_20 < sma_50:
                sell_signals += 1
                reasons.append("Stock price is below short and medium-term averages - Downward trend")
            
            # MACD Analysis
            macd = indicators['macd']
            macd_signal = indicators['macd_signal']
            if macd > macd_signal and macd > 0:
                buy_signals += 1
                reasons.append("Technical momentum is positive - Good for buying")
            elif macd < macd_signal and macd < 0:
                sell_signals += 1
                reasons.append("Technical momentum is negative - Consider selling")
            
            # Volume Analysis
            current_volume = indicators['current_volume']
            volume_sma = indicators['volume_sma']
            
            if current_volume > volume_sma * 1.5:
                if buy_signals > sell_signals:
                    buy_signals += 0.5
                    reasons.append("High trading volume supports the buying signal")
                elif sell_signals > buy_signals:
                    sell_signals += 0.5
                    reasons.append("High trading volume supports the selling signal")
            
            # Price Momentum
            if len(stock_data) >= 5:
                recent_trend = stock_data['Close'].iloc[-5:].pct_change().mean()
                if recent_trend > 0.01:
                    buy_signals += 0.5
                    reasons.append("Recent price movement shows positive momentum")
                elif recent_trend < -0.01:
                    sell_signals += 0.5
                    reasons.append("Recent price movement shows negative momentum")
            
            # Generate recommendation
            signal_strength = abs(buy_signals - sell_signals)
            
            if buy_signals > sell_signals and signal_strength >= 1:
                signal = "BUY"
                confidence = min(60 + (signal_strength * 10), 90)
            elif sell_signals > buy_signals and signal_strength >= 1:
                signal = "SELL"
                confidence = min(60 + (signal_strength * 10), 90)
            else:
                signal = "HOLD"
                confidence = 50
                reasons.append("Mixed signals suggest waiting for better opportunity")
            
            return {
                'signal': signal,
                'confidence': confidence,
                'buy_signals': buy_signals,
                'sell_signals': sell_signals,
                'reasons': reasons[:4],  # Limit to top 4 reasons for clarity
                'indicators': indicators
            }
            
        except Exception as e:
            return {
                'signal': 'HOLD',
                'confidence': 50,
                'buy_signals': 0,
                'sell_signals': 0,
                'reasons': ['Analysis not available - Please try again'],
                'indicators': {}
            }
    
    def get_simple_explanation(self, recommendation):
        """
        Provide simple explanations for layman understanding
        """
        signal = recommendation['signal']
        confidence = recommendation['confidence']
        
        explanations = {
            'BUY': {
                'title': '🟢 BUY - Good Time to Invest',
                'simple': f'Our analysis suggests this stock is likely to go up. Confidence: {confidence:.0f}%',
                'what_it_means': 'The stock appears undervalued or in an upward trend.',
                'action': 'Consider buying if you believe in the company long-term.'
            },
            'SELL': {
                'title': '🔴 SELL - Consider Taking Profits',
                'simple': f'Our analysis suggests this stock might go down. Confidence: {confidence:.0f}%',
                'what_it_means': 'The stock appears overvalued or in a downward trend.',
                'action': 'Consider selling if you own this stock to protect gains.'
            },
            'HOLD': {
                'title': '🟡 HOLD - Wait and Watch',
                'simple': f'Mixed signals - neither strong buy nor sell. Confidence: {confidence:.0f}%',
                'what_it_means': 'The stock is in a neutral zone with unclear direction.',
                'action': 'If you own it, keep it. If not, wait for clearer signals.'
            }
        }
        
        return explanations.get(signal, explanations['HOLD'])

    def get_portfolio_suggestions(self, stocks_data):
        """
        Provide AI-powered portfolio suggestions based on current market conditions
        """
        suggestions = {
            'strong_buys': [],
            'moderate_buys': [],
            'holds': [],
            'sells': [],
            'analysis_summary': ''
        }
        
        try:
            for stock, data in stocks_data.items():
                recommendation = self.get_recommendation(data)
                signal = recommendation['signal']
                confidence = recommendation['confidence']
                
                stock_info = {
                    'symbol': stock,
                    'signal': signal,
                    'confidence': confidence,
                    'current_price': data['Close'].iloc[-1],
                    'reasons': recommendation['reasons'][:2]  # Top 2 reasons
                }
                
                if signal == 'BUY' and confidence >= 70:
                    suggestions['strong_buys'].append(stock_info)
                elif signal == 'BUY' and confidence >= 55:
                    suggestions['moderate_buys'].append(stock_info)
                elif signal == 'SELL':
                    suggestions['sells'].append(stock_info)
                else:
                    suggestions['holds'].append(stock_info)
            
            # Sort by confidence
            suggestions['strong_buys'].sort(key=lambda x: x['confidence'], reverse=True)
            suggestions['moderate_buys'].sort(key=lambda x: x['confidence'], reverse=True)
            suggestions['sells'].sort(key=lambda x: x['confidence'], reverse=True)
            
            # Generate summary
            total_stocks = len(stocks_data)
            buy_count = len(suggestions['strong_buys']) + len(suggestions['moderate_buys'])
            sell_count = len(suggestions['sells'])
            
            if buy_count > sell_count:
                market_sentiment = "Positive - More buying opportunities"
            elif sell_count > buy_count:
                market_sentiment = "Cautious - More selling signals"
            else:
                market_sentiment = "Mixed - Balanced signals"
            
            suggestions['analysis_summary'] = f"Market Sentiment: {market_sentiment}"
            
        except Exception as e:
            suggestions['analysis_summary'] = "Analysis temporarily unavailable"
        
        return suggestions