import pytest
from validators.email_validator import EmailValidator


class TestEmailValidator:

    @pytest.mark.parametrize(
        "email,expected",
        [
            ("user@example.com", True),
            ("user+tag@domain.co.uk", True),
            ("invalid@", False),
            ("@domain.com", False),
            ("user", False),
            ("", False),
            (None, False),
            (" user@example.com ", True),
        ],
    )
    def test_email_validation(self, email, expected):
        assert EmailValidator.validate(email) == expected
