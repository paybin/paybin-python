import requests
from typing import Optional, Dict, Any
from .exceptions import PaybinAPIError, PaybinAuthError
from .resources.balance import BalanceResource
from .resources.deposit import DepositResource
from .resources.withdraw import WithdrawResource

class PaybinClient:
    SANDBOX_URL = "https://sandbox.paybin.io/v1"
    PRODUCTION_URL = "https://gateway.paybin.io/v1"

    def __init__(self, public_key: str, secret_key: str, sandbox: bool = False):
        self.public_key = public_key
        self.secret_key = secret_key
        self.base_url = self.SANDBOX_URL if sandbox else self.PRODUCTION_URL
        self.session = requests.Session()
        self.session.headers.update({
            "X-Api-Key": self.secret_key,
            "Content-Type": "application/json",
            "User-Agent": "Paybin-Python-SDK/0.1.0"
        })

        # Initialize resources
        self.balance = BalanceResource(self)
        self.deposit = DepositResource(self)
        self.withdraw = WithdrawResource(self)

    def request(self, method: str, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}{endpoint}"
        
        # Always include PublicKey in data if not present, as most endpoints require it
        if data is None:
            data = {}
        if "PublicKey" not in data:
            data["PublicKey"] = self.public_key

        try:
            response = self.session.request(method, url, json=data)
            response.raise_for_status()
            result = response.json()
            
            if result.get("code") != 200:
                raise PaybinAPIError(
                    message=result.get("message", "Unknown API error"),
                    code=result.get("code"),
                    data=result.get("data")
                )
                
            return result.get("data")
            
        except requests.exceptions.RequestException as e:
            raise PaybinAPIError(f"Request failed: {str(e)}")
