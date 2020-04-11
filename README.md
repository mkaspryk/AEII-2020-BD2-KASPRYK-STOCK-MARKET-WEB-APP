# Stock Masters
### Symulator gry na giełdzie.

Program umożliwia inwestowanie wirtualnych pieniędzy i analizowanie zysków/strat w oparciu o faktyczne kursy giełdowe.
W programie będą zdefiniowane dwa typy graczy: osoba fizyczna i osoba prawna. Dodatkowym aktorem systemu będzie administrator.

Finansowanie gry będzie oparte o system pay-to-win, im więcej fizycznych pieniędzy zapłacisz producentom, tym wyżej jesteś w rankingu.

Użytkownik rozpoczyna z zerowym poziomem i może zdobywać doświadczenie za udane transakcje giełdowe.

Uruchomienie na Linux OS
------------------

1. Upewnij się, że Python 3 jest zainstalowany na Twoim komputerze
2. Pobierz projekt: `git clone https://github.com/mkaspryk/AEII-2020-BD2-KASPRYK-STOCK-MARKET-WEB-APP.git`
3. Uruchom skrypt, który znajdziesz w głównym folderze: `./installserver_linux.sh`
4. Aby włączyć serwer, użyj komendy `./runserver_linux.sh`
5. Wejdź na http://localhost:8000

Uruchomienie na Windows OS
------------------
UWAGA! Zainstalowanie Dockera, koniecznego do uruchomienia serwera, możliwe jest tylko na wersjach Enterprise i Professional Windowsa 10.

0. Zainstaluj Docker Desktop for Windows: https://hub.docker.com/editions/community/docker-ce-desktop-windows/
1. Upewnij się, że Python 3 jest zainstalowany (i dodany do PATH) na Twoim komputerze
2. Pobierz projekt: `git clone https://github.com/mkaspryk/AEII-2020-BD2-KASPRYK-STOCK-MARKET-WEB-APP.git`
3. Uruchom PowerShella jako administrator (!) i wprowadź komendę `set-executionpolicy unrestricted`, umożliwiającą wykonywanie skryptów
4. Przejdź do głównego folderu projektu i uruchom skrypt `.\installserver_windows.ps1`
5. Aktywuj wirtualne środowisko (`.\.venv\Scripts\activate`) i wykonaj polecenie: `docker pull redis:4; docker run -p 6379:6379 -d redis`
6. Odpal serwer komendą `.\runserver_windows.ps1`
7. Wejdź na http://localhost:8000

Zarządzanie bazą danych pgAdmin 4 dla Windows OS
-----------------

1. Instalacja pgAdmin4 https://www.pgadmin.org/download/pgadmin-4-windows/
2. Uruchomienie pgAdmin4
3. Prawym klawiszem klikamy na nazwę Servers następnie Create -> Server..
4. Pojawi się panel (nazwa serwera jest obojętna)
5. W panelu Create-Server należy przejść do Connection i uzupełnić następujące pola:
   - Host name/address: serwer1990534.home.pl
   - Port: 5432
   - Maintenance database: 31177086_stock_web_app
   - Username: 31177086_stock_web_app
   - Password: mKMlNg__ag
6. Save (powinno się utworzyć połączenie)
7. Po lewej stronie powinna znajdować się ikonka z nowym serwerem
