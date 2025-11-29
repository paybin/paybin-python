import hashlib

def generate_hash(data_string: str, secret_key: str) -> str:
    """
    Generates MD5 hash for Paybin API signature.
    
    Args:
        data_string: The concatenated string of data fields
        secret_key: The merchant's secret key
        
    Returns:
        MD5 hash string
    """
    raw_string = f"{data_string}{secret_key}"
    return hashlib.md5(raw_string.encode('utf-8')).hexdigest()
