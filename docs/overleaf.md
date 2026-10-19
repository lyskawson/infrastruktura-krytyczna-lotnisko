# Overleaf — dwa sposoby pracy

Główny plik: **main.tex**. Kompilator: **pdfLaTeX**. Projekt działa z typowym TeX Live, bez zewnętrznych programów do rysunków i bez shell escape.

## A. Import repozytorium z GitHuba

Wymaga funkcji GitHub Synchronization premium lub uprawnienia instytucjonalnego.

1. Połącz konto GitHub z kontem Overleaf w ustawieniach konta.
2. W Overleaf wybierz **New Project → Import from GitHub**.
3. Wybierz repozytorium **infrastruktura-krytyczna-lotnisko**.
4. Ustaw main.tex jako główny plik i pdfLaTeX jako kompilator.
5. Kompiluj i udostępnij projekt członkom zespołu zgodnie z limitami swojego planu.

Synchronizacja nie jest samoczynnym współdzieleniem plików w czasie rzeczywistym między GitHubem i Overleafem. W menu synchronizacji pobieraj zmiany z GitHub i wysyłaj zatwierdzone zmiany z Overleafa. Przed zmianą narzędzia zsynchronizuj projekt, żeby ograniczyć konflikty.

Według dokumentacji Overleaf można utworzyć nowy projekt z istniejącego repo albo nowe repo z projektu; nie łączy się wprost dwóch już istniejących i niezależnych projektów.

## B. Import ZIP

Ten wariant nie wymaga funkcji synchronizacji Git.

1. Pobierz lotnisko-overleaf.zip przygotowany przez make overleaf albo z artefaktów kompilacji na GitHubie.
2. W Overleaf wybierz **New Project → Upload Project** i wskaż ZIP.
3. Sprawdź main.tex i pdfLaTeX.
4. Edytuj metadata.tex, a potem pliki w sections/.

Zmiany wykonane w tym wariancie nie trafiają automatycznie na GitHub. Wyeksportuj źródła z Overleafa i uzgodnij ich włączenie do repo; unikaj równoległego edytowania tych samych rozdziałów w dwóch miejscach.

## Bezpośredni Git Overleafa

To odrębna funkcja premium. Po utworzeniu projektu Overleaf udostępnia własny adres zdalnego repozytorium i uwierzytelnianie tokenem. Można dodać go jako drugi remote lokalnego repo, używając dokładnego adresu podanego przez Overleaf. Sam publiczny GitHub nie włącza tej funkcji.

Sprawdzono 19.10.2026:

- [Git integration and GitHub synchronization](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization)
- [GitHub synchronization](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/github-synchronization)
- [Git integration](https://www.overleaf.com/learn/how-to/Git_integration)
