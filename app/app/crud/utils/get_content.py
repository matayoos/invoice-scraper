from app import scraper


def get_invoice_info(url: str) -> dict:
    url_content = scraper.get_content(url)

    grocery_store_info = scraper.get_grocery_store_info(url_content)
    invoice_info = scraper.get_invoice_info(url_content, url)
    items = scraper.get_items(url_content)

    return {
        "grocery_store": grocery_store_info,
        "invoice": invoice_info,
        "items": items,
    }
