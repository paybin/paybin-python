class PaybinError(Exception):
    """Base exception for Paybin SDK"""
    pass

class PaybinAPIError(PaybinError):
    """Exception raised for API errors"""
    def __init__(self, message, code=None, data=None):
        self.message = message
        self.code = code
        self.data = data
        super().__init__(f"{message} (Code: {code})")

class PaybinAuthError(PaybinError):
    """Exception raised for authentication errors"""
    pass
