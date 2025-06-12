import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time
import os

# Load environment variables for local development
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not available in Replit environment

from stock_data import StockDataFetcher
from technical_analysis import TechnicalAnalyzer
from indian_stocks import get_indian_stocks, get_nifty_50_stocks, get_nifty_next_50_stocks, get_sector_wise_stocks
from chatbot import StockMarketChatbot, ChatInterface, create_quick_help_section, create_chatbot_sidebar

# Configure page
st.set_page_config(
    page_title="Indian Stock Market Dashboard - Easy Investment Guide",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better appearance
st.markdown("""
<style>
    .big-font {
        font-size:20px !important;
        font-weight: bold;
    }
    .recommendation-box {
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        border: 2px solid;
    }
    .buy-box {
        border-color: #28a745;
        background-color: rgba(40, 167, 69, 0.1);
    }
    .sell-box {
        border-color: #dc3545;
        background-color: rgba(220, 53, 69, 0.1);
    }
    .hold-box {
        border-color: #ffc107;
        background-color: rgba(255, 193, 7, 0.1);
    }
    .simple-explanation {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
        border-left: 4px solid #007bff;
    }
    .ai-suggestion {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        margin: 20px 0;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'selected_stocks' not in st.session_state:
    st.session_state.selected_stocks = []
if 'stock_data_cache' not in st.session_state:
    st.session_state.stock_data_cache = {}

# Initialize data fetcher and analyzer
@st.cache_resource
def get_data_fetcher():
    return StockDataFetcher()

@st.cache_resource
def get_technical_analyzer():
    return TechnicalAnalyzer()

data_fetcher = get_data_fetcher()
analyzer = get_technical_analyzer()

# Initialize chatbot
@st.cache_resource
def get_chatbot():
    return StockMarketChatbot()

chatbot = get_chatbot()

# Main title
st.markdown("""
<div style="text-align: center; padding: 20px; background: linear-gradient(90deg, #1f77b4, #2ca02c); 
            border-radius: 15px; color: white; margin-bottom: 30px;">
    <h1>🇮🇳 Indian Stock Market - Easy Investment Guide</h1>
    <h3>Simple Stock Analysis for Everyone</h3>
    <p>Get easy-to-understand investment advice powered by AI</p>
</div>
""", unsafe_allow_html=True)

# Sidebar for stock selection
st.sidebar.header("📈 Choose Your Stocks")

# Get Indian stocks list
indian_stocks = get_indian_stocks()
nifty_50 = get_nifty_50_stocks()
sector_stocks = get_sector_wise_stocks()

# Simple filter options
filter_option = st.sidebar.selectbox(
    "📂 Choose Category",
    ["Popular Stocks (NIFTY 50)", "All Stocks", "Banking Stocks", "IT Stocks", "Pharma Stocks"],
    index=0
)

# Filter stocks based on selection
if filter_option == "Popular Stocks (NIFTY 50)":
    available_stocks = {symbol: indian_stocks[symbol] for symbol in nifty_50 if symbol in indian_stocks}
elif filter_option == "Banking Stocks":
    banking_stocks = sector_stocks.get("Banking & Finance", [])
    available_stocks = {symbol: indian_stocks[symbol] for symbol in banking_stocks if symbol in indian_stocks}
elif filter_option == "IT Stocks":
    it_stocks = sector_stocks.get("Information Technology", [])
    available_stocks = {symbol: indian_stocks[symbol] for symbol in it_stocks if symbol in indian_stocks}
elif filter_option == "Pharma Stocks":
    pharma_stocks = sector_stocks.get("Pharmaceuticals", [])
    available_stocks = {symbol: indian_stocks[symbol] for symbol in pharma_stocks if symbol in indian_stocks}
else:
    available_stocks = indian_stocks

# Search functionality
search_term = st.sidebar.text_input(
    "🔍 Search for a company", 
    placeholder="Type company name...",
    help="Search by company name"
)

# Filter based on search
if search_term:
    filtered_stocks = {
        symbol: name for symbol, name in available_stocks.items() 
        if search_term.lower() in name.lower()
    }
    if filtered_stocks:
        st.sidebar.success(f"Found {len(filtered_stocks)} companies")
        available_stocks = filtered_stocks
    else:
        st.sidebar.warning("No companies found. Try a different search.")

# Stock selection
if available_stocks:
    stock_names = [f"{name} ({symbol})" for symbol, name in available_stocks.items()]
    
    selected_stock_display = st.sidebar.selectbox(
        "Select a company to analyze:",
        options=["Choose a company..."] + stock_names,
        index=0
    )
    
    if selected_stock_display and selected_stock_display != "Choose a company...":
        # Extract symbol from the display text
        selected_symbol = selected_stock_display.split('(')[-1].replace(')', '')
        
        if st.sidebar.button("📊 Analyze This Stock", use_container_width=True):
            if selected_symbol not in st.session_state.selected_stocks:
                st.session_state.selected_stocks.append(selected_symbol)
                st.sidebar.success(f"Added {selected_symbol} for analysis!")
                st.rerun()
            else:
                st.sidebar.info(f"{selected_symbol} is already being analyzed!")

# Display selected stocks
if st.session_state.selected_stocks:
    st.sidebar.subheader("📋 Your Selected Stocks")
    for i, stock in enumerate(st.session_state.selected_stocks):
        col1, col2 = st.sidebar.columns([3, 1])
        col1.write(f"**{stock}** - {indian_stocks.get(stock, 'Unknown')[:20]}...")
        if col2.button("❌", key=f"remove_{i}"):
            st.session_state.selected_stocks.remove(stock)
            if stock in st.session_state.stock_data_cache:
                del st.session_state.stock_data_cache[stock]
            st.rerun()
    
    if st.sidebar.button("🗑️ Clear All", use_container_width=True):
        st.session_state.selected_stocks = []
        st.session_state.stock_data_cache = {}
        st.rerun()

# Add quick chatbot to sidebar
create_chatbot_sidebar(chatbot, st.session_state.selected_stocks, indian_stocks)

# Time period selection
st.sidebar.subheader("⏱️ Analysis Period")
period_options = {
    "1 Month": "1mo",
    "3 Months": "3mo", 
    "6 Months": "6mo",
    "1 Year": "1y",
    "2 Years": "2y"
}

selected_period = st.sidebar.selectbox(
    "How far back to analyze:",
    list(period_options.keys()),
    index=2  # Default to 6 months
)
period = period_options[selected_period]

# Main content
if not st.session_state.selected_stocks:
    # Welcome screen
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="ai-suggestion">
            <h2>🚀 Welcome to Your Investment Assistant!</h2>
            <h4>How it works:</h4>
            <p>1️⃣ Choose stocks from the sidebar</p>
            <p>2️⃣ Get simple AI-powered recommendations</p>
            <p>3️⃣ See easy charts and explanations</p>
            <p>4️⃣ Make informed investment decisions</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Show some popular stocks as examples
    st.subheader("🌟 Popular Stocks to Get Started")
    popular_examples = ["RELIANCE", "TCS", "HDFCBANK", "INFY", "ITC"]
    
    cols = st.columns(5)
    for i, stock in enumerate(popular_examples):
        with cols[i]:
            if st.button(f"📈 {stock}\n{indian_stocks.get(stock, '')[:15]}...", key=f"pop_{stock}"):
                if stock not in st.session_state.selected_stocks:
                    st.session_state.selected_stocks.append(stock)
                    st.rerun()

else:
    # AI-Powered Investment Suggestions
    st.markdown("""
    <div class="ai-suggestion">
        <h2>🤖 AI Investment Advisor</h2>
        <h4>Analyzing your selected stocks for the best opportunities...</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Fetch data for selected stocks
    with st.spinner("📊 Getting latest market data and running AI analysis..."):
        for stock in st.session_state.selected_stocks:
            if stock not in st.session_state.stock_data_cache:
                try:
                    stock_data = data_fetcher.get_stock_data(stock, period)
                    if stock_data is not None and not stock_data.empty:
                        st.session_state.stock_data_cache[stock] = stock_data
                except Exception as e:
                    st.error(f"Could not get data for {stock}. Please try again.")
    
    # Get AI portfolio suggestions
    if st.session_state.stock_data_cache:
        suggestions = analyzer.get_portfolio_suggestions(st.session_state.stock_data_cache)
        
        # Display AI suggestions prominently
        st.subheader("🎯 AI Investment Recommendations Right Now")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🟢 **TOP PICKS TO BUY**")
            if suggestions['strong_buys']:
                for stock_info in suggestions['strong_buys'][:3]:  # Top 3
                    st.markdown(f"""
                    <div class="recommendation-box buy-box">
                        <h4>🚀 {stock_info['symbol']} - {indian_stocks.get(stock_info['symbol'], '')}</h4>
                        <p><strong>AI Confidence:</strong> {stock_info['confidence']:.0f}%</p>
                        <p><strong>Current Price:</strong> ₹{stock_info['current_price']:.2f}</p>
                        <p><strong>Why Buy:</strong> {stock_info['reasons'][0] if stock_info['reasons'] else 'Strong technical signals'}</p>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("No strong buy signals found in your selected stocks right now.")
        
        with col2:
            st.markdown("### 🔴 **CONSIDER SELLING**")
            if suggestions['sells']:
                for stock_info in suggestions['sells'][:3]:  # Top 3
                    st.markdown(f"""
                    <div class="recommendation-box sell-box">
                        <h4>📉 {stock_info['symbol']} - {indian_stocks.get(stock_info['symbol'], '')}</h4>
                        <p><strong>AI Confidence:</strong> {stock_info['confidence']:.0f}%</p>
                        <p><strong>Current Price:</strong> ₹{stock_info['current_price']:.2f}</p>
                        <p><strong>Why Sell:</strong> {stock_info['reasons'][0] if stock_info['reasons'] else 'Showing weakness'}</p>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.success("No sell signals - your stocks look stable!")
        
        # Market summary
        st.markdown(f"""
        <div class="simple-explanation">
            <h4>📊 Overall Market Analysis</h4>
            <p>{suggestions['analysis_summary']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Individual stock analysis
    st.subheader("📈 Detailed Analysis of Your Stocks")
    
    for stock in st.session_state.selected_stocks:
        if stock in st.session_state.stock_data_cache:
            stock_data = st.session_state.stock_data_cache[stock]
            
            st.markdown(f"### 📊 {stock} - {indian_stocks.get(stock, 'Unknown Company')}")
            
            # Basic stock info
            current_price = stock_data['Close'].iloc[-1]
            previous_price = stock_data['Close'].iloc[-2] if len(stock_data) > 1 else current_price
            price_change = current_price - previous_price
            price_change_pct = (price_change / previous_price) * 100 if previous_price != 0 else 0
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("💰 Current Price", f"₹{current_price:.2f}", 
                         delta=f"{price_change_pct:.1f}%")
            
            with col2:
                high_52w = stock_data['High'].max()
                st.metric("📈 52-Week High", f"₹{high_52w:.2f}")
            
            with col3:
                low_52w = stock_data['Low'].min()
                st.metric("📉 52-Week Low", f"₹{low_52w:.2f}")
            
            with col4:
                volume = stock_data['Volume'].iloc[-1]
                st.metric("📊 Today's Volume", f"{volume:,.0f}")
            
            # AI Recommendation
            try:
                recommendation = analyzer.get_recommendation(stock_data)
                explanation = analyzer.get_simple_explanation(recommendation)
                
                # Display recommendation with simple explanation
                signal_class = {
                    'BUY': 'buy-box',
                    'SELL': 'sell-box', 
                    'HOLD': 'hold-box'
                }.get(recommendation['signal'], 'hold-box')
                
                st.markdown(f"""
                <div class="recommendation-box {signal_class}">
                    <h3>{explanation['title']}</h3>
                    <p class="big-font">{explanation['simple']}</p>
                    <p><strong>What this means:</strong> {explanation['what_it_means']}</p>
                    <p><strong>What you should do:</strong> {explanation['action']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Simple reasons
                if recommendation['reasons']:
                    st.markdown("**🧠 AI Analysis Reasons:**")
                    for reason in recommendation['reasons']:
                        st.write(f"• {reason}")
                
            except Exception as e:
                st.warning("Could not generate recommendation for this stock. Please try refreshing.")
            
            # Simple price chart
            try:
                fig = go.Figure()
                
                # Add price line
                fig.add_trace(go.Scatter(
                    x=stock_data.index,
                    y=stock_data['Close'],
                    mode='lines',
                    name='Stock Price',
                    line=dict(color='blue', width=3)
                ))
                
                # Add moving average for trend
                if len(stock_data) >= 20:
                    ma_20 = stock_data['Close'].rolling(20).mean()
                    fig.add_trace(go.Scatter(
                        x=stock_data.index,
                        y=ma_20,
                        mode='lines',
                        name='20-Day Average (Trend)',
                        line=dict(color='orange', width=2, dash='dash')
                    ))
                
                fig.update_layout(
                    title=f"{stock} Price Movement - {selected_period}",
                    xaxis_title="Date",
                    yaxis_title="Price (₹)",
                    height=400,
                    template="plotly_white"
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
            except Exception as e:
                st.error("Could not create chart for this stock.")
            
            # Profit/Loss if you had invested
            st.markdown("#### 💡 What if you had invested ₹10,000?")
            
            try:
                periods = [30, 90, 180]
                returns_data = []
                
                for days in periods:
                    if len(stock_data) > days:
                        past_price = stock_data['Close'].iloc[-days-1]
                        shares_bought = 10000 / past_price
                        current_value = shares_bought * current_price
                        profit_loss = current_value - 10000
                        
                        period_name = f"{days} days ago"
                        if days == 30:
                            period_name = "1 month ago"
                        elif days == 90:
                            period_name = "3 months ago"
                        elif days == 180:
                            period_name = "6 months ago"
                        
                        returns_data.append({
                            'period': period_name,
                            'investment': 10000,
                            'current_value': current_value,
                            'profit_loss': profit_loss
                        })
                
                if returns_data:
                    cols = st.columns(len(returns_data))
                    for i, (col, data) in enumerate(zip(cols, returns_data)):
                        with col:
                            profit_color = "normal" if data['profit_loss'] >= 0 else "inverse"
                            col.metric(
                                f"If invested {data['period']}",
                                f"₹{data['current_value']:,.0f}",
                                delta=f"₹{data['profit_loss']:,.0f}",
                                delta_color=profit_color
                            )
            
            except Exception as e:
                st.info("Profit/loss calculation not available for this period.")
            
            st.divider()

# Add comprehensive chatbot interface
st.markdown("---")
st.markdown("## 🤖 Stock Market Investment Assistant")
st.markdown("Ask any questions about your investments, market analysis, or get personalized advice!")

# Create chatbot interface
if st.session_state.selected_stocks or True:  # Always show chatbot
    chat_interface = ChatInterface(
        chatbot, 
        st.session_state.selected_stocks, 
        st.session_state.stock_data_cache, 
        indian_stocks
    )
    
    # Create tabs for better organization
    tab1, tab2 = st.tabs(["💬 Chat with AI", "❓ Help & Examples"])
    
    with tab1:
        chat_interface.display_chat_interface()
    
    with tab2:
        create_quick_help_section()
        
        st.markdown("### 🎯 Smart Questions Based on Your Stocks")
        if st.session_state.selected_stocks:
            for stock in st.session_state.selected_stocks[:3]:
                company_name = indian_stocks.get(stock, stock)
                st.markdown(f"""
                **Questions about {stock} ({company_name}):**
                - Is {stock} a good buy right now?
                - What are the risks of investing in {company_name}?
                - How long should I hold {stock} stocks?
                - What's the target price for {stock}?
                """)
        else:
            st.info("Select some stocks to get personalized question suggestions!")

# Add helpful information at the bottom
st.markdown("---")
st.markdown("""
### 📚 Understanding the Recommendations

**🟢 BUY:** The AI thinks this stock might go up in price. Good time to invest if you believe in the company.

**🔴 SELL:** The AI thinks this stock might go down. If you own it, consider selling to protect your money.

**🟡 HOLD:** Mixed signals. If you own it, keep it. If you don't own it, wait for a clearer signal.

**⚠️ Important:** This is for educational purposes only. Always do your own research and consider consulting a financial advisor before investing.
""")

# Auto-refresh option
if st.session_state.selected_stocks:
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔄 Refresh Analysis", use_container_width=True):
            st.session_state.stock_data_cache = {}
            st.rerun()
    
    with col2:
        st.info("💡 Data updates automatically. Refresh for latest analysis.")