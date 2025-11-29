import os
import time
from paybin import PaybinClient

public_key = os.environ.get("PAYBIN_PUBLIC_KEY", "YOUR_PUBLIC_KEY")
secret_key = os.environ.get("PAYBIN_SECRET_KEY", "YOUR_SECRET_KEY")

client = PaybinClient(public_key, secret_key, sandbox=True)

def main():
    print("--- Withdrawal Flow Example ---")

    # 1. Check for withdrawable assets
    ref_id = "USER_123_REF"
    try:
        assets = client.withdraw.get_withdrawable_assets(reference_id=ref_id)
        print(f"Withdrawable Assets: {assets}")
    except Exception as e:
        print(f"Error fetching assets: {e}")
        # Proceeding for demonstration purposes

    # 2. Create Withdrawal Request
    # Note: This requires 2FA code and Email, which usually requires user interaction
    print("\nInitiating Withdrawal...")
    try:
        withdrawal = client.withdraw.create_request(
            reference_id=ref_id,
            amount=0.01,
            symbol="ETH",
            address="0x742d35Cc6634C0532925a3b8D4C9db96C4b4d8b6",
            label="Withdrawal Test",
            merchant_transaction_id=f"TX_{int(time.time())}",
            tfa_code="123456", # Mock 2FA
            email="user@example.com"
        )
        print(f"Withdrawal Request Created: {withdrawal}")
        
        # 3. Start Verification (if required)
        print("\nStarting Verification...")
        client.withdraw.start_verification(
            reference_id=ref_id,
            symbol="ETH",
            network_id=1,
            address="0x742d35Cc6634C0532925a3b8D4C9db96C4b4d8b6",
            label="Withdrawal Test"
        )
        print("Verification Started.")

        # 4. Confirm Amount (User would verify the small amount sent to their wallet)
        # In a real flow, you would ask the user for the amount they received
        print("\nConfirming Amount (Mock)...")
        # amount_received = float(input("Enter amount received: "))
        amount_received = 0.00001 # Example
        
        # Hash generation for confirmation might be needed here if SDK doesn't handle it internally yet
        # or if it's passed explicitly.
        # Assuming we have the hash from the verification start response or similar in a real scenario
        mock_hash = "mock_hash_value" 
        
        confirm = client.withdraw.confirm_amount(
            reference_id=ref_id,
            symbol="ETH",
            network_id=1,
            amount=amount_received,
            hash_value=mock_hash
        )
        print(f"Confirmation Result: {confirm}")

    except Exception as e:
        print(f"Withdrawal flow stopped: {e}")

if __name__ == "__main__":
    main()
