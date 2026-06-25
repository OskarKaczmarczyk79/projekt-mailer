# Przykłady użycia `mailer.subscribers`

## 1. Dodawanie subskrybentów

```python
from mailer.subscribers import SubscriberManager

manager = SubscriberManager()
manager.add_subscriber("user@example.com", "User")
manager.add_subscriber("kontakt@firma.pl")
```

## 2. Listowanie subskrybentów

```python
for subscriber in manager.list_subscribers():
    print(subscriber["email"], subscriber["name"])
```

## 3. Usuwanie subskrybenta

```python
success = manager.remove_subscriber("user@example.com")
if success:
    print("Subskrybent usunięty")
else:
    print("Nie znaleziono subskrybenta")
```

## 4. Pobieranie pojedynczego subskrybenta

```python
subscriber = manager.get_subscriber("kontakt@firma.pl")
if subscriber:
    print(subscriber)
```

## 5. Obsługa błędów przy niepoprawnym emailu

```python
try:
    manager.add_subscriber("zly-adres")
except ValueError as error:
    print(f"Błąd: {error}")
```
