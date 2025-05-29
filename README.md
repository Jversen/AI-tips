# Veckans AI-tips

# Statisk webbplats med veckovisa AI-tips för jobb eller privat bruk.

## Struktur
- `index.html`: Startsida som listar inlägg.
- `posts/`: Enskilda inlägg.
- `css/styles.css`: Enkel styling.
- `js/script.js`: Eventuella skript.

## Publicering
# Använd GitHub Pages för att hosta sidan. Ett workflow finns under `.github/workflows/deploy.yml`.

## Lokal utveckling
 - Klona repot: `git clone <URL>`
 - Öppna `index.html` i din webbläsare.

## Automatiskt generera inlägg

Varje fredag kl. 09:00 UTC körs ett GitHub Actions workflow (`.github/workflows/new_post.yml`) som:

- Använder `scripts/generate_post.py` för att skapa en ny post baserat på `posts/post_template.html`
- Namnger filen med dagens datum och ett löpnummer
- Lägger till placeholder-titel och innehåll

A fullständig lista på planerade publiceringsdatum finns i [schedule.md](schedule.md).