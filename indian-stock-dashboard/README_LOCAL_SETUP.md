# Indian Stock Market Dashboard - MacBook Setup

This guide will help you run the Indian Stock Market Dashboard locally on your MacBook.

## Prerequisites

- macOS with Python 3.8 or higher
- Terminal access
- Internet connection

## Quick Setup (Recommended)

### 1. Install Python and pip (if not already installed)

```bash
# Check if Python 3 is installed
python3 --version

# If not installed, install via Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
```

### 2. Create Project Directory

```bash
# Create a new directory for the project
mkdir indian-stock-dashboard
cd indian-stock-dashboard
```

### 3. Download Project Files

Copy all the Python files from this project to your local directory:
- `app.py` (main application)
- `stock_data.py` (data fetching)
- `technical_analysis.py` (analysis engine)
- `indian_stocks.py` (stock database)
- `chatbot.py` (AI assistant)
- `setup_requirements.txt` (dependencies)

### 4. Set Up Virtual Environment

```bash
# Create virtual environment
python3 -m venv stock_env

# Activate virtual environment
source stock_env/bin/activate

# You should see (stock_env) in your terminal prompt
```

### 5. Install Dependencies

```bash
# Install required packages
pip install -r setup_requirements.txt
```

### 6. Set Up API Key (Optional)

The chatbot works without an API key using local knowledge. To enable advanced AI features:

```bash
# Create environment file
echo "ANTHROPIC_API_KEY=your_api_key_here" > .env
```

### 7. Create Streamlit Configuration

```bash
# Create streamlit config directory
mkdir -p .streamlit

# Create config file
cat > .streamlit/config.toml << EOF
[server]
headless = true
address = "localhost"
port = 8501

[browser]
gatherUsageStats = false
EOF
```

### 8. Run the Application

```bash
# Start the dashboard
streamlit run app.py
```

The application will automatically open in your default browser at `http://localhost:8501`

## Alternative Setup with pip only

If you prefer not to use virtual environment:

```bash
# Install globally (not recommended but simpler)
pip3 install streamlit anthropic numpy pandas pandas-ta plotly yfinance python-dotenv

# Run the app
streamlit run app.py
```

## Features Available Locally

- **Stock Selection**: Choose from 500+ Indian stocks
- **Technical Analysis**: RSI, MACD, Bollinger Bands, Moving Averages
- **Price Charts**: Interactive Plotly charts
- **Investment Recommendations**: AI-powered buy/sell/hold signals
- **Portfolio Analysis**: Multi-stock comparison
- **Chatbot**: Investment guidance (works offline with local knowledge)

## Usage Tips

1. **Stock Selection**: Use the sidebar to filter by category (NIFTY 50, Banking, IT, etc.)
2. **Search**: Type company names to find specific stocks
3. **Analysis Period**: Choose from 1 month to 2 years of data
4. **Chatbot**: Ask questions like "Should I buy RELIANCE?" or "How to start investing?"

## Troubleshooting

### Common Issues:

**"Module not found" errors:**
```bash
# Make sure virtual environment is activated
source stock_env/bin/activate
pip install -r setup_requirements.txt
```

**Port already in use:**
```bash
# Use a different port
streamlit run app.py --server.port 8502
```

**Data not loading:**
- Check internet connection (yfinance needs internet)
- Some stocks may have different symbols - try searching by company name

**Chatbot not responding:**
- The app works without API key using local knowledge
- For advanced AI features, add your Anthropic API key to .env file

## Performance Tips

- **Faster Loading**: Start with fewer stocks, add more as needed
- **Memory Usage**: Clear cache if app becomes slow (Settings > Clear Cache in Streamlit)
- **Data Updates**: Refresh analysis button updates all data

## Security Notes

- Never commit .env file with API keys to version control
- API key is optional - app works fully without it
- All data comes from Yahoo Finance (free and reliable)

## Updating the App

```bash
# Pull latest changes and update dependencies
cd indian-stock-dashboard
source stock_env/bin/activate
pip install --upgrade -r setup_requirements.txt
```

## Stopping the Application

- Press `Ctrl+C` in terminal to stop
- Type `deactivate` to exit virtual environment

---

**Support**: The dashboard provides educational content only. Always do your own research or consult financial advisors before investing.