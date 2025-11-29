from typing import Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import PaybinClient

class BalanceResource:
    def __init__(self, client: 'PaybinClient'):
        self.client = client

    def get_merchant_balances(self) -> Dict[str, float]:
        """
        Get merchant balances for all supported currencies.
        
        Returns:
            Dictionary containing balances (e.g., {'btcBalance': 0.1, ...})
        """
        return self.client.request("POST", "/merchant/balances")
