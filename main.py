import os
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# Load API keys from local configuration
try:
    from local_config import OPENAI_API_KEY, FINNHUB_API_KEY
    
    # Set environment variables for this session only
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    os.environ["FINNHUB_API_KEY"] = FINNHUB_API_KEY
    
    print("✅ API keys loaded from local configuration")
except ImportError:
    print("⚠️  local_config.py not found. Please create it with your API keys.")
    print("   See local_config.py.example for reference")
    exit(1)
except Exception as e:
    print(f"❌ Error loading API keys: {e}")
    exit(1)

# Use default config with cheaper models
config = DEFAULT_CONFIG.copy()
# The defaults are already set to:
# "deep_think_llm": "o4-mini"
# "quick_think_llm": "gpt-4o-mini"
# "llm_provider": "openai"

# For changing the models, uncomment the following lines
# config["llm_provider"] = "google"  # Use a different model
# config["backend_url"] = "https://generativelanguage.googleapis.com/v1"  # Use a different backend
# config["deep_think_llm"] = "gemini-2.0-flash"  # Use a different model
# config["quick_think_llm"] = "gemini-2.0-flash"  # Use a different model
# config["max_debate_rounds"] = 1  # Increase debate rounds
# config["online_tools"] = True  # Increase debate rounds

# Initialize with custom config
ta = TradingAgentsGraph(debug=True, config=config)

# forward propagate
_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)

# Memorize mistakes and reflect
# ta.reflect_and_remember(1000) # parameter is the position returns
