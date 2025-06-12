
# 🇮🇳 Indian Stock Market Dashboard - Easy Investment Guide

A comprehensive, AI-powered stock market analysis platform designed specifically for Indian stocks, making investment decisions accessible to everyone from beginners to experienced traders.

## 🚀 Features Overview

### 📊 **Smart Stock Analysis**
- **Real-time Data**: Live stock prices from NSE (National Stock Exchange) and BSE (Bombay Stock Exchange)
- **Technical Indicators**: RSI, MACD, Bollinger Bands, Moving Averages, Stochastic Oscillator
- **AI-Powered Recommendations**: Get BUY/SELL/HOLD signals with confidence levels
- **Simple Explanations**: Complex technical analysis made easy to understand

### 🤖 **AI Investment Assistant**
- **Conversational Chatbot**: Ask questions about stocks, market trends, and investment strategies
- **Personalized Advice**: Get recommendations based on your selected stocks
- **Educational Support**: Learn about technical indicators and market concepts
- **Quick Help**: Suggested questions to get you started

### 📈 **Stock Selection & Analysis**
- **NIFTY 50 Focus**: Easy access to India's top 50 companies
- **Sector-wise Filtering**: Banking, IT, Pharma, Auto, FMCG, and more
- **Advanced Search**: Find stocks by company name
- **Multiple Stock Analysis**: Compare multiple stocks simultaneously

### 💰 **Investment Insights**
- **Profit/Loss Calculator**: See potential returns for different investment periods
- **Price Movement Charts**: Interactive charts with trend analysis
- **Volume Analysis**: Trading volume trends and patterns
- **52-Week High/Low**: Key price levels for investment decisions

### 🎯 **Portfolio Recommendations**
- **Top Picks**: AI-curated list of best buying opportunities
- **Risk Assessment**: Identify stocks to sell or avoid
- **Market Sentiment**: Overall market analysis and trends
- **Confidence Scores**: AI confidence levels for each recommendation

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Data Source**: Yahoo Finance API via yfinance
- **AI Integration**: Anthropic Claude for intelligent recommendations
- **Visualization**: Plotly for interactive charts
- **Technical Analysis**: Custom-built indicators and algorithms

## 📁 Project Structure

```
├── app.py                    # Main application file with UI and logic
├── chatbot.py               # AI chatbot implementation using Anthropic Claude
├── indian_stocks.py         # Comprehensive database of Indian stocks
├── stock_data.py           # Stock data fetching and processing
├── technical_analysis.py   # Technical indicators and recommendation engine
├── pyproject.toml          # Project dependencies
└── README.md              # This file
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.11+
- Anthropic API key for AI features

### Quick Start on Replit
1. **Clone this repository** to your Replit workspace
2. **Set up API Key**:
   - Go to Secrets tab in Replit
   - Add `ANTHROPIC_API_KEY` with your Anthropic API key
3. **Run the application**:
   - Click the "Run" button
   - Access your app at the provided URL

### Manual Installation

#### From GitHub Repository
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/indian-stock-market-dashboard.git
cd indian-stock-market-dashboard

# Install dependencies
pip install -r requirements.txt

# Create environment file
echo "ANTHROPIC_API_KEY=your_api_key_here" > .env

# Run the application
streamlit run app.py --server.port 5000
```

#### Direct Installation
```bash
# Install dependencies
pip install streamlit yfinance plotly pandas numpy anthropic pandas-ta python-dotenv

# Run the application
streamlit run app.py --server.port 5000
```

## 🔑 Key Features Explained

### 1. **AI-Powered Recommendations**
The system analyzes multiple technical indicators to provide investment recommendations:
- **RSI Analysis**: Identifies overbought/oversold conditions
- **MACD Signals**: Momentum and trend analysis
- **Moving Average Trends**: Price direction and support/resistance
- **Volume Confirmation**: Validates price movements with trading volume

### 2. **User-Friendly Interface**
- **Beginner-Friendly**: Technical jargon explained in simple terms
- **Visual Charts**: Easy-to-read price charts with trend lines
- **Color-Coded Signals**: Green for buy, red for sell, yellow for hold
- **Metric Cards**: Key information at a glance

### 3. **Comprehensive Stock Database**
- **500+ Indian Stocks**: Major companies from NSE and BSE
- **Sector Classification**: Organized by industry for easy browsing
- **Search Functionality**: Find stocks quickly by company name
- **Real-time Updates**: Live price data and market movements

### 4. **Investment Education**
- **Simple Explanations**: What each recommendation means
- **Action Guidance**: Clear next steps for each signal
- **Risk Awareness**: Educational disclaimers and risk information
- **Learning Resources**: Built-in help and examples

### 5. **Interactive Chatbot**
Ask questions like:
- "Should I buy Reliance stocks now?"
- "What's the difference between NIFTY 50 and other stocks?"
- "How much should I invest initially?"
- "What are the risks in stock market?"

## 📊 Technical Indicators Explained

### **RSI (Relative Strength Index)**
- **Range**: 0-100
- **Buy Signal**: Below 30 (oversold)
- **Sell Signal**: Above 70 (overbought)

### **MACD (Moving Average Convergence Divergence)**
- **Signal**: When MACD line crosses above/below signal line
- **Trend**: Positive values indicate upward momentum

### **Moving Averages**
- **SMA 20**: Short-term trend (20 days)
- **SMA 50**: Medium-term trend (50 days)
- **SMA 200**: Long-term trend (200 days)

### **Bollinger Bands**
- **Upper Band**: Potential resistance level
- **Lower Band**: Potential support level
- **Price Position**: Indicates volatility and potential reversals

## 🎯 How to Use

### **Step 1: Select Stocks**
1. Choose from popular NIFTY 50 stocks
2. Filter by sector (Banking, IT, Pharma, etc.)
3. Search for specific companies
4. Add multiple stocks for comparison

### **Step 2: Analyze Recommendations**
1. View AI-powered buy/sell signals
2. Read simple explanations for each recommendation
3. Check confidence levels and reasoning
4. Review technical indicator summaries

### **Step 3: Make Informed Decisions**
1. Consider the AI recommendations
2. Review your risk tolerance
3. Check historical performance
4. Use the profit/loss calculator

### **Step 4: Get Additional Insights**
1. Ask the AI chatbot specific questions
2. Learn about technical concepts
3. Get personalized advice
4. Stay updated with market trends

## 📱 Features in Detail

### **Dashboard Layout**
- **Header**: Project title and navigation
- **Sidebar**: Stock selection and filters
- **Main Area**: AI recommendations and analysis
- **Charts**: Interactive price movements
- **Chatbot**: Q&A section at bottom

### **Stock Selection Panel**
- **Category Filters**: Popular stocks, All stocks, Sector-specific
- **Search Bar**: Type company names for quick access
- **Selected Stocks**: Manage your watchlist
- **Quick Actions**: Add/remove stocks easily

### **AI Recommendation Engine**
- **Portfolio Analysis**: Overall investment suggestions
- **Individual Stock Analysis**: Detailed recommendations per stock
- **Confidence Scoring**: AI certainty levels (50-90%)
- **Reasoning**: Why each recommendation was made

### **Interactive Charts**
- **Price Movement**: Historical price trends
- **Moving Averages**: Trend indicators overlay
- **Volume Data**: Trading activity visualization
- **Responsive Design**: Works on all screen sizes

### **Investment Calculator**
- **What-if Scenarios**: Returns for ₹10,000 investment
- **Multiple Timeframes**: 1 month, 3 months, 6 months
- **Profit/Loss Display**: Clear gain/loss indicators
- **Indian Rupee Format**: All prices in ₹ (INR)

## ⚠️ Important Disclaimers

- **Educational Purpose**: This tool is for educational purposes only
- **Not Financial Advice**: Always consult qualified financial advisors
- **Market Risks**: Stock investments carry inherent risks
- **Research Required**: Do your own research before investing
- **No Guarantees**: Past performance doesn't guarantee future results

## 🔐 Security & Privacy

- **API Security**: Anthropic API key stored securely in environment variables
- **No Personal Data**: No storage of personal financial information
- **Open Source**: Code is transparent and auditable
- **Local Processing**: Analysis happens on your device

## 🤝 Contributing

We welcome contributions! Areas for improvement:
- Additional technical indicators
- More Indian stock exchanges
- Enhanced AI recommendations
- Mobile responsiveness
- Performance optimizations

## 📞 Support

- **Issues**: Report bugs or request features via GitHub issues
- **Documentation**: Comprehensive help within the application
- **Community**: Join discussions about Indian stock market analysis

## 🏆 Why Choose This Platform?

### **For Beginners**
- Simple, jargon-free explanations
- AI-guided investment decisions
- Educational chatbot assistance
- Risk-aware recommendations

### **For Experienced Traders**
- Comprehensive technical analysis
- Multiple indicator confirmation
- Batch stock analysis
- Customizable time periods

### **For Indian Market Focus**
- NSE and BSE integration
- Rupee-denominated analysis
- Local market understanding
- Sector-specific insights

## 🎉 Get Started Today!

1. **Run the application** on Replit
2. **Add your favorite stocks** to the watchlist
3. **Get AI recommendations** instantly
4. **Start your investment journey** with confidence

---

**Made with ❤️ for Indian investors | Powered by AI | Educational purposes only**

*Remember: The best investment you can make is in your financial education!*
