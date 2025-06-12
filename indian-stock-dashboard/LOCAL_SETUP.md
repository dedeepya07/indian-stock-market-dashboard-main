
# Local Setup Guide

## Prerequisites
- Python 3.11 or higher
- Git
- Anthropic API key

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/indian-stock-market-dashboard.git
cd indian-stock-market-dashboard
```

### 2. Install Dependencies
```bash
# Using pip
pip install -r requirements.txt

# Or using conda
conda install --file requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the project root:
```bash
echo "ANTHROPIC_API_KEY=your_actual_api_key_here" > .env
```

### 4. Get Your Anthropic API Key
1. Visit [console.anthropic.com](https://console.anthropic.com/)
2. Create an account or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key to your `.env` file

### 5. Run the Application
```bash
streamlit run app.py --server.port 8501
```

### 6. Access the Application
Open your browser and go to: `http://localhost:8501`

## VS Code Setup

### Create Launch Configuration
Create `.vscode/launch.json`:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Run Streamlit App",
            "type": "python",
            "request": "launch",
            "module": "streamlit",
            "args": ["run", "app.py", "--server.port", "8501"],
            "console": "integratedTerminal",
            "justMyCode": false
        }
    ]
}
```

## Troubleshooting

### Common Issues
1. **Import Errors**: Make sure all dependencies are installed
2. **API Key Errors**: Verify your Anthropic API key is correct
3. **Port Issues**: Try different ports if 8501 is occupied

### WebSocket Errors
The WebSocket errors you see in the console are normal for Streamlit and won't affect functionality.

### Performance Tips
- Start with 2-3 stocks for analysis
- Use shorter time periods (1-3 months) for faster loading
- Clear cache if data seems outdated
