# Email Templates Skill

## Cel Umiejętności
Ten skill pomaga w tworzeniu ustandaryzowanych szablonów wiadomości email (HTML oraz plain text) dla projektu Mailer. Skupia się na ponownym wykorzystaniu kodu poprzez dziedziczenie szablonów oraz bezpiecznym wstrzykiwaniu zmiennych.

## Główne Koncepcje i Wymagania

### 1. Template Inheritance (Dziedziczenie)
Wszystkie szablony HTML muszą dziedziczyć z głównego pliku bazowego `base.html`. Dzięki temu utrzymujemy spójny nagłówek, stopkę i style CSS w każdej wiadomości. Nie powielamy kodu strukturalnego.

### 2. Variable Substitution (Zmienne)
Do renderowania szablonów wykorzystujemy system Jinja2 (domyślny we Flasku). Zmienne muszą być poprawnie formatowane. Zawsze należy dbać o unikanie wstrzykiwania szkodliwego kodu HTML przez użytkownika (XSS) – korzystamy z domyślnego mechanizmu autoescape.

### 3. HTML i Plain Text
Każdy email wysyłany do klienta powinien zawierać dwie wersje: rozbudowaną wersję HTML (dla nowoczesnych klientów poczty) oraz wersję Plain Text jako fallback (zapasową).

## Przykładowe Szablony (Examples)

### A. Newsletter (HTML)
\`\`\`html
{% extends "base.html" %}
{% block content %}
<h2>Witaj {{ subscriber_name }},</h2>
<p>Oto najnowsze wiadomości z tego tygodnia:</p>
<div class="newsletter-body">
    {{ newsletter_content | safe }}
</div>
<p><a href="{{ unsubscribe_link }}">Wypisz się</a></p>
{% endblock %}
\`\`\`

### B. Potwierdzenie rejestracji (Plain Text)
\`\`\`text
Witaj {{ subscriber_name }},

Dziękujemy za rejestrację w naszym systemie!
Aby potwierdzić konto, wejdź na poniższy link:
{{ confirmation_link }}

Pozdrawiamy,
Zespół Mailera
\`\`\`

## Wskazówki do testowania (Template Testing)
Podczas pisania testów dla szablonów nie musimy za każdym razem podnosić całego serwera pocztowego. Powinniśmy skupić się na renderowaniu szablonu lokalnie we Flasku przy użyciu `render_template_string` lub testowego klienta, a następnie sprawdzać, czy:
1. Zmienne (np. `subscriber_name`) zostały poprawnie podstawione w tekście.
2. Linki (szczególnie wypisu i potwierdzenia) nie są puste i mają odpowiedni format.
3. Znaki specjalne w treści wiadomości nie niszczą struktury HTML.

Zawsze generuj testy pokrywające wariant z brakującymi zmiennymi, aby zweryfikować zachowanie aplikacji.