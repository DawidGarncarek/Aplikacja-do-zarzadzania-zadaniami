from zadanie import ManagerZadan, Zadanie, ZadaniePriorytetowe, ZadanieRegularne

def main():
    manager = ManagerZadan()
    
    while True:
        print("\n--- Menedżer Zadań ---")
        print("1. Dodaj zadanie")
        print("2. Usuń zadanie")
        print("3. Oznacz jako wykonane")
        print("4. Edytuj zadanie")
        print("5. Wyświetl zadania")
        print("6. Zapisz do pliku")
        print("7. Wczytaj z pliku")
        print("8. Wyjście")


        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            tytul = input("Tytuł: ")
            opis = input("Opis: ")
            termin = input("Termin (YYYY-MM-DD): ")
            typ = input("Typ (1 - Regularne, 2 - Priorytetowe): ")

            if typ == "1":
                powtarzalnosc = input("Powtarzalność (np. codziennie, co tydzień): ")
                zadanie = ZadanieRegularne(tytul, opis, termin, powtarzalnosc)
            elif typ == "2":
                priorytet = input("Priorytet (1-5): ")
                zadanie = ZadaniePriorytetowe(tytul, opis, termin, int(priorytet))
            else:
                zadanie = Zadanie(tytul, opis, termin)

            manager.dodaj_zadanie(zadanie)

        elif wybor == "2":
            tytul = input("Tytuł zadania do usunięcia: ")
            manager.usun_zadanie(tytul)

        elif wybor == "3":
            tytul = input("Tytuł zadania do oznaczenia jako wykonane: ")
            manager.oznacz_jako_wykonane(tytul)

        elif wybor == "4":
            tytul = input("Tytuł zadania do edycji: ")
            nowy_tytul = input("Nowy tytuł: ")
            nowy_opis = input("Nowy opis: ")
            nowy_termin = input("Nowy termin (YYYY-MM-DD): ")
            manager.edytuj_zadanie(tytul, nowy_tytul, nowy_opis, nowy_termin)

        elif wybor == "5":
            manager.wyswietl_zadania()

        elif wybor == "6":
            manager.zapisz_do_pliku()

        elif wybor == "7":
            manager.wczytaj_z_pliku()

        elif wybor == "8":
            break
        else:
            print("Niepoprawna opcja, spróbuj ponownie.")

if __name__ == "__main__":
    main()
