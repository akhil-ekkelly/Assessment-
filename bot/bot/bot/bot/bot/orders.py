import logging
from .client import BinanceFuturesClient

logger = logging.getLogger(__name__)

def place_order(client: BinanceFuturesClient, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    endpoint = "/fapi/v1/order"
    
    params = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": order_type.upper(),
        "quantity": quantity
    }
    
    if order_type.upper() == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"  # Good Till Cancel is required for limit orders
        
    logger.info(f"Initiating {order_type} {side} order for {quantity} {symbol}")
    
    response = client.send_signed_request("POST", endpoint, params)
    return response
  
