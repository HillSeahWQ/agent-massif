"""
Live Web Search Tool using SerpAPI
"""
import os
from typing import Optional
from dotenv import load_dotenv
import json
from serpapi import GoogleSearch

class GoogleSearchClient:
    """
    https://serpapi.com/search-api
    Initialize the GoogleSearchClient with your SerpAPI key.
        
    Args:
        api_key: Your SerpAPI API key
    """

    def __init__(
          self, 
          api_key: Optional[str] = None
    ):
        """
        Initialize the GoogleSearchClient with your SerpAPI key.
        
        Args:
            api_key: Your SerpAPI API key
        """
        self.api_key = api_key or os.getenv("SERPAPI_API_KEY")
        if not self.api_key:
            raise ValueError("SERPAPI API key not provided")

    def search(
        self,
        query: str,
        google_domain: Optional[str] = "google.com",
        **kwargs
    ):
        # Build search parameters
        params = {
            "q": query,
            "api_key": self.api_key,
        }
        
        if google_domain:
            params["google_domain"] = google_domain
        
        params.update(kwargs)
        
        # Perform the search
        search = GoogleSearch(params)
        results = search.get_dict()

        return results


if __name__ == "__main__":

    load_dotenv()
    SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

    gs_client = GoogleSearchClient()

    results = gs_client.search(
        query="hong kong thousand sunny technology",
        google_domain="google.com"
    )

    print(json.dumps(results, indent=2, ensure_ascii=False))