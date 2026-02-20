from bot.client import get_client

def place_order(symbol, side, order_type, quantity, price=None, reduce_only=False):
    client = get_client()

    params = {
        "symbol": symbol,
        "side": side.upper(),
        "type": order_type.upper(),
        "quantity": quantity,
        "reduceOnly": reduce_only
    }

    # Only add price if LIMIT order
    if order_type.upper() == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT order")
        params["price"] = price
        params["timeInForce"] = "GTC"

    order = client.futures_create_order(**params)
    return order