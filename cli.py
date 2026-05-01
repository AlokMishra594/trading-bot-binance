import argparse
import logging

from client import get_client
from orders import place_order
from validators import validate_input
from logging_config import setup_logger

def main():
    setup_logger()

    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    args = parser.parse_args()

    try:
        validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

        client = get_client()

        logging.info(f"Placing order: {vars(args)}")

        response = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        if "error" in response:
            print("❌ Order Failed:", response["error"])
            logging.error(response["error"])
        else:
            print("\n✅ Order Success!")
            print("Order ID:", response.get("orderId"))
            print("Status:", response.get("status"))
            print("Executed Qty:", response.get("executedQty"))
            print("Avg Price:", response.get("avgPrice"))

            logging.info(response)

    except Exception as e:
        print("❌ Error:", str(e))
        logging.error(str(e))

if __name__ == "__main__":
    main()