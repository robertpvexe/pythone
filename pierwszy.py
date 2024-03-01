from datetime import date

dzisiaj = date.today()
dzis_rok = dzisiaj.year   
dzis_miesiac = dzisiaj.month
dzis_dzien = dzisiaj.day

rok_urodzenia = int(input("Podaj rok urodzenia: ")) 

wiek = dzis_rok - rok_urodzenia

print("Masz " + str(wiek) + " lat")
print(dzis_dzien)
