"""R11-17 (source) auth-core issues RS256 JWTs with its RSA private key."""
import jwt

def issue(claims: dict, private_pem: str) -> str:
    return jwt.encode(claims, private_pem, algorithm="RS256", headers={"kid": "qx-rsa-1"})
