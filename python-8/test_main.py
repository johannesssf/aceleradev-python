import pytest

from jwt.exceptions import InvalidTokenError, InvalidKeyError
from unittest.mock import patch

from main import create_token, verify_signature


class TestChallenge4:
    token = (b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsYW5ndWFnZSI6IlB5dG'
             b'hvbiJ9.sM_VQuKZe_VTlqfS3FlAm8XLFhgvQQLk2kkRTpiXq7M')

    def test_create_token(self):
        assert create_token({"language": "Python"}, "acelera") == self.token

    def test_create_token_invalid_data(self):
        assert create_token(None, 'acelera') is None
        assert create_token(123, 'acelera') is None
        assert create_token("invalid data", 'acelera') is None
        assert create_token([], 'acelera') is None

    def test_create_token_invalid_secret(self):
        assert create_token({"language": "Python"}, None) is None
        assert create_token({"language": "Python"}, 123456) is None
        assert create_token({"language": "Python"}, [1, 2, 3]) is None

    def test_verify_signature_ok(self):
        token = create_token({"language": "Python"}, "acelera")
        assert verify_signature(token) == {"language": "Python"}

    def test_verify_signature_wrong_signature(self):
        token = create_token({"language": "Python"}, "desacelera")
        assert verify_signature(token) == {"error": 2}

    def test_verify_signature_invalid_token(self):
        invalid = (b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9eyJsYW5ndWFnZSI6I'
                   b'lB5dGhvbiJ9sM_VQuKZe_VTlqfS3FlAm8XLFhgvQQLk2kkRTpiXq7M')
        assert verify_signature(invalid) == {"error": 2}

    @patch('main.jwt')
    def test_verify_signature_specific_exception(self, jwt_mock):
        jwt_mock.decode.side_effect = InvalidKeyError
        with pytest.raises(InvalidKeyError):
            verify_signature(None)

    @patch('main.jwt')
    def test_verify_signature_generic_exception(self, jwt_mock):
        jwt_mock.decode.side_effect = InvalidTokenError
        with pytest.raises(InvalidTokenError):
            verify_signature(None)
