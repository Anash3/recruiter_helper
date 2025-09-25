from bs4 import BeautifulSoup
import requests


def scrape_job_info(url: str) -> str:
    """Fetches and extracts visible text content from a webpage."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # raises error for 4xx/5xx responses

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract visible text
        text = soup.get_text(separator="\n", strip=True)
        return text

    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return ""