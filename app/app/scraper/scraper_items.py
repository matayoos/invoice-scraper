import pandas as pd

from app.scraper.base import items_value_to_float

ITEMS_INDEX = 3

KEYS_INDEX = 0
CONTENT_INDEX = 0


def get_items(iframe_content) -> list:
    items = iframe_content.findAll("table", "NFCCabecalho")[ITEMS_INDEX]

    # Get first tables
    items_df = pd.read_html(str(items))[CONTENT_INDEX]
    items_df.columns = ["item_id", "description", "qty", "unit", "value", "final_value"]

    items_list = items_df.to_dict("records")
    del items_list[KEYS_INDEX]

    return items_value_to_float(items_list)
