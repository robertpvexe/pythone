lista_liczb = input("Wprowadź listę liczb całkowitych, a zwróce tylko te które są parzyste ")

liczby_uzytkownika_str = lista_liczb.split()

liczby_uzytkownika_int = [eval(i) for i in liczby_uzytkownika_str]

print("Liczby parzyste z podanej listy:")

for liczba in liczby_uzytkownika_int:
    if liczba % 2 == 0:
        print(liczba)
