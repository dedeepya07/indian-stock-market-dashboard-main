# MacBook Setup Guide - Indian Stock Market Dashboard

## Prerequisites
- Python 3.8 or higher (check with `python3 --version`)
- Terminal application
- Internet connection

## Step 1: Extract the Downloaded File

1. Open Terminal (press `Cmd + Space`, type "Terminal", press Enter)
2. Navigate to your Downloads folder:
   ```bash
   cd ~/Downloads
   ```
3. Extract the dashboard:
   ```bash
   tar -xzf indian-stock-dashboard.tar.gz
   ```
4. Create a dedicated folder and move files:
   ```bash
   mkdir ~/indian-stock-dashboard
   mv *.py *.md .streamlit ~/indian-stock-dashboard/
   cd ~/indian-stock-dashboard
   ```

## Step 2: Install Python Dependencies

1. Install required packages:
   ```bash
   pip3 install streamlit anthropic numpy pandas pandas-ta plotly yfinance
   ```

   If you get permission errors, use:
   ```bash
   pip3 install --user streamlit anthropic numpy pandas pandas-ta plotly yfinance
   ```

## Step 3: Get Your Anthropic API Key

1. Visit https://console.anthropic.com/
2. Create an account or sign in
3. Go to "API Keys" section
4. Click "Create Key"
5. Copy the API key (starts with `sk-ant-`)

## Step 4: Set Up Environment Variable

Create a `.env` file in your dashboard folder:
```bash
echo "ANTHROPIC_API_KEY=your_actual_api_key_here" > .env
```

Replace `your_actual_api_key_here` with your actual API key from step 3.

## Step 5: Run the Dashboard

Start the dashboard:
```bash
streamlit run app.py
```

The dashboard will automatically open in your default web browser at `http://localhost:8501`

## Troubleshooting

### If Python 3 is not installed:
Install using Homebrew:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
```

### If pip3 is not found:
```bash
python3 -m ensurepip --upgrade
```

### If streamlit won't start:
Make sure you're in the correct directory:
```bash
cd ~/indian-stock-dashboard
ls -la  # Should show app.py and other files
```

### If you get "ModuleNotFoundError":
Reinstall dependencies:
```bash
pip3 install --upgrade streamlit anthropic numpy pandas pandas-ta plotly yfinance
```

## Usage

1. **Select Stocks**: Use the sidebar to choose from popular NIFTY 50 stocks or search for specific companies
2. **Get AI Recommendations**: The dashboard will analyze your selected stocks and provide buy/sell/hold recommendations
3. **View Charts**: See price movements and technical indicators
4. **Chat with AI**: Use the chatbot feature for investment questions

## Stopping the Dashboard

Press `Ctrl + C` in the Terminal where streamlit is running.

## Running Again Later

Navigate to your dashboard folder and run:
```bash
cd ~/indian-stock-dashboard
streamlit run app.py
```

## Important Notes

- Keep your API key secure and never share it
- The dashboard uses real market data from Yahoo Finance
- Recommendations are for educational purposes only
- Always do your own research before investing

## File Structure
Your dashboard folder should contain:
- `app.py` - Main application
- `stock_data.py` - Data fetching
- `technical_analysis.py` - Analysis engine
- `chatbot.py` - AI assistant
- `indian_stocks.py` - Stock database
- `.streamlit/config.toml` - Configuration
- `.env` - Your API key (you create this)
- Various `.md` files - Documentation