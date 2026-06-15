import requests
import hashlib
import sys

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
        
        # Create a unique fingerprint (hash) of the page content
        # We use the text content to detect any changes in the HTML
        page_hash = hashlib.md5(response.text.encode('utf-8')).hexdigest()
        
        # Print the hash so the automation workflow can read it
        print(page_hash)
        
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
