"""""
tools.py
Defines custom tools for our LangChain agent to use.
Optimized to stay strictly within Groq's free tier token limits.
"""

from langchain_core.tools import tool
from tavily import TavilyClient
import config

@tool
def weather_search(query: str) -> str:
    """
    Search the web for real-time weather information for a specific location.
    Use this tool whenever the user asks for current weather conditions.
    """
    try:
        client = TavilyClient(api_key=config.TAVILY_API_KEY)
        
        # Keep the query extremely concise to prevent extra tokens
        optimized_query = f"{query} current weather temperature"
        
        # FIX: Switched depth to "basic" and dropped max_results to 2 to save tokens
        response = client.search(
            query=optimized_query, 
            search_depth="basic", 
            max_results=2
        )
        
        results = response.get("results", [])
        if not results:
            return f"No live weather information found for: '{query}'."
            
        compiled_info = []
        for index, item in enumerate(results, 1):
            title = item.get("title", "No Title")
            # FIX: Truncate the web content to 500 characters max to guarantee we never breach 6k tokens
            content = item.get("content", "No Content")[:500]
            compiled_info.append(f"Source {index}: {title}\nData: {content}\n")
            
        return "\n---\n".join(compiled_info)

    except Exception as e:
        return f"An error occurred while fetching weather data: {str(e)}"