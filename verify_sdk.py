import os
import sys
from paybin import PaybinClient, PaybinAPIError

def main():
    # Get keys from environment variables or use placeholders
    public_key = os.environ.get("PAYBIN_PUBLIC_KEY")
    secret_key = os.environ.get("PAYBIN_SECRET_KEY")

    if not public_key or not secret_key:
        print("Please set PAYBIN_PUBLIC_KEY and PAYBIN_SECRET_KEY environment variables.")
        sys.exit(1)

    print(f"Initializing Paybin Client (Sandbox)...")
    client = PaybinClient(public_key=public_key, secret_key=secret_key, sandbox=True)

    try:
        # 1. Check Balance
        print("\n--- Checking Balance ---")
        balances = client.balance.get_merchant_balances()
        print(f"Balances: {balances}")

        # 2. Create Deposit Address
        print("\n--- Creating Deposit Address ---")
        # Using random reference ID to avoid conflicts
        import uuid
        ref_id = f"REF_{uuid.uuid4().hex[:8]}"
        
        deposit_address = client.deposit.create_address(
            symbol="ETH",
            label="Test Deposit",
            reference_id=ref_id,
            callback_url="https://example.com/webhook",
            amount=0.1
        )
        print(f"Deposit Address Created: {deposit_address}")
        
        # 3. Get Deposit Address
        print("\n--- Getting Deposit Address ---")
        # Assuming we can get it back using the same details or if we had a member ID
        # The create response might not give MemberId, but let's try to just print what we got.
        
        # 4. Withdraw (Just creating a request, might fail if no balance)
        print("\n--- Creating Withdraw Request (Might fail if insufficient balance) ---")
        withdraw_ref = f"W_{uuid.uuid4().hex[:8]}"
        try:
            withdraw = client.withdraw.create_request(
                reference_id=withdraw_ref,
                amount=0.001,
                symbol="ETH",
                address="0x742d35Cc6634C0532925a3b8D4C9db96C4b4d8b6", # Example address
                label="Test Withdraw",
                merchant_transaction_id=f"TX_{uuid.uuid4().hex[:8]}",
                tfa_code="123456",
                email="test@example.com"
            )
            print(f"Withdraw Request Created: {withdraw}")
        except PaybinAPIError as e:
            print(f"Withdraw failed (expected if no balance): {e}")

    except PaybinAPIError as e:
        print(f"API Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
