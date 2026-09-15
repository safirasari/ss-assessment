# Task: String Formatting
# Goal: Transform a raw SKU into a readable title.

def format_sku(sku_string):
    """
    Instructions: Convert 'engine-oil-10w30' to 'Engine Oil 10w30'.
    """
    # TODO: Implement logic

    return sku_string.replace("-", " ").title()

    pass

print(format_sku("brake-pads-ceramic"))
# Test: format_sku("brake-pads-ceramic") -> "Brake Pads Ceramic"