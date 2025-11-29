# Paybin Python SDK

Official Python SDK for the [Paybin API](https://developers.paybin.io/).

## Installation

```bash
pip install paybin-sdk
```

## Configuration

You need your Paybin Public and Secret keys. You can generate them in your [Paybin Portfolio](https://portfolio.paybin.io).

## Usage

### Initialization

```python
from paybin import PaybinClient

client = PaybinClient(
    public_key="YOUR_PUBLIC_KEY",
    secret_key="YOUR_SECRET_KEY",
    sandbox=True  # Set to False for production
)
```

### Balance

Get your merchant balances:

```python
balances = client.balance.get_merchant_balances()
print(balances)
```

### Deposit

Create a new deposit address:

```python
address = client.deposit.create_address(
    symbol="ETH",
    label="Order #123",
    reference_id="ORDER_123",
    callback_url="https://your-domain.com/webhook",
    amount=0.1
)
print(address)
```

### Withdraw

Create a withdrawal request:

```python
withdrawal = client.withdraw.create_request(
    reference_id="W_001",
    amount=0.05,
    symbol="ETH",
    address="0x...",
    label="Withdrawal",
    merchant_transaction_id="TX_001",
    tfa_code="123456",
    email="user@example.com"
)
print(withdrawal)
```

## Support

For more information, please visit the [Paybin Developer Documentation](https://developers.paybin.io/).
