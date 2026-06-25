import re
from typing import ClassVar


class EmailValidator:
    """Prosty walidator formatu adresu email."""

    PATTERN: ClassVar[str] = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    @staticmethod
    def validate(email: str) -> bool:
        """Waliduj format emaila bez wysyłania wiadomości."""
        if not email or not isinstance(email, str):
            return False
        return bool(re.match(EmailValidator.PATTERN, email.strip()))
