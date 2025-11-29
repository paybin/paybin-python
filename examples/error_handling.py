import os
from paybin import PaybinClient, PaybinAPIError, PaybinAuthError

public_key = os.environ.get("PAYBIN_PUBLIC_KEY", "YOUR_PUBLIC_KEY")
secret_key = os.environ.get("PAYBIN_SECRET_KEY", "YOUR_SECRET_KEY")

client = PaybinClient(public_key, secret_key, sandbox=True)

def main():
    print("--- Error Handling Example ---")

    # Example 1: Invalid Request (e.g., missing required fields or invalid data)
    try:
        # Intentionally passing invalid data
        client.deposit.create_address(
            symbol="INVALID_SYMBOL", 
            label="Test",
            reference_id="REF_ERR",
            callback_url="http://bad-url",
            amount=-1
        )
    except PaybinAPIError as e:
        print(f"\nCaught API Error:")
        print(f"  Message: {e.message}")
        print(f"  Code: {e.code}")
        print(f"  Data: {e.data}")
    except Exception as e:
        print(f"Caught unexpected error: {e}")

    # Example 2: Authentication Error (using wrong keys)
    bad_client = PaybinClient("wrong", "wrong", sandbox=True)
    try:
        bad_client.balance.get_merchant_balances()
    except PaybinAPIError as e:
        # The API might return 401/403 as a PaybinAPIError with a specific code
        print(f"\nCaught Auth/API Error with bad keys:")
        print(f"  Message: {e.message}")
    except Exception as e:
        print(f"Caught unexpected error: {e}")

if __name__ == "__main__":
    main()
