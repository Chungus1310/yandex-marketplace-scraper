from bs4 import BeautifulSoup
import json
import requests
from urllib.parse import quote
import time
import random

def get_html_content(search_query):
    """
    Fetches HTML content from Yandex Market search.
    """
    # Encode the search query and create the URL
    encoded_query = quote(search_query)
    url = f"https://market.yandex.ru/search?text={encoded_query}"
    
    # Headers to mimic a real browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    
    try:
        # Add random delay to avoid rate limiting
        time.sleep(random.uniform(1, 3))
        
        # Make the request
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
        
    except requests.RequestException as e:
        print(f"Error fetching search results: {e}")
        return None

def scrape_yandex_market_items(search_query):
    """
    Scrapes top items data from Yandex Market search results.

    Args:
        search_query (str): Search query for Yandex Market.

    Returns:
        str: JSON string containing scraped item data.
    """
    # Get HTML content
    html_content = get_html_content(search_query)
    if not html_content:
        return json.dumps([], indent=4, ensure_ascii=False)

    soup = BeautifulSoup(html_content, 'html.parser')
    items_data = []
    item_count = 0

    # Select all article elements that are not sponsored (searchOrganic)
    item_containers = soup.select('section._3BHKe article[data-auto="searchOrganic"]')

    for container in item_containers:
        if item_count >= 18:
            break

        item = {}

        title_element = container.select_one('span[data-auto="snippet-title"]')
        item['title'] = title_element.text.strip() if title_element else 'N/A'

        # Extract product URL
        url_element = container.select_one('div._1ENFO a[data-auto="snippet-link"]')
        item['product_url'] = 'https://market.yandex.ru' + url_element['href'] if url_element else 'N/A'

        # Extract product image URL
        image_element = container.select_one('div._1OjQK img.w7Bf7')
        item['product_image_url'] = image_element['src'] if image_element else 'N/A'


        discount_badge = container.select_one('div[data-auto="discount-badge"] span.ds-badge__textContent span:first-child')
        item['discount_percentage'] = discount_badge.text.strip() if discount_badge else None

        price_current_element = container.select_one('span[data-auto="snippet-price-current"] span.ds-text_headline-5_bold')
        item['price_current'] = price_current_element.text.strip() if price_current_element else 'N/A'

        price_old_element = container.select_one('span[data-auto="snippet-price-old"] span.ds-text')
        item['price_old'] = price_old_element.text.strip() if price_old_element else 'N/A'

        rating_value_element = container.select_one('span._1kXge span[aria-hidden="true"].ds-text_weight_med')
        item['rating_value'] = rating_value_element.text.strip() if rating_value_element else None

        rating_count_element = container.select_one('span._1kXge span[aria-hidden="true"].ds-text_lineClamp_1')
        item['rating_count'] = rating_count_element.text.strip().replace(' оценки', '').replace(' оценка', '') if rating_count_element else None

        delivery_element = container.select_one('div[data-auto="delivery-wrapper"] span._1yLiV')
        delivery_type_element = container.select_one('div[data-auto="delivery-wrapper"] span._1U2DA._2Lt3J')
        delivery_type_extra_element = container.select_one('div[data-auto="delivery-wrapper"] span._1U2DA.DhcCT')

        delivery_text = delivery_element.text.strip() if delivery_element else 'N/A'
        delivery_type = delivery_type_element.text.strip() if delivery_type_element else ''
        delivery_type_extra = delivery_type_extra_element.text.strip() if delivery_type_extra_element else ''

        item['delivery_info'] = f"{delivery_text}, {delivery_type} {delivery_type_extra}".strip().rstrip(',')

        items_data.append(item)
        item_count += 1

    return json.dumps(items_data, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    search_query = "lavender nail polish"
    json_output = scrape_yandex_market_items(search_query)
    
    # Save results to a file
    with open('search_results.json', 'w', encoding='utf-8') as f:
        f.write(json_output)
    
    print("Results have been saved to search_results.json")