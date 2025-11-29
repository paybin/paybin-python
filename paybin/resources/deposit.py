from typing import Dict, Any, Optional, TYPE_CHECKING
from ..utils import generate_hash

if TYPE_CHECKING:
    from ..client import PaybinClient

class DepositResource:
    def __init__(self, client: 'PaybinClient'):
        self.client = client

    def create_address(self, 
                       symbol: str, 
                       label: str, 
                       reference_id: str, 
                       callback_url: str, 
                       amount: float, 
                       currency: str = "USD") -> Dict[str, Any]:
        """
        Create a new deposit address.
        
        Args:
            symbol: Cryptocurrency symbol (e.g., 'ETH')
            label: Label for the address
            reference_id: Unique reference ID
            callback_url: Webhook URL for notifications
            amount: Amount to deposit
            currency: Currency for the amount (default: 'USD')
            
        Returns:
            Dictionary containing address details
        """
        # Hash generation: PublicKey + Symbol + Label + ReferenceId + CallbackUrl + secretKey
        # Note: The docs say "PublicKey + Symbol + Label + ReferenceId + CallbackUrl" then MD5(hashString + secretKey)
        # My generate_hash does MD5(data + secret)
        
        data_string = f"{self.client.public_key}{symbol}{label}{reference_id}{callback_url}"
        signature = generate_hash(data_string, self.client.secret_key)
        
        payload = {
            "Symbol": symbol,
            "Label": label,
            "ReferenceId": reference_id,
            "CallbackUrl": callback_url,
            "Amount": amount,
            "Currency": currency,
            "Hash": signature
        }
        
        return self.client.request("POST", "/deposit/address/create", payload)

    def get_address(self, 
                    member_id: str, 
                    symbol: str, 
                    label: str, 
                    network_id: int) -> Dict[str, Any]:
        """
        Get an existing deposit address.
        
        Args:
            member_id: Member ID
            symbol: Cryptocurrency symbol
            label: Label
            network_id: Network ID
            
        Returns:
            Dictionary containing address details
        """
        payload = {
            "MemberId": member_id,
            "Symbol": symbol,
            "Label": label,
            "NetworkId": network_id
        }
        
        return self.client.request("POST", "/deposit/address/get", payload)
