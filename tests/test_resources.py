import unittest
from unittest.mock import MagicMock
from paybin import PaybinClient

class TestResources(unittest.TestCase):
    def setUp(self):
        self.client = PaybinClient("pub_key", "sec_key", sandbox=True)
        self.client.request = MagicMock(return_value={"status": "success"})

    def test_balance_get(self):
        self.client.balance.get_merchant_balances()
        self.client.request.assert_called_with("POST", "/merchant/balances")

    def test_deposit_create(self):
        self.client.deposit.create_address(
            symbol="ETH",
            label="Test",
            reference_id="REF1",
            callback_url="http://url",
            amount=1.0
        )
        # Verify request called with correct endpoint and payload containing Hash
        args, kwargs = self.client.request.call_args
        self.assertEqual(args[0], "POST")
        self.assertEqual(args[1], "/deposit/address/create")
        self.assertIn("Hash", args[2])

    def test_withdraw_create(self):
        self.client.withdraw.create_request(
            reference_id="REF2",
            amount=0.1,
            symbol="ETH",
            address="0x123",
            label="Withdraw",
            merchant_transaction_id="TX1",
            tfa_code="000",
            email="test@test.com"
        )
        args, kwargs = self.client.request.call_args
        self.assertEqual(args[0], "POST")
        self.assertEqual(args[1], "/withdraw/add")
        self.assertIn("Hash", args[2])

if __name__ == '__main__':
    unittest.main()
