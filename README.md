# stock-market-web-app
Symulator gry na giełdzie.

Program umożliwia inwestowanie wirtualnych pieniędzy i analizowanie zysków/strat w oparciu o faktyczne kursy giełdowe.
W programie będą zdefiniowane dwa typy graczy: osoba fizyczna i osoba prawna. Dodatkowym aktorem systemu będzie administrator.

Finansowanie gry będzie oparte o system pay-to-win, im więcej fizycznych pieniędzy zapłacisz producentom, tym wyżej jesteś w rankingu.

Użytkownik rozpoczyna z zerowym poziomem i może zdobywać doświadczenie za udane transakcje giełdowe.

Instrukcja uruchomienia projektu dla Windows OS
------------------

1. Sklonowanie projektu na komputer lokalny
2. Instalacja Python 3.8 (minimum 3), dodanie Pythona do PATH
2. Uruchomienie power shell bądź np. git bash w folderze z rozwiązaniem
3. Sprawdzenie czy są zainstalowane odpowiednie paczki "pip freeze" ostatnie wy listowane powinno być virtualenv (wersja sprawdzona to 20.0.5)
4. Utworzenie wirtualnego środowiska poprzez "pip -m venv venv" ostatni parametr określa nazwę wirtualnego środowiska
5. Uruchomienie wirtualnego środowiska "source venv/Scripts/activate"
6. Instalacja frameworku Django "pip install Django"
7. Instalacja postgresql "pip install psycopg2"
8. Instalacja pakietu do api "pip install requests"
9. Instalacja pakietu do wykresów webowych "pip install django_plotly_dash"
10. Instalacja pakietu do uaktualniania wykresów w trybie live "pip install channels daphne redis django-redis channels-redis"
11. Instalacja Docker desktop dla Windows. Po instalacja program Docker automatycznie dodaje sie do patha naszego systemu.
12. Na aktywowanym wirtualnym środowisku z python uruchomić polecenia Docker:
 - docker pull redis:4
 - docker run -p 6379:6379 -d redis
13. W folderze stock znajduje się plik manage.py(zawiera całą konfigurację) jest potrzebny do uruchomienia serwera.
14. Za pomocą pliku manage.py można dokonać migracji bazy danych i dodatkowych aplikacji z projektu "python ./manage.py migrate"
15. Uruchomienie serwera "python manage.py runserver"
16. Podgląd strony po linkiem "http://localhost:8000/"

Zarządzanie bazą danych pgAdmin 4 dla Windows OS
-----------------

1. Instalacja pgAdmin4 https://www.pgadmin.org/download/pgadmin-4-windows/
2. Uruchomienie pgAdmin4
3. Prawym klawiszem klikamy na nazwę Servers następnie Create -> Server..
4. Pojawi się panel (nazwa serwera jest obojętna)
5. W panelu Create-Server należy przejść do Connection

Należy uzupełnić następujące pola:
 - Host name/address: serwer1990534.home.pl
 - Port: 5432
 - Maintenance database: 31177086_stock_web_app
 - Username: 31177086_stock_web_app
 - Password: mKMlNg__ag
6. Save (powinno się utworzyć połączenie)
7. Po lewej stronie powinna znajdować się ikonka z nowym serwerem

