import requests
from bs4 import BeautifulSoup
import logging
import argparse

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_parser():
    """Set up command-line argument parser."""
    parser = argparse.ArgumentParser(description="Scrape article titles from a website.")
    parser.add_argument('url', type=str, help="URL of the website to scrape")
    parser.add_argument('--max_titles', type=int, default=10, help="Maximum number of titles to scrape")
    return parser

def fetch_page(url):
    """Fetch the webpage content."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        raise

def parse_titles(html, max_titles):
    """Parse article titles from the HTML content."""
    soup = BeautifulSoup(html, 'html.parser')
    titles = []
    
    # Look for common heading tags
    for tag in ['h1', 'h2', 'h3', 'a']:
        elements = soup.find_all(tag, class_=lambda x: x and ('title' in x.lower() or 'headline' in x.lower()))
        for element in elements:
            text = element.get_text(strip=True)
            if text and len(titles) < max_titles:
                titles.append(text)
    
    return titles[:max_titles]

def save_titles(titles, output_file="titles.txt"):
    """Save titles to a file."""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for title in titles:
                f.write(f"{title}\n")
        logging.info(f"Saved {len(titles)} titles to {output_file}")
    except Exception as e:
        logging.error(f"Error saving titles: {e}")

def main():
    """Main function to scrape titles."""
    parser = setup_parser()
    args = parser.parse_args()
    
    try:
        html = fetch_page(args.url)
        titles = parse_titles(html, args.max_titles)
        if not titles:
            logging.warning("No titles found.")
            return
        
        for idx, title in enumerate(titles, 1):
            logging.info(f"Title {idx}: {title}")
        save_titles(titles)
    except Exception as e:
        logging.error(str(e))
        exit(1)

if __name__ == "__main__":
    main()
