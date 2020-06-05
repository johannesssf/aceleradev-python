import jwt

from jwt.exceptions import (
    InvalidSignatureError,
    DecodeError,
    InvalidTokenError,
)


TOKEN_ALGORITHM = 'HS256'


def create_token(data, secret):
    """Generates a simple JWT token.

    Args:
        data (dict): Data to be inserted into the token
        secret (str): A strong secret crypt the token

    Returns:
        jwt: Token or None
    """
    try:
        token = jwt.encode(data, secret, algorithm=TOKEN_ALGORITHM)
    except TypeError as ex:
        print(f"ERROR: {ex}")
        token = None
    return token


def verify_signature(token):
    """Verifies a JWT token signature.

    Args:
        token (jwt): Token

    Raises:
        ex: Exceptions raised by jwt.decode

    Returns:
        dict: Token payload or error code
    """
    try:
        payload = jwt.decode(token, 'acelera', algorithms=TOKEN_ALGORITHM)
        return payload

    except (InvalidSignatureError, DecodeError):
        return {"error": 2}

    except InvalidTokenError as ex:
        print(f"ERROR: ({type(ex)}) {ex}")
        raise ex
