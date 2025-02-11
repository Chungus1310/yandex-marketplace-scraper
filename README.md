# Yandex Marketplace Scraper 🛍️

A friendly Python script that helps you fetch product information from Yandex Market search results! This scraper gets the top 18 non-sponsored products for any search query and saves them in a neat JSON file.

## Features ✨

- Scrapes top 18 non-sponsored products from Yandex Market search results
- Extracts detailed product information:
  - Product title
  - Current price
  - Old price (if discounted)
  - Discount percentage (if available)
  - Rating value
  - Number of ratings
  - Delivery information
  - Product image URL
  - Product page URL
- Uses random delays and realistic headers to be gentle with Yandex's servers
- Handles various error scenarios gracefully
- Saves results in a clean JSON format

## Requirements 📋

```
beautifulsoup4
requests
```

## Installation 🚀

1. Clone this repository:
```bash
git clone https://github.com/Chungus1310/yandex-marketplace-scraper.git
cd yandex-marketplace-scraper
```

2. Install the required packages:
```bash
pip install beautifulsoup4 requests
```

## Usage 💻

1. Run the script with your desired search query:
```bash
python yandex_scraper.py
```

2. The results will be saved in `search_results.json` with the following format:
```json
[
  {
    "title": "Product Name",
    "price_current": "₽XXX",
    "price_old": "₽XXX",
    "discount_percentage": "XX%",
    "rating_value": "X.X",
    "rating_count": "XXX",
    "delivery_info": "Delivery details",
    "product_image_url": "https://...",
    "product_url": "https://market.yandex.ru/..."
  },
  ...
]
```

## Error Handling 🛠️

The scraper includes basic error handling for:
- Network connectivity issues
- Request timeouts
- Invalid HTML content

If any errors occur, the script will return an empty JSON array and print an error message.

## Important Notes ⚠️

1. Be mindful of Yandex's terms of service and rate limits
2. The script includes random delays (1-3 seconds) between requests
3. Consider using a VPN or proxy if you encounter frequent blocks
4. The script filters out sponsored products to ensure organic search results
5. Currently supports Russian language content from Yandex Market

## Troubleshooting 🔍

If you encounter blocks or issues:
1. Try increasing the delay between requests
2. Use a VPN or proxy service
3. Ensure your headers are up to date
4. Clear your browser cookies and try accessing Yandex Market normally first

## Contributing 🤝

Feel free to open issues or submit pull requests! We appreciate any contributions to improve the scraper.

## Author 👨‍💻

Created by [Chun](https://github.com/Chungus1310)

## License 📝

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer ⚖️

This scraper is for educational purposes only. Make sure to comply with Yandex's terms of service and robots.txt when using this tool.

---

Happy scraping! Remember to use this tool responsibly and respect Yandex's servers. If you find this project helpful, consider giving it a ⭐ on GitHub!
