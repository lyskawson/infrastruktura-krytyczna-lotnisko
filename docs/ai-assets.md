# Pochodzenie ilustracji i użycie AI

## Okładka

- Plik: images/airport-cover.png.
- Narzędzie: wbudowane **ImageGen**, generowanie nowego obrazu; bez API/CLI użytkownika.
- Data: 19.10.2026.
- Obiekt całkowicie fikcyjny; brak obrazów referencyjnych.
- Ilustracja okładkowa, która nie odwzorowuje dokładnie geometrii rysunków technicznych.

Pełny prompt:

> Use case: stylized-concept. Asset type: landscape cover illustration for a Polish university engineering concept report about integrated airport security. Primary request: create a beautifully composed isometric architectural illustration of a completely fictional small regional airport campus: a modern low terminal, apron with two small passenger aircraft, one hangar, a small technical building, security gate and short access road, parking and landscaping. Show the idea of a connected campus through a few subtle teal dotted paths and small amber glowing points, without labels or technical claims. Style: premium architectural model / crisp 3D editorial illustration, refined matte materials, clean edges, gentle shadows, restrained detail suitable for print. Palette: warm white and very pale blue-grey ground, dark navy roofs, teal accents, tiny amber highlights. Composition: landscape 3:2, entire miniature campus visible, generous pale negative space around it, high three-quarter aerial view. Lighting: soft bright daytime. Constraints: imaginary site with no real airport names, no map labels, no text, no logos, no watermark, no people in close-up, no embedded diagrams. This is only an artistic cover, not a technical plan. Render at high resolution.

Nie potwierdza się wyłączności ani ochrony prawnoautorskiej obrazu wygenerowanego przez AI. Licencja MIT dotyczy praw do autorskich części repozytorium w zakresie, w jakim takie prawa przysługują autorom.

## Rysunki techniczne i tekst

Sześć schematów w figures/ jest rysowanych deterministycznie z kodu tools/generate_figures.py i danych data/design.json. Mają edytowalne źródła; podpisy nie są tekstem wygenerowanym w bitmapie.

AI wspomogła przygotowanie tekstu, obliczeń i kodu. Zespół powinien sprawdzić treść, źródła i wymagania przed oddaniem oraz dostosować opis wykorzystania AI do zasad uczelni.
