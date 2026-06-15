import requests
import hashlib
import sys
from bs4 import BeautifulSoup

# Configuration
TARGET_URL = "https://admission.uod.ac.in"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

def main():
    try:
        # Fetch the website content
        response = requests.get(TARGET_URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        
        # Parse HTML and extract ONLY visible text
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script, style, and meta tags (they often contain dynamic data)
        for tag in soup(['script', 'style', 'meta', 'link', 'noscript']):
            tag.decompose()
        
        # Get clean text content
        text_content = soup.get_text(separator=' ', strip=True)
        
        # Create hash of only the meaningful text
        page_hash = hashlib.md5(text_content.encode('utf-8')).hexdigest()
        
        print(page_hash)
        
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
