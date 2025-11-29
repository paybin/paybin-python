from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

# Your Paybin Secret Key
SECRET_KEY = "YOUR_SECRET_KEY"

def verify_signature(data, signature):
    """
    Verify the webhook signature.
    Note: Adjust the hashing logic based on the actual webhook signature format 
    provided in the Paybin documentation for callbacks.
    """
    # Example verification logic (placeholder)
    # raw_string = ...
    # expected_signature = hashlib.md5(raw_string.encode()).hexdigest()
    # return signature == expected_signature
    return True

@app.route('/webhook/paybin', methods=['POST'])
def paybin_webhook():
    data = request.json
    signature = request.headers.get('X-Paybin-Signature') # Example header

    print(f"Received Webhook: {data}")

    if not verify_signature(data, signature):
        return jsonify({"error": "Invalid signature"}), 401

    # Process the event
    event_type = data.get('type')
    
    if event_type == 'deposit.success':
        print(f"Deposit received: {data.get('amount')} {data.get('currency')}")
        # Update user balance in your DB
    elif event_type == 'withdraw.completed':
        print(f"Withdrawal completed: {data.get('txId')}")

    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    print("Starting Webhook Server on port 5000...")
    app.run(port=5000)
