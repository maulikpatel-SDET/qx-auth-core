"""R11-17 auth-core publishes its public key as JWKS (alg RS256)."""
import json
def jwks(n_b64url: str, e_b64url: str) -> str:
    return json.dumps({"keys": [{"kty": "RSA", "alg": "RS256", "use": "sig",
                                 "kid": "qx-rsa-1", "n": n_b64url, "e": e_b64url}]})
