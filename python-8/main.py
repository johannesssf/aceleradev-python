import jwt

from jwt.exceptions import (
    InvalidSignatureError,
    DecodeError,
    InvalidTokenError,
)


DFL_ALGORITHM = 'HS256'
DFL_SECRET = 'acelera'


def create_token(data, secret, algorithm=DFL_ALGORITHM):
    """Generates a simple JWT token.

    Args:
        data (dict): Data to be inserted into the token
        secret (str): A strong secret to crypt the token
        algorithm (str, optional): Which algorithm to use
        for encryptation (defaults to DFL_ALGORITHM)

    Returns:
        jwt: Token or None if something went wrong
    """
    try:
        token = jwt.encode(data, secret, algorithm=DFL_ALGORITHM)
    except TypeError as ex:
        print(f"ERROR: {ex}")
        token = None
    return token


def verify_signature(token, secret=DFL_SECRET):
    """Verifies a JWT token signature.

    Args:
        token (jwt): Token
        secret (str, optional): Secret to validate signature (defaults
        to DFL_SECRET)

    Raises:
        ex: Exceptions raised by jwt.decode

    Returns:
        dict: Token payload or error code
    """
    try:
        payload = jwt.decode(token, secret, algorithms=DFL_ALGORITHM)
        return payload

    except (InvalidSignatureError, DecodeError):
        return {"error": 2}

    except InvalidTokenError as ex:
        print(f"ERROR: ({type(ex)}) {ex}")
        raise ex
