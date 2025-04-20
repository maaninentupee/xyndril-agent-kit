# xyncrawl/src/scraper_basic.py

import json
from pathlib import Path
from bs4 import BeautifulSoup

# Staattinen testisivu (voit vaihtaa polun halutessasi)
HTML_PATH = Path("tests/test-page.html")
OUTPUT_PATH = Path("output/data.json")


def extract_data(html_file):
    with open(html_file, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Esimerkki: etsitään kaikki otsikot ja kappaleet
    data = {
        "headings": [h.get_text(strip=True) for h in soup.find_all("h1")],
        "paragraphs": [p.get_text(strip=True) for p in soup.find_all("p")],
    }
    return data


def save_to_json(data, output_file):
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def main():
    if not HTML_PATH.exists():
        print(f"HTML testisivua ei löytynyt: {HTML_PATH}")
        return

    data = extract_data(HTML_PATH)
    save_to_json(data, OUTPUT_PATH)
    print(f"Data tallennettu tiedostoon: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
