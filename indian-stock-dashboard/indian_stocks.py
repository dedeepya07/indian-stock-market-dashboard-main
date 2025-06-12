def get_indian_stocks():
    """
    Return a comprehensive dictionary of Indian stocks with their company names
    This includes major NSE and BSE listed companies
    
    Returns:
        dict: Dictionary with stock symbol as key and company name as value
    """
    
    indian_stocks = {
        # Large Cap Stocks - NIFTY 50
        "RELIANCE": "Reliance Industries Limited",
        "TCS": "Tata Consultancy Services Limited",
        "HDFCBANK": "HDFC Bank Limited",
        "INFY": "Infosys Limited",
        "HINDUNILVR": "Hindustan Unilever Limited",
        "ICICIBANK": "ICICI Bank Limited",
        "KOTAKBANK": "Kotak Mahindra Bank Limited",
        "HDFC": "Housing Development Finance Corporation Limited",
        "ITC": "ITC Limited",
        "LT": "Larsen & Toubro Limited",
        "SBIN": "State Bank of India",
        "BHARTIARTL": "Bharti Airtel Limited",
        "ASIANPAINT": "Asian Paints Limited",
        "MARUTI": "Maruti Suzuki India Limited",
        "BAJFINANCE": "Bajaj Finance Limited",
        "HCLTECH": "HCL Technologies Limited",
        "M&M": "Mahindra & Mahindra Limited",
        "AXISBANK": "Axis Bank Limited",
        "TITAN": "Titan Company Limited",
        "SUNPHARMA": "Sun Pharmaceutical Industries Limited",
        "WIPRO": "Wipro Limited",
        "ULTRACEMCO": "UltraTech Cement Limited",
        "NESTLEIND": "Nestle India Limited",
        "NTPC": "NTPC Limited",
        "POWERGRID": "Power Grid Corporation of India Limited",
        "TECHM": "Tech Mahindra Limited",
        "TATAMOTORS": "Tata Motors Limited",
        "BAJAJFINSV": "Bajaj Finserv Limited",
        "DRREDDY": "Dr. Reddy's Laboratories Limited",
        "ONGC": "Oil and Natural Gas Corporation Limited",
        "INDUSINDBK": "IndusInd Bank Limited",
        "CIPLA": "Cipla Limited",
        "EICHERMOT": "Eicher Motors Limited",
        "COALINDIA": "Coal India Limited",
        "GRASIM": "Grasim Industries Limited",
        "BRITANNIA": "Britannia Industries Limited",
        "DIVISLAB": "Divi's Laboratories Limited",
        "HEROMOTOCO": "Hero MotoCorp Limited",
        "TATASTEEL": "Tata Steel Limited",
        "HINDALCO": "Hindalco Industries Limited",
        "ADANIPORTS": "Adani Ports and Special Economic Zone Limited",
        "UPL": "UPL Limited",
        "JSWSTEEL": "JSW Steel Limited",
        "SHREECEM": "Shree Cement Limited",
        "BAJAJ-AUTO": "Bajaj Auto Limited",
        "SBILIFE": "SBI Life Insurance Company Limited",
        "HDFCLIFE": "HDFC Life Insurance Company Limited",
        "BPCL": "Bharat Petroleum Corporation Limited",
        "IOC": "Indian Oil Corporation Limited",
        "TATACONSUM": "Tata Consumer Products Limited",
        
        # Mid Cap Stocks
        "ADANIGREEN": "Adani Green Energy Limited",
        "ADANIENT": "Adani Enterprises Limited",
        "ADANITRANS": "Adani Transmission Limited",
        "APOLLOHOSP": "Apollo Hospitals Enterprise Limited",
        "BANDHANBNK": "Bandhan Bank Limited",
        "BANKBARODA": "Bank of Baroda",
        "BIOCON": "Biocon Limited",
        "BOSCHLTD": "Bosch Limited",
        "CADILAHC": "Cadila Healthcare Limited",
        "CANBK": "Canara Bank",
        "CHOLAFIN": "Cholamandalam Investment and Finance Company Limited",
        "CONCOR": "Container Corporation of India Limited",
        "COFORGE": "Coforge Limited",
        "CUMMINSIND": "Cummins India Limited",
        "DABUR": "Dabur India Limited",
        "ESCORTS": "Escorts Limited",
        "FEDERALBNK": "Federal Bank Limited",
        "GAIL": "GAIL (India) Limited",
        "GODREJCP": "Godrej Consumer Products Limited",
        "HAVELLS": "Havells India Limited",
        "IBULHSGFIN": "Indiabulls Housing Finance Limited",
        "ICICIPRULI": "ICICI Prudential Life Insurance Company Limited",
        "IDFCFIRSTB": "IDFC First Bank Limited",
        "INDIGO": "InterGlobe Aviation Limited",
        "INDUSTOWER": "Indus Towers Limited",
        "L&TFH": "L&T Finance Holdings Limited",
        "LICHSGFIN": "LIC Housing Finance Limited",
        "LUPIN": "Lupin Limited",
        "MARICO": "Marico Limited",
        "MCDOWELL-N": "United Spirits Limited",
        "MINDTREE": "Mindtree Limited",
        "MOTHERSUMI": "Motherson Sumi Systems Limited",
        "MRF": "MRF Limited",
        "MUTHOOTFIN": "Muthoot Finance Limited",
        "NMDC": "NMDC Limited",
        "PAGEIND": "Page Industries Limited",
        "PETRONET": "Petronet LNG Limited",
        "PIDILITIND": "Pidilite Industries Limited",
        "PNB": "Punjab National Bank",
        "RBLBANK": "RBL Bank Limited",
        "SAIL": "Steel Authority of India Limited",
        "SIEMENS": "Siemens Limited",
        "SRF": "SRF Limited",
        "TORNTPHARM": "Torrent Pharmaceuticals Limited",
        "TVSMOTOR": "TVS Motor Company Limited",
        "VOLTAS": "Voltas Limited",
        "ZEEL": "Zee Entertainment Enterprises Limited",
        
        # Small Cap and Other Notable Stocks
        "ACC": "ACC Limited",
        "AUROPHARMA": "Aurobindo Pharma Limited",
        "BERGEPAINT": "Berger Paints India Limited",
        "BHARATFORG": "Bharat Forge Limited",
        "BHARTIHEXA": "Bharti Hexacom Limited",
        "CANFINHOME": "Can Fin Homes Limited",
        "CHAMBLFERT": "Chambal Fertilisers and Chemicals Limited",
        "COLPAL": "Colgate Palmolive (India) Limited",
        "DLF": "DLF Limited",
        "EMAMILTD": "Emami Limited",
        "EXIDEIND": "Exide Industries Limited",
        "FORTIS": "Fortis Healthcare Limited",
        "GLENMARK": "Glenmark Pharmaceuticals Limited",
        "GODREJPROP": "Godrej Properties Limited",
        "HONAUT": "Honeywell Automation India Limited",
        "IDEA": "Vodafone Idea Limited",
        "INDIANB": "Indian Bank",
        "IRCTC": "Indian Railway Catering and Tourism Corporation Limited",
        "JINDALSTEL": "Jindal Steel & Power Limited",
        "JUBLFOOD": "Jubilant FoodWorks Limited",
        "KANSAINER": "Kansai Nerolac Paints Limited",
        "LTTS": "L&T Technology Services Limited",
        "MANAPPURAM": "Manappuram Finance Limited",
        "MFSL": "Max Financial Services Limited",
        "MINDAIND": "Minda Industries Limited",
        "NAUKRI": "Info Edge (India) Limited",
        "OBEROIRLTY": "Oberoi Realty Limited",
        "OFSS": "Oracle Financial Services Software Limited",
        "OIL": "Oil India Limited",
        "PERSISTENT": "Persistent Systems Limited",
        "PFC": "Power Finance Corporation Limited",
        "PHOENIXLTD": "Phoenix Mills Limited",
        "POLYCAB": "Polycab India Limited",
        "RAJESHEXPO": "Rajesh Exports Limited",
        "RECLTD": "REC Limited",
        "RELAXO": "Relaxo Footwears Limited",
        "SANOFI": "Sanofi India Limited",
        "SCHAEFFLER": "Schaeffler India Limited",
        "STAR": "Sterlite Technologies Limited",
        "SUNTV": "Sun TV Network Limited",
        "SUPREMEIND": "Supreme Industries Limited",
        "TATACHEM": "Tata Chemicals Limited",
        "TATAELXSI": "Tata Elxsi Limited",
        "TATAPOWER": "Tata Power Company Limited",
        "TRENT": "Trent Limited",
        "UNIONBANK": "Union Bank of India",
        "VEDL": "Vedanta Limited",
        "WHIRLPOOL": "Whirlpool of India Limited",
        
        # Banking & Financial Services
        "YESBANK": "Yes Bank Limited",
        "PEL": "Piramal Enterprises Limited",
        "BAJAJHLDNG": "Bajaj Holdings & Investment Limited",
        "SHRIRAMFIN": "Shriram Finance Limited",
        "IIFL": "India Infoline Finance Limited",
        "SRTRANSFIN": "Shriram Transport Finance Company Limited",
        
        # IT & Technology
        "MPHASIS": "Mphasis Limited",
        "LTIM": "LTIMindtree Limited",
        "KPITTECH": "KPIT Technologies Limited",
        "CYIENT": "Cyient Limited",
        "RAMPGREEN": "Ramco Systems Limited",
        
        # Pharma & Healthcare
        "ALKEM": "Alkem Laboratories Limited",
        "ABBOTINDIA": "Abbott India Limited",
        "CADILAHC": "Cadila Healthcare Limited",
        "REDUXWT": "Redux Laboratories Limited",
        
        # FMCG & Consumer Goods
        "BATINDIA": "ITC Limited",
        "GODREJIND": "Godrej Industries Limited",
        "JYOTHYLAB": "Jyothy Labs Limited",
        "RADICO": "Radico Khaitan Limited",
        "VBL": "Varun Beverages Limited",
        
        # Auto & Auto Components
        "ASHOKLEY": "Ashok Leyland Limited",
        "BALKRISIND": "Balkrishna Industries Limited",
        "BHARATFORG": "Bharat Forge Limited",
        "EXIDEIND": "Exide Industries Limited",
        "FORCEMOT": "Force Motors Limited",
        "MRF": "MRF Limited",
        "SPARC": "Sun Pharma Advanced Research Company Limited",
        
        # Infrastructure & Construction
        "IRB": "IRB Infrastructure Developers Limited",
        "JKLAKSHMI": "JK Lakshmi Cement Limited",
        "KNR": "KNR Constructions Limited",
        "NCC": "NCC Limited",
        "PNC": "Pritish Nandy Communications Limited",
        
        # Metals & Mining
        "JSWENERGY": "JSW Energy Limited",
        "JSPL": "Jindal Steel & Power Limited",
        "MOIL": "MOIL Limited",
        "RATNAMANI": "Ratnamani Metals & Tubes Limited",
        "WELCORP": "Welspun Corp Limited",
        
        # Textiles
        "ARVIND": "Arvind Limited",
        "RTNPOWER": "RattanIndia Power Limited",
        "VARDHMAN": "Vardhman Textiles Limited",
        "WELSPUN": "Welspun India Limited",
        
        # Real Estate
        "BRIGADE": "Brigade Enterprises Limited",
        "GODREJPROP": "Godrej Properties Limited",
        "IBREALEST": "Indiabulls Real Estate Limited",
        "PHOENIXLTD": "Phoenix Mills Limited",
        "SOBHA": "Sobha Limited",
        
        # Power & Energy
        "ADANIPOWER": "Adani Power Limited",
        "CESC": "CESC Limited",
        "JSWENERGY": "JSW Energy Limited",
        "NHPC": "NHPC Limited",
        "SJVN": "SJVN Limited",
        "TATAPOWER": "Tata Power Company Limited",
        
        # Telecom
        "RCOM": "Reliance Communications Limited",
        
        # Media & Entertainment
        "SAREGAMA": "Saregama India Limited",
        "TIPS": "Tips Industries Limited",
        "TVTODAY": "TV Today Network Limited",
        
        # Chemicals
        "AAVAS": "Aavas Financiers Limited",
        "ALKYLAMINE": "Alkyl Amines Chemicals Limited",
        "BALRAMCHIN": "Balrampur Chini Mills Limited",
        "DEEPAKNTR": "Deepak Nitrite Limited",
        "GHCL": "GHCL Limited",
        "GNFC": "Gujarat Narmada Valley Fertilizers Company Limited",
        "NOCIL": "NOCIL Limited",
        "TATACHEMICALS": "Tata Chemicals Limited",
        
        # Agriculture & Food Processing
        "BRITANNIA": "Britannia Industries Limited",
        "KRBL": "KRBL Limited",
        "RUCHI": "Ruchi Soya Industries Limited",
        "USHAMART": "Usha Martin Limited",
        
        # Aviation
        "SPICEJET": "SpiceJet Limited",
        
        # Others
        "BEML": "BEML Limited",
        "BEL": "Bharat Electronics Limited",
        "CROMPTON": "Crompton Greaves Consumer Electricals Limited",
        "FILATEX": "Filatex India Limited",
        "HAL": "Hindustan Aeronautics Limited",
        "KSCL": "Kaveri Seed Company Limited",
        "NETWORK18": "Network18 Media & Investments Limited",
        "ORIENTELEC": "Orient Electric Limited",
        "PHILIPCARB": "Phillips Carbon Black Limited",
        "QUESS": "Quess Corp Limited",
        "RITES": "RITES Limited",
        "TEAMLEASE": "TeamLease Services Limited",
        "UJJIVAN": "Ujjivan Financial Services Limited",
        "VSTIND": "VST Industries Limited",
        "WABCOINDIA": "Wabco India Limited",
        "ZENSARTECH": "Zensar Technologies Limited"
    }
    
    return indian_stocks

def get_nifty_50_stocks():
    """
    Get NIFTY 50 stock symbols
    
    Returns:
        list: List of NIFTY 50 stock symbols
    """
    nifty_50 = [
        "RELIANCE", "TCS", "HDFCBANK", "INFY", "HINDUNILVR",
        "ICICIBANK", "KOTAKBANK", "HDFC", "ITC", "LT",
        "SBIN", "BHARTIARTL", "ASIANPAINT", "MARUTI", "BAJFINANCE",
        "HCLTECH", "M&M", "AXISBANK", "TITAN", "SUNPHARMA",
        "WIPRO", "ULTRACEMCO", "NESTLEIND", "NTPC", "POWERGRID",
        "TECHM", "TATAMOTORS", "BAJAJFINSV", "DRREDDY", "ONGC",
        "INDUSINDBK", "CIPLA", "EICHERMOT", "COALINDIA", "GRASIM",
        "BRITANNIA", "DIVISLAB", "HEROMOTOCO", "TATASTEEL", "HINDALCO",
        "ADANIPORTS", "UPL", "JSWSTEEL", "SHREECEM", "BAJAJ-AUTO",
        "SBILIFE", "HDFCLIFE", "BPCL", "IOC", "TATACONSUM"
    ]
    return nifty_50

def get_nifty_next_50_stocks():
    """
    Get NIFTY Next 50 stock symbols
    
    Returns:
        list: List of NIFTY Next 50 stock symbols
    """
    nifty_next_50 = [
        "ADANIGREEN", "ADANIENT", "APOLLOHOSP", "BANDHANBNK", "BANKBARODA",
        "BIOCON", "BOSCHLTD", "CHOLAFIN", "COLPAL", "CONCOR",
        "DABUR", "DLF", "ESCORTS", "FEDERALBNK", "GAIL",
        "GODREJCP", "HAVELLS", "IBULHSGFIN", "ICICIPRULI", "IDFCFIRSTB",
        "INDIGO", "INDUSTOWER", "L&TFH", "LICHSGFIN", "LUPIN",
        "MARICO", "MCDOWELL-N", "MOTHERSUMI", "MRF", "MUTHOOTFIN",
        "NMDC", "OBEROIRLTY", "OIL", "PAGEIND", "PETRONET",
        "PFC", "PIDILITIND", "PNB", "RBLBANK", "RECLTD",
        "SAIL", "SIEMENS", "SRF", "TORNTPHARM", "TVSMOTOR",
        "VOLTAS", "YESBANK", "ZEEL", "ACC", "AUROPHARMA"
    ]
    return nifty_next_50

def search_indian_stocks(query):
    """
    Search for Indian stocks based on symbol or company name
    
    Args:
        query (str): Search query
        
    Returns:
        list: List of tuples (symbol, company_name) matching the query
    """
    indian_stocks = get_indian_stocks()
    query = query.lower()
    
    matches = []
    for symbol, company_name in indian_stocks.items():
        if query in symbol.lower() or query in company_name.lower():
            matches.append((symbol, company_name))
    
    return matches

def get_sector_wise_stocks():
    """
    Get stocks categorized by sectors
    
    Returns:
        dict: Dictionary with sector as key and list of stock symbols as value
    """
    sectors = {
        "Banking & Finance": [
            "HDFCBANK", "ICICIBANK", "KOTAKBANK", "SBIN", "AXISBANK",
            "INDUSINDBK", "BANDHANBNK", "FEDERALBNK", "PNB", "YESBANK"
        ],
        "Information Technology": [
            "TCS", "INFY", "HCLTECH", "WIPRO", "TECHM",
            "MINDTREE", "MPHASIS", "COFORGE", "LTTS", "PERSISTENT"
        ],
        "Oil & Gas": [
            "RELIANCE", "ONGC", "IOC", "BPCL", "GAIL",
            "OIL", "PETRONET"
        ],
        "Pharmaceuticals": [
            "SUNPHARMA", "DRREDDY", "CIPLA", "DIVISLAB", "LUPIN",
            "BIOCON", "AUROPHARMA", "TORNTPHARM", "ALKEM", "CADILAHC"
        ],
        "Automobiles": [
            "MARUTI", "M&M", "TATAMOTORS", "EICHERMOT", "HEROMOTOCO",
            "BAJAJ-AUTO", "TVSMOTOR", "ASHOKLEY", "ESCORTS", "FORCEMOT"
        ],
        "FMCG": [
            "HINDUNILVR", "ITC", "ASIANPAINT", "NESTLEIND", "BRITANNIA",
            "DABUR", "MARICO", "GODREJCP", "COLPAL", "EMAMILTD"
        ],
        "Metals & Mining": [
            "TATASTEEL", "JSWSTEEL", "HINDALCO", "COALINDIA", "SAIL",
            "NMDC", "VEDL", "JINDALSTEL", "MOIL"
        ],
        "Cement": [
            "ULTRACEMCO", "SHREECEM", "GRASIM", "ACC", "JKLAKSHMI"
        ],
        "Power & Energy": [
            "NTPC", "POWERGRID", "TATAPOWER", "ADANIGREEN", "ADANIPOWER",
            "JSWENERGY", "CESC", "NHPC", "PFC", "RECLTD"
        ],
        "Telecom": [
            "BHARTIARTL", "IDEA", "RCOM"
        ]
    }
    
    return sectors
