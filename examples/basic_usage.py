import os
from paybin import PaybinClient

# Initialize the client
# In a real application, use environment variables for keys
public_key = os.environ.get("PAYBIN_PUBLIC_KEY", "YOUR_PUBLIC_KEY")
secret_key = os.environ.get("PAYBIN_SECRET_KEY", "YOUR_SECRET_KEY")

client = PaybinClient(
    public_key=public_key,
    secret_key=secret_key,
    sandbox=True
)

def main():
    print("--- Basic Usage Example ---")
    
    # 1. Check Balance
    try:
        balances = client.balance.get_merchant_balances()
        print("Merchant Balances:")
        for currency, amount in balances.items():
            print(f"  {currency}: {amount}")
    except Exception as e:
        print(f"Error fetching balance: {e}")

    # 2. Create a Deposit Address
    try:
        address_info = client.deposit.create_address(
            symbol="ETH",
            label="Example Order",
            reference_id="ORDER_001",
            callback_url="https://example.com/webhook",
            amount=0.05
        )
        print("\nCreated Deposit Address:")
        print(f"  Address: {address_info.get('wallet')}")
        print(f"  Symbol: {address_info.get('symbol')}")
    except Exception as e:
        print(f"Error creating address: {e}")

if __name__ == "__main__":
    main()
