"""
Moduł zarządzający zadaniami.
Zawiera klasy Zadanie, ZadaniePriorytetowe, ZadanieRegularne oraz ManagerZadan.
"""

import time
from datetime import datetime


def czas_wykonania(funkcja):
    """Dekorator mierzący czas wykonania funkcji."""
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        end = time.time()
        print(f"Funkcja {funkcja.__name__} wykonała się w {end - start:.4f} sekundy.")
        return wynik
    return wrapper

class Zadanie:
    """
    Klasa reprezentująca podstawowe zadanie.
    :param tytul: Tytuł zadania.
    :param opis: Opis zadania.
    :param termin_wykonania: Termin wykonania zadania w formacie 'YYYY-MM-DD'.
    """
    def __init__(self, tytul, opis, termin_wykonania, **kwargs):
        self.tytul = tytul
        self.opis = opis
        self.termin_wykonania = datetime.strptime(termin_wykonania, "%Y-%m-%d")
        self.wykonane = kwargs.get("wykonane", False)  # Domyślnie False
    
    def oznacz_jako_wykonane(self):
        """Oznacza zadanie jako wykonane."""
        self.wykonane = True
    
    def __str__(self):
        """Zwraca tekstową reprezentację zadania."""
        status = "✔" if self.wykonane else "✘"
        return f"[{status}] {self.tytul} - {self.opis} (Termin: {self.termin_wykonania.date()})"

class ZadaniePriorytetowe(Zadanie):
    """Zadanie z dodatkowym atrybutem priorytetu."""
    def __init__(self, tytul, opis, termin_wykonania, priorytet, **kwargs):
        super().__init__(tytul, opis, termin_wykonania, **kwargs)
        self.priorytet = priorytet
    
    def __str__(self):
        return super().__str__() + f" [Priorytet: {self.priorytet}]"

class ZadanieRegularne(Zadanie):
    """Zadanie, które powtarza się cyklicznie."""
    def __init__(self, tytul, opis, termin_wykonania, powtarzalnosc, **kwargs):
        super().__init__(tytul, opis, termin_wykonania, **kwargs)
        self.powtarzalnosc = powtarzalnosc
    
    def __str__(self):
        return super().__str__() + f" [Powtarzalność: {self.powtarzalnosc}]"

class ManagerZadan:
    """Klasa do zarządzania listą zadań."""
    def __init__(self):
        """Inicjalizuje pustą listę zadań."""
        self.zadania = []
    
    @czas_wykonania
    def dodaj_zadanie(self, zadanie):
        """
        Dodaje zadanie do listy.
        :param zadanie: Obiekt klasy Zadanie do dodania.
        """
        self.zadania.append(zadanie)
    
    @czas_wykonania
    def usun_zadanie(self, tytul):
        """Usuwa zadanie na podstawie tytułu."""
        self.zadania = [zadanie for zadanie in self.zadania if zadanie.tytul != tytul]
    
    def oznacz_jako_wykonane(self, tytul):
        """Oznacza zadanie jako wykonane."""
        for zadanie in self.zadania:
            if zadanie.tytul == tytul:
                zadanie.oznacz_jako_wykonane()
    
    def edytuj_zadanie(self, tytul, nowy_tytul=None, nowy_opis=None, nowy_termin=None):
        """Edytuje zadanie (można podać tylko wybrane zmiany)."""
        for zadanie in self.zadania:
            if zadanie.tytul == tytul:
                zadanie.tytul = nowy_tytul or zadanie.tytul
                zadanie.opis = nowy_opis or zadanie.opis
                if nowy_termin:
                    zadanie.termin_wykonania = datetime.strptime(nowy_termin, "%Y-%m-%d")
    
    def __contains__(self, tytul):
        return any(zadanie.tytul == tytul for zadanie in self.zadania)

    def wyswietl_zadania(self):
        """Wyświetla listę zadań, posortowaną po terminie wykonania."""
        for zadanie in sorted(self.zadania, key=lambda x: x.termin_wykonania):
            print(zadanie)

    def zapisz_do_pliku(self, nazwa_pliku="zadania.txt"):
        """Zapisuje zadania do pliku tekstowego."""
        with open(nazwa_pliku, "w", encoding="utf-8") as plik:
            for zadanie in self.zadania:
                plik.write(str(zadanie) + "\n")
    
    def wczytaj_z_pliku(self, nazwa_pliku="zadania.txt"):
        """Wczytuje zadania z pliku tekstowego."""
        try:
            with open(nazwa_pliku, "r", encoding="utf-8") as plik:
                for linia in plik:
                    print(linia.strip()) 
        except FileNotFoundError:
            print("Plik nie istnieje.")
