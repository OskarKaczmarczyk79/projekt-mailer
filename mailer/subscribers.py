from __future__ import annotations

from typing import Dict, List, Optional

from validators.email_validator import EmailValidator


class SubscriberManager:
    """Zarządza listą subskrybentów emailowych."""

    def __init__(self) -> None:
        self._subscribers: Dict[str, Optional[str]] = {}

    def add_subscriber(self, email: str, name: Optional[str] = None) -> bool:
        """Dodaj subskrybenta, jeśli email jest prawidłowy i nie występuje na liście.

        Args:
            email: Adres email subskrybenta.
            name: Opcjonalna nazwa subskrybenta.

        Returns:
            True jeśli subskrybent został dodany, False jeśli email już istnieje.

        Raises:
            ValueError: Jeśli email jest nieprawidłowego formatu.
        """
        if not EmailValidator.validate(email):
            raise ValueError("Nieprawidłowy adres email")

        normalized_email = email.strip().lower()
        if normalized_email in self._subscribers:
            return False

        self._subscribers[normalized_email] = name.strip() if name else None
        return True

    def remove_subscriber(self, email: str) -> bool:
        """Usuń subskrybenta według adresu email.

        Args:
            email: Adres email do usunięcia.

        Returns:
            True jeśli subskrybent został usunięty, False jeśli nie znaleziono emaila.
        """
        normalized_email = email.strip().lower()
        return self._subscribers.pop(normalized_email, None) is not None

    def list_subscribers(self) -> List[Dict[str, Optional[str]]]:
        """Zwróć listę wszystkich subskrybentów.

        Returns:
            Lista słowników z kluczami `email` i `name`.
        """
        return [
            {"email": email, "name": name}
            for email, name in self._subscribers.items()
        ]

    def get_subscriber(self, email: str) -> Optional[Dict[str, Optional[str]]]:
        """Pobierz szczegóły subskrybenta po adresie email.

        Args:
            email: Adres email subskrybenta.

        Returns:
            Słownik z danymi subskrybenta lub None, jeśli nie istnieje.
        """
        normalized_email = email.strip().lower()
        if normalized_email not in self._subscribers:
            return None
        return {"email": normalized_email, "name": self._subscribers[normalized_email]}
