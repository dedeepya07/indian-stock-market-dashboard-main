import streamlit as st
import os
from anthropic import Anthropic
import pandas as pd
import numpy as np
from datetime import datetime
import json

class StockMarketChatbot:
    def __init__(self):
        """Initialize the chatbot with Anthropic API"""
        try:
            api_key = os.environ.get('ANTHROPIC_API_KEY')
            if not api_key:
                st.error("Anthropic API key not found. Please provide your API key.")
                self.client = None
                return
            
            self.client = Anthropic(api_key=api_key)
            self.model = "claude-3-5-sonnet-20241022"
            self.max_tokens = 1000
        except Exception as e:
            st.error(f"Failed to initialize chatbot: {str(e)}")
            self.client = None
    
    def get_market_context(self, selected_stocks, stock_data_cache, indian_stocks):
        """Prepare market context for the chatbot"""
        context = {
            "selected_stocks": selected_stocks,
            "market_data": {},
            "available_stocks": len(indian_stocks),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Add current stock data for selected stocks
        for stock in selected_stocks:
            if stock in stock_data_cache:
                data = stock_data_cache[stock]
                current_price = data['Close'].iloc[-1]
                previous_price = data['Close'].iloc[-2] if len(data) > 1 else current_price
                change_pct = ((current_price - previous_price) / previous_price) * 100 if previous_price != 0 else 0
                
                context["market_data"][stock] = {
                    "company_name": indian_stocks.get(stock, "Unknown"),
                    "current_price": round(current_price, 2),
                    "change_percent": round(change_pct, 2),
                    "high_52w": round(data['High'].max(), 2),
                    "low_52w": round(data['Low'].min(), 2),
                    "volume": int(data['Volume'].iloc[-1])
                }
        
        return context
    
    def create_system_prompt(self, context):
        """Create system prompt with current market context"""
        return f"""You are a helpful Indian stock market investment advisor chatbot. You provide clear, accurate, and easy-to-understand advice about Indian stocks and investments.

Current Context:
- Date: {context['timestamp']}
- User is analyzing {len(context['selected_stocks'])} stocks: {', '.join(context['selected_stocks'])}
- Total Indian stocks available: {context['available_stocks']}

Current Stock Data:
{json.dumps(context['market_data'], indent=2)}

Guidelines:
1. Provide simple, clear explanations suitable for beginners
2. Use Indian Rupees (₹) for all price references
3. Focus on Indian stock market (NSE/BSE)
4. Give practical, actionable advice
5. Always mention that this is for educational purposes and not financial advice
6. Be encouraging but realistic about market risks
7. Use everyday language, avoid complex jargon
8. If asked about specific stocks not in the current selection, provide general guidance
9. Help users understand technical terms in simple language
10. Suggest specific actions when appropriate (buy, sell, hold, research more)

Remember: Always end responses with a disclaimer that this is educational content and users should do their own research or consult financial advisors for investment decisions.
"""
    
    def get_local_response(self, user_question, context):
        """Get local chatbot response based on common stock market questions"""
        question_lower = user_question.lower()
        selected_stocks = context.get('selected_stocks', [])
        market_data = context.get('market_data', {})
        
        # Common investment questions with educational responses
        if any(keyword in question_lower for keyword in ['start investing', 'how to invest', 'begin']):
            return """**Getting Started with Stock Investing in India:**

1. **Open a Demat Account**: Choose a reliable broker like Zerodha, Upstox, or ICICI Direct
2. **Start Small**: Begin with ₹5,000-10,000 to learn the market
3. **Research Before Buying**: Use this dashboard to analyze stocks
4. **Diversify**: Don't put all money in one stock
5. **Long-term Approach**: Hold good stocks for years, not days

**Beginner-Friendly Stocks**: NIFTY 50 companies like Reliance, TCS, HDFC Bank

*Disclaimer: This is educational content. Consult a financial advisor before investing.*"""

        elif any(keyword in question_lower for keyword in ['buy', 'purchase']) and selected_stocks:
            stock = selected_stocks[0]
            stock_info = market_data.get(stock, {})
            current_price = stock_info.get('current_price', 'N/A')
            change = stock_info.get('change_percent', 0)
            
            trend = "positive" if change > 0 else "negative" if change < 0 else "neutral"
            
            return f"""**Analysis for {stock}:**

**Current Status:**
- Price: ₹{current_price}
- Today's Change: {change:.1f}%
- Trend: {trend.title()}

**General Investment Guidelines:**
- Buy when stock is undervalued with good fundamentals
- Check company's quarterly results and debt levels
- Consider market conditions and sector performance
- Set a target price and stop-loss before buying

**For {stock} specifically:** Use the technical analysis above to see buy/sell signals.

*This is educational guidance. Make your own investment decisions.*"""

        elif any(keyword in question_lower for keyword in ['sell', 'exit']):
            return """**When to Sell Stocks:**

1. **Target Achieved**: Sell when stock reaches your target price
2. **Fundamentals Deteriorate**: Company facing major issues
3. **Better Opportunities**: Need money for better investments
4. **Stop Loss**: Limit losses if stock falls 10-15%
5. **Rebalancing**: Maintain portfolio balance

**Avoid Emotional Selling**: Don't panic during market dips if company fundamentals are strong.

*Set clear exit strategies before investing.*"""

        elif any(keyword in question_lower for keyword in ['risk', 'risky', 'safe']):
            return """**Stock Market Risks in India:**

**High Risk Stocks:**
- Small-cap companies
- New IPOs
- Volatile sectors (crypto, biotech)

**Medium Risk:**
- Mid-cap established companies
- Sectoral funds

**Lower Risk:**
- NIFTY 50 companies
- Blue-chip stocks (TCS, Reliance, HDFC)
- Dividend-paying stocks

**Risk Management:**
- Never invest borrowed money
- Keep 6 months emergency fund separate
- Diversify across sectors
- Start with large-cap stocks

*Higher returns come with higher risks.*"""

        elif any(keyword in question_lower for keyword in ['diversify', 'portfolio']):
            return """**Portfolio Diversification Strategy:**

**Sector Allocation (Example):**
- Banking & Finance: 25%
- IT & Technology: 20%
- Healthcare & Pharma: 15%
- Consumer Goods: 15%
- Energy & Infrastructure: 15%
- Others: 10%

**Market Cap Mix:**
- Large Cap: 60-70%
- Mid Cap: 20-30%
- Small Cap: 5-10%

**Review Quarterly**: Rebalance if any sector exceeds 30% of portfolio.

*Diversification reduces risk but doesn't eliminate it.*"""

        else:
            # Default response for other questions
            return f"""**General Stock Market Guidance:**

I understand you're asking about: "{user_question}"

**Key Investment Principles:**
1. **Research First**: Analyze company financials and market position
2. **Time in Market**: Long-term investing typically outperforms short-term trading
3. **Regular Investment**: Consider SIPs for mutual funds or regular stock purchases
4. **Stay Informed**: Follow company news and quarterly results

**For Specific Stock Analysis**: Use the technical analysis and charts above for your selected stocks.

**Need More Help?** Try asking more specific questions like:
- "Should I buy [stock name]?"
- "How to analyze stock fundamentals?"
- "What's a good portfolio allocation?"

*This dashboard provides technical analysis - combine it with fundamental research for best results.*"""

    def get_response(self, user_question, context):
        """Get chatbot response using Anthropic API or local fallback"""
        if not self.client:
            return self.get_local_response(user_question, context)
        
        try:
            system_prompt = self.create_system_prompt(context)
            
            enhanced_question = f"""
User question: {user_question}

Please provide a helpful response considering the user's current stock selection and market data provided in the system context.
"""
            
            message = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=0.7,
                system=system_prompt,
                messages=[
                    {
                        "role": "user", 
                        "content": enhanced_question
                    }
                ]
            )
            
            if message.content and len(message.content) > 0:
                content_block = message.content[0]
                if hasattr(content_block, 'text'):
                    return content_block.text
                elif hasattr(content_block, 'content'):
                    return str(content_block.content)
                else:
                    return str(content_block)
            return "I couldn't generate a response. Please try again."
            
        except Exception as e:
            error_msg = str(e)
            if "credit balance is too low" in error_msg:
                # Use local response instead of showing error
                local_response = self.get_local_response(user_question, context)
                return f"""**Using Backup Knowledge Base** (API credits needed for advanced AI)

{local_response}

---
**To enable advanced AI responses:** Add credits to your Anthropic account at console.anthropic.com"""
            else:
                return self.get_local_response(user_question, context)
    
    def get_suggested_questions(self, selected_stocks):
        """Generate suggested questions based on user's selected stocks"""
        if not selected_stocks:
            return [
                "How do I start investing in Indian stocks?",
                "What are the best stocks for beginners?",
                "How much money should I invest initially?",
                "What is the difference between NSE and BSE?",
                "How do I analyze if a stock is good to buy?"
            ]
        
        stock_list = ", ".join(selected_stocks[:3])
        return [
            f"Should I buy {selected_stocks[0]} right now?",
            f"What's your opinion on {stock_list}?",
            f"How long should I hold {selected_stocks[0]}?",
            "Which of my selected stocks has the best potential?",
            "What are the risks with my current stock selection?",
            "Should I diversify more or focus on fewer stocks?",
            "When is the best time to sell stocks?",
            "How do I set a stop loss for my investments?"
        ]
    
    def format_response(self, response):
        """Format the chatbot response for better display"""
        # Split response into paragraphs for better readability
        paragraphs = response.split('\n\n')
        formatted_paragraphs = []
        
        for para in paragraphs:
            if para.strip():
                # Check if it's a list item
                if para.strip().startswith('-') or para.strip().startswith('•'):
                    formatted_paragraphs.append(para.strip())
                # Check if it's a numbered list
                elif any(para.strip().startswith(f"{i}.") for i in range(1, 10)):
                    formatted_paragraphs.append(para.strip())
                else:
                    formatted_paragraphs.append(para.strip())
        
        return '\n\n'.join(formatted_paragraphs)

class ChatInterface:
    def __init__(self, chatbot, selected_stocks, stock_data_cache, indian_stocks):
        self.chatbot = chatbot
        self.selected_stocks = selected_stocks
        self.stock_data_cache = stock_data_cache
        self.indian_stocks = indian_stocks
        
        # Initialize chat history in session state
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        if 'chat_input_key' not in st.session_state:
            st.session_state.chat_input_key = 0
    
    def display_chat_interface(self):
        """Display the main chat interface"""
        st.markdown("### 🤖 Ask Your Investment Questions")
        
        # Get market context
        context = self.chatbot.get_market_context(
            self.selected_stocks, 
            self.stock_data_cache, 
            self.indian_stocks
        )
        
        # Chat input
        user_question = st.text_input(
            "Ask me anything about stocks, investments, or market analysis:",
            placeholder="e.g., Should I buy Reliance stocks now?",
            key=f"chat_input_{st.session_state.chat_input_key}"
        )
        
        col1, col2 = st.columns([1, 4])
        
        with col1:
            if st.button("Send 💬", use_container_width=True):
                if user_question.strip():
                    self.process_question(user_question, context)
        
        with col2:
            if st.button("Clear Chat 🗑️", use_container_width=True):
                st.session_state.chat_history = []
                st.session_state.chat_input_key += 1
                st.rerun()
        
        # Suggested questions
        st.markdown("#### 💡 Suggested Questions")
        suggested = self.chatbot.get_suggested_questions(self.selected_stocks)
        
        cols = st.columns(2)
        for i, suggestion in enumerate(suggested[:6]):  # Show 6 suggestions
            with cols[i % 2]:
                if st.button(suggestion, key=f"suggest_{i}", use_container_width=True):
                    self.process_question(suggestion, context)
        
        # Display chat history
        if st.session_state.chat_history:
            st.markdown("### 💬 Chat History")
            
            # Display in reverse order (latest first)
            for i, (question, answer, timestamp) in enumerate(reversed(st.session_state.chat_history)):
                with st.expander(f"Q: {question[:50]}... ({timestamp})", expanded=(i == 0)):
                    st.markdown(f"**You asked:** {question}")
                    st.markdown("**Chatbot response:**")
                    st.markdown(answer)
                    
                    # Add action buttons
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("👍 Helpful", key=f"helpful_{len(st.session_state.chat_history)-i}"):
                            st.success("Thank you for the feedback!")
                    with col2:
                        if st.button("🔄 Ask Similar", key=f"similar_{len(st.session_state.chat_history)-i}"):
                            # Add the previous question back to input
                            st.session_state[f"chat_input_{st.session_state.chat_input_key}"] = question
                            st.rerun()
    
    def process_question(self, question, context):
        """Process user question and get response"""
        with st.spinner("🤖 Thinking about your question..."):
            response = self.chatbot.get_response(question, context)
            formatted_response = self.chatbot.format_response(response)
            
            # Add to chat history
            timestamp = datetime.now().strftime("%H:%M")
            st.session_state.chat_history.append((question, formatted_response, timestamp))
            
            # Increment input key to clear the input field
            st.session_state.chat_input_key += 1
            
            # Show immediate response
            st.success("Got your answer! Check the chat history below.")
            st.rerun()

def create_quick_help_section():
    """Create a quick help section for users"""
    with st.expander("❓ How to Use the Chatbot"):
        st.markdown("""
        **What can you ask?**
        - "Should I buy [stock name] now?"
        - "What's the difference between NIFTY 50 and other stocks?"
        - "How much should I invest in stocks?"
        - "When should I sell my stocks?"
        - "What are the risks in stock market?"
        - "How do I read stock charts?"
        - "What is RSI and MACD?"
        
        **Tips for better answers:**
        - Be specific about the stocks you're interested in
        - Mention your investment goals (short-term/long-term)
        - Ask about concepts you don't understand
        - Feel free to ask follow-up questions
        
        **Remember:** All advice is for educational purposes. Always do your own research!
        """)

def create_chatbot_sidebar(chatbot, selected_stocks, indian_stocks):
    """Create a compact chatbot interface for sidebar"""
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🤖 Quick Chat")
    
    quick_question = st.sidebar.text_input(
        "Ask quickly:",
        placeholder="Quick question...",
        key="sidebar_chat"
    )
    
    if st.sidebar.button("Ask", use_container_width=True):
        if quick_question.strip():
            context = chatbot.get_market_context(selected_stocks, {}, indian_stocks)
            with st.spinner("Getting answer..."):
                response = chatbot.get_response(quick_question, context)
                st.sidebar.markdown("**Answer:**")
                st.sidebar.markdown(response[:200] + "..." if len(response) > 200 else response)
                st.sidebar.info("For detailed answers, use the main chatbot below!")