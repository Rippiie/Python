hotelKosten = 4356
def programma():
    while True:
        try:
            aantalPersonen = int(input('Hoeveel mensen gingen er mee?: '))
            if aantalPersonen < 0:
                raise Exception
            elif aantalPersonen == 0:
                raise ZeroDivisionError
            else:
                break
        except ZeroDivisionError:
            print('Kan niet delen door 0, voer geldig getal in')
        except ValueError:
            print('Voer een geldig getal in')
        except Exception:
            print('Voer een positief getal in')
        except:
            print('Andere fout')
    uitkomst = hotelKosten / aantalPersonen
    print('de kosten zijn {}'.format(uitkomst))

programma()