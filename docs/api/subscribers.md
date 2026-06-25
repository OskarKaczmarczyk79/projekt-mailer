# API: `mailer.subscribers`

## Przegląd
Moduł `mailer.subscribers` udostępnia klasę `SubscriberManager` do zarządzania subskrybentami emailowymi. Obsługuje dodawanie, usuwanie, listowanie i pobieranie subskrybentów oraz zapobiega dodawaniu duplikatów.

## Klasy

### `SubscriberManager`

`SubscriberManager()`

Zarządza listą subskrybentów.

#### Metody

- `add_subscriber(email: str, name: Optional[str] = None) -> bool`
  - Dodaje nowego subskrybenta.
  - Zwraca `True`, jeśli subskrybent został dodany.
  - Zwraca `False`, jeśli adres email już istnieje.
  - Podnosi `ValueError` dla niepoprawnych adresów email.

- `remove_subscriber(email: str) -> bool`
  - Usuwa subskrybenta o podanym adresie.
  - Zwraca `True`, jeśli subskrybent został usunięty.
  - Zwraca `False`, jeśli adres nie istnieje.

- `list_subscribers() -> List[Dict[str, Optional[str]]]`
  - Zwraca listę subskrybentów.
  - Każdy element to słownik z kluczami `email` i `name`.

- `get_subscriber(email: str) -> Optional[Dict[str, Optional[str]]]`
  - Zwraca dane subskrybenta lub `None` jeśli nie znaleziono adresu.

## Przykładowe użycie

```python
from mailer.subscribers import SubscriberManager

manager = SubscriberManager()
manager.add_subscriber("user@example.com", "Jan Kowalski")
manager.add_subscriber("newsletter@domain.pl")
print(manager.list_subscribers())
```

### Uwagi
- `SubscriberManager` normalizuje adresy email do małych liter.
- Walidacja adresu email jest realizowana przez moduł `validators.email_validator`.
- Metoda `add_subscriber` zapobiega dodaniu duplikatów przez sprawdzenie już istniejących adresów.
