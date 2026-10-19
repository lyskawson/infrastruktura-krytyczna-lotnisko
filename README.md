# Infrastruktura krytyczna — systemy bezpieczeństwa lotniska

Zespołowy projekt akademicki w LaTeX-u: CCTV, kontrola dostępu, SSWiN i SSP (SAP) dla **fikcyjnej strefy terminalowo-technicznej „Lotniska Północ”**.

**[Otwórz PDF](output/pdf/lotnisko-polnoc.pdf)** · [Instrukcja Overleafa](docs/overleaf.md) · [Podział pracy i prezentacja](docs/praca-zespolowa.md)

![Ilustracja koncepcyjna lotniska wygenerowana przez AI](images/airport-cover.png)

Pełna wersja robocza koncepcji, z opisem technicznym, obliczeniami, zestawieniem materiałów, procedurami i źródłami. Dane uczelni i autorów należy uzupełnić w **metadata.tex**. Projekt nie jest dokumentacją wykonawczą ani opisem zabezpieczeń rzeczywistego lotniska.

## Proponowany spis treści — już zastosowany w PDF

1. Cel, zakres i założenia.
2. Strefy ochrony i wymagania.
3. Charakterystyka systemów: CCTV, KD i SSWiN, SSP/SAP.
4. Schemat ideowy i integracja.
5. Sieć transmisyjna i technologie.
6. Projekt trasowy i lokalizacja urządzeń: teren, trasy, terminal.
7. Zastosowanie ML i AI.
8. Zabezpieczenie dostawy energii: UPS, baterie DC, agregat i SZR.
9. Zestawienie materiałów podstawowych.
10. Procedury bezpieczeństwa.
11. Cyberbezpieczeństwo i ochrona danych.
12. Odbiór, utrzymanie i podział prac.
13. Źródła i podstawa opracowania.

Układ realizuje wszystkie osiem elementów wskazanych przez prowadzącego. Liczba stron wynika z treści; tygodniowy harmonogram nie jest sztucznie wpisany w dokument.

## Co jest w środku

- 24 kamery: 20 stałych i 4 PTZ, z bilansem zapisu na 7 dni.
- 12 drzwi i 2 bramy KD, 16 czytników, 8 kontrolerów dwukanałowych.
- 4 lokalne centrale SSWiN i 4 lokalne centrale SSP.
- Plan obszaru 600 × 400 m i 1520 m tras pierścienia światłowodowego.
- 6 edytowalnych rysunków wektorowych: architektura, teren, trasy, terminal, AI i zasilanie.
- Bilans mocy, pojemności dysków, UPS i baterii, tabela reakcji na incydenty oraz plan prób odbiorowych.

Wartości są założeniami dydaktycznymi. Nie deklarujemy rzeczywistych wyników AI, pomiarów, wymaganej prawem retencji ani potwierdzonej zgodności wykonawczej. W dokumencie wskazano kwestie do dalszego uzgodnienia.

## Kompilacja

Na Overleafie: główny plik **main.tex**, kompilator **pdfLaTeX**, kodowanie UTF-8. Bibliografia jest w źródłach; nie wymaga BibTeX ani Biber. Nie jest potrzebny shell escape.

Lokalnie, z TeX Live / MacTeX i latexmk:

~~~sh
make pdf
~~~

Wynik: output/pdf/lotnisko-polnoc.pdf. Rysunki PDF są dołączone do repo, więc Python/ReportLab nie jest potrzebny do samej kompilacji.

Po zmianie geometrii:

~~~sh
python3 -m pip install -r requirements-figures.txt
make figures
make pdf
~~~

Generator korzysta z Arial na macOS lub DejaVu Sans na Linuksie. Można wskazać własne fonty przez PROJECT_FONT_REGULAR i PROJECT_FONT_BOLD. Pliki fontów nie są dystrybuowane w repo.

Pakiet do ręcznego importu do Overleafa:

~~~sh
make overleaf
~~~

Wynik: output/lotnisko-overleaf.zip, z main.tex w katalogu głównym archiwum. ZIP jest pomijany przez Git, aby nie duplikować obrazów; można go wygenerować lokalnie albo pobrać z artefaktów udanej kompilacji w GitHub Actions.

## Praca przez GitHub

Każdy push i pull request uruchamia kompilację i sprawdzenie danych w GitHub Actions. Aktualny wynik jest dostępny w artefakcie **lotnisko-pdf-i-overleaf**. Automat nie aktualizuje sam pliku PDF w repo — po zmianach lokalnych uruchom make pdf i dołącz również PDF do commita.

Proponowany przepływ: mała zmiana → własna gałąź → pull request → przegląd przez drugą osobę → scalenie. [Instrukcja współpracy](docs/praca-zespolowa.md) podaje pakiety prac bez narzucania terminów tygodniowych.

**Overleaf Git i synchronizacja GitHub wymagają dostępu premium/instytucjonalnego.** Zwykły import ZIP nie wymaga tych funkcji i nie tworzy automatycznej synchronizacji. [Oficjalna dokumentacja Overleaf](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization).

## Pliki do edycji

| Plik / katalog | Co zmieniać |
|---|---|
| metadata.tex | Uczelnia, autorzy, grupa, prowadzący, data i wersja |
| main.tex | Kolejność rozdziałów |
| sections/ | Treść merytoryczna |
| preamble.tex | Kolory, typografia, marginesy i nagłówki |
| data/design.json | Geometria tras, liczby urządzeń i dane bilansu |
| tools/generate_figures.py | Edytowalne źródła sześciu rysunków |
| figures/ | Gotowe wektorowe PDF-y włączane do dokumentu |
| tools/validate_design.py | Kontrola sum, geometrii, portów, PoE i pojemności |
| docs/rejestr-urzadzen.md | Rejestr zespołów urządzeń, generowany razem z rysunkami |
| docs/ai-assets.md | Pochodzenie i pełny prompt ilustracji AI |

Zmiana JSON nie zmienia automatycznie liczb w tekście — po każdej zmianie przejrzyj właściwe rozdziały i zestawienie. Walidator kontroluje wybrane zależności liczbowe, nie zastępuje przeglądu merytorycznego.

## Przed oddaniem

- Uzupełnić stronę tytułową i przyjąć wspólnie zakres fikcyjnego obiektu.
- Zweryfikować treść, obliczenia oraz aktualność źródeł z prowadzącym.
- Rozstrzygnąć, czy prowadzący oczekuje mapy rzeczywistej lokalizacji lub konkretnych modeli urządzeń.
- Doprecyzować plan pożarowy, rzeczywiste rzuty i macierz sterowań, jeśli wymaga tego zakres zajęć.
- Skompilować PDF i przeczytać wszystkie strony po ostatnich zmianach.

Autorskie źródła udostępniono na licencji MIT; materiały zewnętrzne są wyłącznie cytowane. Obraz AI opisano oddzielnie w docs/ai-assets.md.
